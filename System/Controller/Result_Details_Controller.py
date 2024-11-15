from UI_Screen.Result_Details_Screen import Ui_MainWindow
# from Controller.Main_Window import MainWindow
from enums import Pages
from Model.User import User
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QMessageBox, QPushButton, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from Utility.message_manager import MessageManager
from functools import partial

class ResultDetailsController(QMainWindow):
    def __init__(self, router, db_connection, result_controller):
        super(ResultDetailsController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router
        self.db_connection = db_connection
        self.result_controller = result_controller
        self.detection = None
        
        self.ui.video_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
         # Set the first column to resize to content
        self.ui.video_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.video_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.video_table.setColumnWidth(0, 200)
        self.ui.video_table.setColumnWidth(1, 600)
        
  
        
        # Receive detection result information from result controller
        self.result_controller.detection_passed.connect(self.receive_detection)
        self.ui.back_button.clicked.connect(self.navigate_back)

    # Get logged user information
    def receive_detection(self, detection):
        self.detection = detection

        # Set information
        self.ui.upload_date_edit.setText(detection.upload_date)
        self.ui.upload_time_edit.setText(detection.upload_time)
        self.ui.completion_time_edit.setText(detection.completion_time)
        self.ui.source_edit.setText(detection.source)

        # Query to get video list
        query = f"SELECT file_name, file_path, status, result, ai_frame FROM video WHERE detection_id = {detection.detection_id}"
        
        result = self.db_connection.execute_query(query)

        # check if got error
        if (result[0] != ""):
            MessageManager.show_message(QMessageBox.Critical, "Error", "Failed to retrive data for video list")
        else:
            # get the cursor and fetch the rows
            data = result[1].fetchall()

            # Set total video
            self.ui.total_video_edit.setText(str(len(data)))

            self.populate_table(data)

    # Insert data into table        
    def populate_table(self, data_list):
        # remove all row in table to avoid duplicate
        self.remove_all_rows()
        count_fake_video = 0

        for row_number, data in enumerate(data_list):
            # Create new row
            self.ui.video_table.insertRow(row_number)

            
            for index, column_value in enumerate(data):
                
                if index == 4:
                    if data[3] == 'Fake':
                        count_fake_video = count_fake_video + 1

                        # Create view button that pass the detection id when clicked 
                        view_button = QPushButton("View")
                        view_button.clicked.connect(lambda checked, fake_image=column_value: self.view_fake_frame(fake_image))
                        self.ui.video_table.setCellWidget(row_number, index, view_button)
                        continue
                    else:
                        column_value = "-"
                        
                new_item = QTableWidgetItem(column_value)
                new_item.setFlags(new_item.flags() & ~Qt.ItemIsEditable)  # Make the cell non-editable
                
                # set center alignment except for path column
                if index != 1:
                    new_item.setTextAlignment(Qt.AlignCenter)

                self.ui.video_table.setItem(row_number, index, new_item)
        
        # Set total fake video
        self.ui.num_deepfake_edit.setText(str(count_fake_video))

        self.ui.video_table.setWordWrap(True)
        self.ui.video_table.resizeRowsToContents()

    def view_fake_frame(self, fake_image):
        self.image_window = ImageWindow(fake_image)
        self.image_window.show()

    def navigate_back(self):
        self.router.setCurrentIndex(Pages.RESULT.value)

    def remove_all_rows(self):
        # Get the number of rows currently in the table
        num_rows = self.ui.video_table.rowCount()

        # Remove rows in reverse order to avoids index shifting issues 
        for i in range(num_rows - 1, -1, -1):
            self.ui.video_table.removeRow(i)

class ImageWindow(QMainWindow):
    def __init__(self, image_data):
        super().__init__()
        self.setWindowTitle("Fake Frame")
        self.setGeometry(100, 100, 500, 500)

        # Convert blob data to QImage
        image = QImage.fromData(image_data)
        
        # Convert QImage to QPixmap
        pixmap = QPixmap.fromImage(image)
        
        # Create a label to display the image
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        # Set central widget
        self.setCentralWidget(label)


