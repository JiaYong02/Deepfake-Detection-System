from UI_Screen.Upload_Video_Screen import Ui_MainWindow
from Controller.Main_Window import MainWindow
from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem, QMessageBox, QTableWidgetItem, QHeaderView, QPushButton, QProgressBar
from PyQt5.QtCore import QUrl, QTimer, Qt, QThread, pyqtSignal
from queue import Queue
from enums import Pages
from Model.Video import Video
from Model.Detection import Detection
from Model.Notification import Notification
from Utility.datetime_manager import DatetimeManager
from Utility.message_manager import MessageManager
import time
import os

class UploadVideoController(MainWindow):

    detection_complete_signal = pyqtSignal(bool)

    def __init__(self, router, db_connection, login_controller):
        self.ui = Ui_MainWindow()
        super(UploadVideoController, self).__init__(self.ui, router)
        self.db_connection = db_connection
        self.login_controller = login_controller
        self.logged_user = None
        self.video_list = []
        self.current_worker_status = True
        
        # Receive logged user from login_controller
        self.login_controller.user_passed.connect(self.receive_user)

        self.ui.browse_file_button.clicked.connect(self.browse_file)
        self.ui.browse_folder_button.clicked.connect(self.browse_folder)

        self.ui.video_tree_list.setColumnCount(1)
        self.ui.video_tree_list.setHeaderLabels(["Files"])
        self.root_item = QTreeWidgetItem(self.ui.video_tree_list)
        self.root_item.setText(0, "Files") 

        # hide source text field
        self.ui.video_source_edit.hide()

        # Set radio button
        self.ui.existing_radio.setChecked(True)
        self.ui.existing_radio.toggled.connect(self.source_selection)
        self.ui.new_radio.toggled.connect(self.source_selection)
        self.fill_existing_video_source()

        # Link button
        self.ui.remove_button.clicked.connect(self.remove_selected_file)
        self.ui.reset_button.clicked.connect(self.remove_all_file)
        self.ui.upload_button.clicked.connect(self.upload_for_detection)
        
        self.ui.progress_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def receive_user(self, logged_user):
        self.logged_user = logged_user
        self.clear_table()
        self.fill_existing_video_source()

    def source_selection(self):
        if self.ui.new_radio.isChecked():
            self.ui.video_source_edit.setVisible(True) # unhide text field
            self.ui.source_combo.hide() # hide text field

        elif self.ui.existing_radio.isChecked():
            self.ui.video_source_edit.hide # hide text field
            self.ui.source_combo.setVisible(True) # unhide combo box

            self.ui.source_combo.clear() # clear item to avoid duplication
            self.fill_existing_video_source()
            
    
    def fill_existing_video_source(self):
        if self.logged_user != None:
            self.ui.source_combo.clear()
            
            # get existing source from database
            query = f"SELECT DISTINCT source from detection WHERE user_id = '{self.logged_user.email}'"

            result = self.db_connection.execute_query(query)[1].fetchall()

            for source in result:
                self.ui.source_combo.addItem(str(source[0]))

    def get_source(self):
        if self.ui.new_radio.isChecked():
            return self.ui.video_source_edit.text().lower()

        elif self.ui.existing_radio.isChecked():
            return self.ui.source_combo.currentText()
            

    # Select single or multiple file
    def browse_file(self):
        # Filter out non-video file
        video_filters = "Video Files (*.mp4 *.avi *.mov *.wmv);"

        # Get user input
        file_names, _ = QFileDialog.getOpenFileUrls(self, 'Browse Videos', QUrl(), video_filters)

        # Read and store file
        for file_url in file_names:
            file_url = file_url.toLocalFile()
            print("File ", file_url)
            # Append file url if it does not exist
            if (file_url not in self.video_list):
                self.video_list.append(file_url)
                self.add_files(file_url.split("/")[-1]) # display in tree widget

    # Upload entire folder
    def browse_folder(self):
        # Get folder path
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "")

        # Avoid error when user click on multiple times
        if (folder_path == ""):
            return    

        # Read and store all the file under the folder excluding non-video file and folder
        for file_name in os.listdir(folder_path):
            file_path = folder_path + "/" + file_name
            print("Folder ", file_path)
            if not os.path.isdir(file_path) and file_path.lower().endswith((".mp4", ".avi", ".mov", ".wmv")) and file_path not in self.video_list:
                self.video_list.append(file_path)
                self.add_files(file_name) # display in tree widget

    # Add data to tree widget
    def add_files(self, file):
        item = QTreeWidgetItem(self.root_item)
        item.setText(0, file)

    # Delete file from tree widget
    def remove_selected_file(self):
        # get selected items
        selected_items = self.ui.video_tree_list.selectedItems()

        if selected_items:
            selected_item = selected_items[0]
            parent_item = selected_item.parent()
            if parent_item:
                # remove item
                parent_item.removeChild(selected_item)
                self.video_list.pop(parent_item.indexOfChild(selected_item))
        else:
            # display error message if no item selected
            MessageManager.show_message(QMessageBox.Warning, "No items selected", "Please select a file to remove")
            

    # Clear all uploaded file
    def remove_all_file(self):
        child_count = self.root_item.childCount()
        for i in range(child_count - 1, -1, -1):
            child_item = self.root_item.child(i)
            self.root_item.removeChild(child_item)
        self.video_list.clear()

    # Upload file to perform detection 
    def upload_for_detection(self):
        video_source = self.get_source().lower().strip()

        # check if the list is empty
        if not self.video_list:
            MessageManager.show_message(QMessageBox.Warning, "No file uploaded", "Please upload files for detection.")
        elif len(self.video_list) > 50:
            MessageManager.show_message(QMessageBox.Warning, "Exceeded file limit", "You can only upload a maximum of 50 video for each detection!")
        elif not video_source:
            MessageManager.show_message(QMessageBox.Warning, "Null source", "Please provide the source of video.")
        elif len(video_source) < 5:
            MessageManager.show_message(QMessageBox.Warning, "Warning", "The video source must have a minimum length of 5.")
        elif len(video_source) > 30:
            MessageManager.show_message(QMessageBox.Warning, "Warning", "The video source cannot exceed 30 character.")
        else:
        # Create detection object to call detection function
            detection = Detection(
                            DatetimeManager.get_current_date(),
                            DatetimeManager.get_current_time(),
                            video_source,
                            self.db_connection,
                            video_list=[]
                        )
            
            # detection.video_list.clear()

            # Create video object for each file uploaded
            for video_path in self.video_list:
                print(video_path)
                video = Video(
                            video_path,
                            video_path.split("/")[-1],
                            "In Progress",
                            self.db_connection
                        )
                # Add video to detection object
                detection.add_video(video)
            
            print("Before number video: ",len(self.video_list))
            print("time ", detection.get_number_video())
            # Clear tree item and video list
            self.remove_all_file()
            self.ui.video_source_edit.setText("")

            # Create new row to progress table and start detection
            self.insert_row(detection)

            print("number video: ",len(self.video_list))

        
    # Insert new row to progress table
    def insert_row(self, detection):
        # get  row index
        row_position = self.ui.progress_table.rowCount()
        
        # Insert row to table
        self.ui.progress_table.insertRow(row_position)

        cell_data = [str(detection.upload_date), detection.upload_time, str(len(detection.video_list)), detection.source]
        
        # Create cell for the row
        for column_index in range(4):
            new_item = QTableWidgetItem(cell_data[column_index])
            self.ui.progress_table.setItem(row_position, column_index, new_item)

        # Create progress bar for each detection row
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 100)
        progress_bar.setValue(0)
        self.ui.progress_table.setCellWidget(row_position, 4, progress_bar)

        # Create worker object (thread) to avoid freezing the UI while performing detection 
        worker = Worker(detection)
        worker.progress.connect(progress_bar.setValue)
        worker.finished.connect(lambda: self.delete_progress_row(progress_bar, worker, detection))
        
        # keep track on worker object
        self.task._task_list.append(worker)
        
        # start the worker only when there is only one worker
        if (len(self.task._task_list) == 1):
            print(self.task._task_list)
            print(worker)
            worker.start()
        
        # Create delete button 
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(lambda: self.cancel_detection(cancel_button))
        self.ui.progress_table.setCellWidget(row_position, 5, cancel_button)

    def cancel_detection(self, button):
        if (MessageManager.message_with_action(QMessageBox.Warning, "Cancel detection task", "Are you sure you want to cancel this detection?")):
            index = self.ui.progress_table.indexAt(button.pos())
            if index.isValid():
                row = index.row()
                
                worker = self.task._task_list[row]
                worker.stop()  # Set the flag to stop the thread
                
                if (row != 0):
                    # Remove the worker from the list
                    self.task._task_list.pop(row)
                    self.ui.progress_table.removeRow(row)
                


    # delete table row when the detection completed
    def delete_progress_row(self, progress_bar, worker, detection):
        self.worker_finished()

        # Get table row and remove the worker
        index = self.ui.progress_table.indexAt(progress_bar.pos())
        if index.isValid():
            row = index.row()
            self.ui.progress_table.removeRow(row)
        
        if not worker.is_running:
            return
        
        # Create record in database
        detection.create_record(self.logged_user.email)

        # Create notification
        title = f"Detection task completed"
        content = f"Your detection task created on {detection.upload_date}, {detection.upload_time} has completed on {detection.completion_time}. There are {detection.get_number_deepfake()} deepfake video detected out of {detection.get_number_video()} video. Go check it out at result page!"
        Notification(title, content, self.logged_user.email, DatetimeManager.get_current_date(), DatetimeManager.get_current_time(), self.db_connection).create_notification()

        # Pop up message to notify user
        MessageManager.show_message(QMessageBox.Information, "Detection complete", "Your detection task has completed")

        # send signal to result controller to notify the event changes 
        self.fill_existing_video_source()
        self.detection_complete_signal.emit(True)


    # Handle completion of a worker/thread
    def worker_finished(self):
        # remove completed worker
        self.task._task_list.pop(0)

        # start the next worker
        if (len(self.task._task_list) != 0):
            self.task._task_list[0].start()

    # Clear table row
    def clear_table(self):
        # Get the number of rows currently in the table
        num_rows = self.ui.progress_table.rowCount()

        # Remove rows in reverse order to avoids index shifting issues 
        for i in range(num_rows - 1, -1, -1):
            self.ui.progress_table.removeRow(i)


class Worker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, detection):
        super(Worker, self).__init__()
        self.detection = detection
        self.is_running = True  # Flag to control thread execution

    def run(self):
        # Use lambda to ensure the flag is checked rather than passing static value
        self.detection.start_detection(self.progress, lambda: self.is_running) 
        self.finished.emit()


    def stop(self):
        self.is_running = False
