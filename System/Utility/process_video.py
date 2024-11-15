import librosa
import moviepy.editor as mp
import tempfile
import numpy as np
import os
import cv2
import dlib
from keras._tf_keras.keras.preprocessing.sequence import pad_sequences
import whisperx

class ProcessVideo():
    def __init__(self):
        # Setting for whisperx model
        self.device = "cpu" 
        self.batch_size = 16
        self.compute_type = "float32"
        
        # Dlib facelandmark data
        self.face_landmark = "Database\dlib_facelandmark\shape_predictor_68_face_landmarks.dat"
        
        # Speech to text transcription model # large-v2/base
        self.model = whisperx.load_model("base", self.device, compute_type=self.compute_type)


#============================================= Word Alignment Processing ==============================================
    def getWordAlignment(self, audio_file):
        audio = whisperx.load_audio(audio_file)
        result = self.model.transcribe(audio, batch_size=self.batch_size)

        # Word alignment model
        word_model, metadata = whisperx.load_align_model(language_code = result["language"], device = self.device)

        result = whisperx.align(result["segments"],
                            word_model,
                            metadata,
                            audio,
                            self.device,
                            return_char_alignments = False)

        return result

    def getTimestamp(self, result):
        word_timestamp = []

        for item in result["segments"]:
            for word in item.get("words"):
                start_end_timestamp = [word.get("start"),word.get("end")]
                word_timestamp.append(start_end_timestamp)

        return word_timestamp


#================================================== Audio Processing ==================================================
    def generate_spectrogram(self, y, sr, start_time, end_time):
        # Extract the desired clip
        clip = y[int(start_time*sr):int(end_time*sr)]
        
        # Compute the spectrogram
        Mel_spectrogram = librosa.feature.melspectrogram(y=clip)
        
        log_spectrogram = librosa.power_to_db(Mel_spectrogram, ref=np.max)

        return log_spectrogram
        

#================================================== Video Processing ==================================================

    def mouth_extractor(self, cap, start_timestamp, end_timestamp, fps):
        face_detector = dlib.get_frontal_face_detector()
        dlib_facelandmark = dlib.shape_predictor(self.face_landmark)

        # Define fixed size for the mouth ROI
        fixed_width = 100
        fixed_height = 50

        # Get frame rate
        start_frame = int(start_timestamp * fps)
        end_frame = int(end_timestamp * fps)

        # Set the starting frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        processed_frame = [] # final processed frame

        missing_frame_thres = (end_frame - start_frame) / 2 # threshold for termination based on missing frame

        missing_frame = 0 # number of missing frame

        first_frame = True
        num_face_registered = 0 # number of face detected across frame

        all_face = {} # Save all extracted mouth region for each person in the video
        mouth_open_close_series = {} # Save the difference between mouth top (y) and mouth bottom (y) to determine which person is speaking

        for frame_number in range(start_frame, end_frame+1):
            ret, frame = cap.read()

            if not ret:
                print("Failed to read frame from video.")
                return []

            if (missing_frame >= missing_frame_thres):
                print("Too many missing frame at this section")
                return []

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector(gray)

            num_face_detected = len(faces)

            # Check if no faces were detected
            if num_face_detected == 0:
                missing_frame = missing_frame + 1
                continue

            # detected new face in the following frame (after first frame), register new mouth x coordinate
            if (num_face_detected > num_face_registered) and not first_frame:

                # repeat the process by the number of new face detected
                for i in range(num_face_detected - num_face_registered):
                    mouth_distance = {}
                    
                    for face in faces:
                        # get face landmarks
                        landmarks = dlib_facelandmark(gray, face)

                        # extract mouth landmark at 48 as ID
                        mouth_x = landmarks.part(48).x - 15
                        
                        # Find the nearest mouth in the registered face
                        nearest_distance = [0,100000]
                        for registered_mouth in all_face:
                            # Find the distance between two mouth in x coordinate
                            difference = abs(registered_mouth - mouth_x)
                            
                            # Identify the nearest mouth
                            if (difference < nearest_distance[1]):
                                nearest_distance = [mouth_x, difference]
                        
                        mouth_distance[nearest_distance[0]] = nearest_distance[1]
                    
                    farthest = [0,0]
                    # Find the mouth with the largest difference in distance
                    for key, distance in mouth_distance.items():
                        if distance > farthest[1]:
                            farthest[0] = key
                            farthest[1] = distance
                    
                    # register new mouth with empty list
                    all_face[farthest[0]] = [] # mouth region
                    mouth_open_close_series[farthest[0]] = 0 # difference between top lip (y) and bottom lip (y)

                # update number of face registered
                num_face_registered = num_face_detected


            for face in faces:
                # get face landmarks
                landmarks = dlib_facelandmark(gray, face)

                # extract mouth region
                mouth_x = landmarks.part(48).x - 15
                mouth_y = landmarks.part(51).y - 15
                mouth_w = landmarks.part(54).x - mouth_x + 15
                mouth_h = landmarks.part(57).y - mouth_y + 15


                # When first frame, register the mouth x coordinate to the dictionary
                if first_frame:
                    num_face_registered = num_face_detected
                    all_face[mouth_x] = [gray[mouth_y:mouth_y + mouth_h, mouth_x:mouth_x + mouth_w]] # mouth region
                    mouth_open_close_series[mouth_x] = abs(landmarks.part(63).y - landmarks.part(67).y) # difference between top lip (y) and bottom lip (y)


                else:
                    # Append to the nearest mouth_x list
                    nearest_x = [99999,0]

                    for mouth in all_face:
                        difference = abs(mouth - mouth_x)
                        if (difference < nearest_x[0]):
                            nearest_x[0] = difference # difference between two mouth x coordinate
                            nearest_x[1] = mouth # key

                    # Append the frame to the nearest mouth (key)
                    all_face[nearest_x[1]].append(gray[mouth_y:mouth_y + mouth_h, mouth_x:mouth_x + mouth_w]) # mouth region
                    mouth_open_close_series[nearest_x[1]] = mouth_open_close_series[nearest_x[1]] + abs(landmarks.part(63).y - landmarks.part(67).y) # add the difference between top lip (y) and bottom lip (y)


                    # update the mouth x coordinate (key) with the latest position
                    all_face[mouth_x] = all_face.pop(nearest_x[1])
                    mouth_open_close_series[mouth_x] = mouth_open_close_series.pop(nearest_x[1])

            first_frame = False
        
        # Determine the current speaker by the difference between mouth top and bottom position across frame
        # The speaker will have the largest the difference across frame because they will open and close their mouth
        speaker_key = max(mouth_open_close_series, key=mouth_open_close_series.get)

        # check number of frame. Return empty list when too many missing frame
        if len(all_face[speaker_key]) <= missing_frame_thres:
            return []

        # Resize frame
        for mouth_roi in all_face[speaker_key]:
            if mouth_roi.shape[1] < fixed_width or mouth_roi.shape[0] < fixed_height:
                interpolation_set = cv2.INTER_CUBIC # For upsampling
            else:
                interpolation_set = cv2.INTER_AREA # For downsampling

            resized_mouth_roi = cv2.resize(mouth_roi, (fixed_width, fixed_height), interpolation=interpolation_set)

            # Normalize the resized frame by dividing it with 255 so that each pixel value then lies between 0 and 1
            normalized_frame = resized_mouth_roi / 255

            processed_frame.append(normalized_frame)

        return processed_frame

#================================================== Start Processing ==================================================
    def extract_video_audio(self, video_path, is_running_flag):
        video_data = []
        audio_data = []

        # load the video file
        video = mp.VideoFileClip(video_path)

        audio = video.audio

        audio_path = "D:\OneDrive - Asia Pacific University\Degree Year 3\Sem 2\Final Year Project\Deepfake Detection System\\Temp_folder_audio\\temp.wav"
        audio.write_audiofile(audio_path)
        
        # get word alignment result
        alignment_result = self.getWordAlignment(audio_path)

        y, sr = librosa.load(audio_path)

        os.remove("Temp_folder_audio\\temp.wav")
                   
            
        # Get start and end timestamp for each word in the audio file
        word_timestamp = self.getTimestamp(alignment_result)
        
        for timestamp in word_timestamp:
            if not is_running_flag():
                return False, False, False
            
            # ensure the timestamp is not empty
            if (timestamp[0] == None ):
                continue
                
            print(f"Timestamp -> {timestamp[0]} - {timestamp[1]}")
            # Read video MP4 File
            cap = cv2.VideoCapture(video_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            print("FPS: ", fps)

            # timestamp[0] -> start time | timestamp[1] -> end time
            processed_video = self.mouth_extractor(cap, timestamp[0], timestamp[1], fps)

            # Process and convert audio data to log mel spectrogram
            processed_audio = self.generate_spectrogram(y, sr, timestamp[0], timestamp[1])
            
            if not processed_video:
                continue
            
            video_data.append(processed_video)
            audio_data.append(processed_audio)

        cap.release()

        return self.prepare_data(word_timestamp, video_data, audio_data)
    

    def prepare_data(self, word_timestamp, video_data, audio_data):
        # Add padding to video data
        video_data = pad_sequences(video_data, maxlen = 19, dtype='float32', padding='post', truncating='post', value=0.0 )

        # Add channel dimension
        video_data = np.expand_dims(video_data, axis = -1)

        # Find global min and max of log mel spectrogram for normalziation purpose
        global_min = min(np.min(spectrogram) for spectrogram in audio_data)
        global_max = max(np.max(spectrogram) for spectrogram in audio_data)
        print("global min", global_min)
        print("global max", global_max)
        for i, audio in enumerate(audio_data):
            # transpose audio data
            transpose_audio = audio.transpose()
            
            # Normalize the log-mel spectrogram
            normalized_audio = (transpose_audio - global_min) / (global_max - global_min)
            
            audio_data[i] = normalized_audio
            

        # add paddding to audio data
        audio_data = pad_sequences(audio_data, maxlen = 25, dtype='float32', padding='post', truncating='post', value=0.0 )


        return word_timestamp, np.array(video_data), np.array(audio_data)