from UI_Screen.Result_Screen import Ui_MainWindow
from Controller.Main_Window import MainWindow
from Model.Detection import Detection
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QMessageBox, QPushButton
from Utility.message_manager import MessageManager
from Utility.datetime_manager import DatetimeManager
from PyQt5.QtCore import pyqtSignal, QDate
from enums import Pages

class ResultController(MainWindow):

    detection_passed = pyqtSignal(Detection)

    def __init__(self, router, db_connection, login_controller, upload_video_controller):
        self.ui = Ui_MainWindow()
        super(ResultController, self).__init__(self.ui, router)
        self.db_connection = db_connection
        self.login_controller = login_controller
        self.upload_video_controller = upload_video_controller
        self.logged_user = None
        self.current_data = None
        
        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.to_date_edit.setDate(QDate.currentDate())
        self.ui.to_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.ui.from_date_edit.setDisplayFormat("yyyy-MM-dd")

        self.ui.result_combo.addItem("All")
        self.ui.result_combo.addItem("Deepfake")
        self.ui.result_combo.addItem("Real Only")

        # Link button
        self.ui.search_button.clicked.connect(self.populate_table)

        # Receive logged user from login_controller
        self.login_controller.user_passed.connect(self.receive_user)

        # Receive signal from upload video controller
        self.upload_video_controller.detection_complete_signal.connect(self.update_table_information)
        
    # Get logged user information
    def receive_user(self, logged_user):
        self.logged_user = logged_user

        # get detection result data from database
        self.update_table_information()
    
    # Get detection complete signal from upload video controller
    def update_table_information(self):
        # update table data
        self.get_data()
        self.get_video_source()

    # get detection result data from database
    def get_data(self):
        query = f"""
            SELECT t1.upload_date, t1.upload_time, t1.completion_time, t1.source, t2.total_video, COALESCE(t2.num_deepfake, 0) AS num_deepfake , t1.detection_id FROM 
            (SELECT upload_date, upload_time, completion_time, source,  detection_id 
                from detection WHERE user_id = '{self.logged_user.email}') t1
            INNER JOIN
            (SELECT detection_id, CAST(COUNT(detection_id) AS text) AS total_video, SUM(CASE WHEN result = 'Fake' THEN 1 ELSE 0 END) AS num_deepfake FROM video GROUP BY detection_id) t2
            ON t1.detection_id = t2.detection_id
            ORDER BY t1.detection_id DESC
        """
        
        result = self.db_connection.execute_query(query)

        # check if got error
        if (result[0] != ""):
            print(result[0])
            MessageManager.show_message(QMessageBox.Critical, "Data retrieval error", "Failed to retrive data for detection result")
        else:
            # get the cursor and fetch the rows
            data = result[1].fetchall()
            self.current_data = data
            self.populate_table()
    
    # insert data into table
    def populate_table(self):
        # Get filter condition
        from_date = self.ui.from_date_edit.text()
        to_date = self.ui.to_date_edit.text()
        source_filter = self.ui.source_combo.currentText()
        result_filter = self.ui.result_combo.currentText()

        # Avoid from_date is later than to_date
        if (DatetimeManager.compare_dates(from_date,  to_date)) > 0:
            MessageManager.show_message(QMessageBox.Critical, "Invalid Date", "The 'from date' cannot be later than 'to date'")
            return

        self.remove_all_rows()
        
        row_number = 0
        for data in self.current_data:
            # Create detection object 
            detection_ins = Detection(upload_date= data[0], upload_time=data[1], source=data[3], db_connection=self.db_connection, completion_time=data[2], detection_id=data[6])

            # Filter by date
            if not (DatetimeManager.compare_dates(data[0], self.ui.from_date_edit.text()) >= 0 and DatetimeManager.compare_dates(data[0], self.ui.to_date_edit.text()) <= 0):
                continue
            
            if source_filter == "":
                source_filter = "All"

            if (source_filter != "All"):
                if (data[3] != source_filter):
                    continue
            
            
            # Filter by result
            if (((result_filter == "Deepfake" and data[5] == 0) or (result_filter == "Real Only" and data[5] != 0)) and (result_filter != "All")):
                continue
            
            print(data[3])
            # Create new row
            self.ui.result_table.insertRow(row_number)

            for index, column_value in enumerate(data):
                if index == 6:
                    # Create view button that pass the detection id when clicked 
                    view_button = QPushButton("View")
                    view_button.clicked.connect(lambda checked, detection_id=detection_ins: self.view_result_details(detection_id))
                    self.ui.result_table.setCellWidget(row_number, index, view_button)
                else:
                    new_item = QTableWidgetItem(str(column_value))
                    self.ui.result_table.setItem(row_number, index, new_item)

            row_number+=1

    def view_result_details(self, detection):
        self.detection_passed.emit(detection)
        self.router.setCurrentIndex(Pages.RESULT_DETAILS.value)


    def get_video_source(self):
        # Remove all item first to avoid duplication
        self.ui.source_combo.clear()

        # get existing source from database
        query = f"SELECT DISTINCT source from detection WHERE user_id = '{self.logged_user.email}'"

        result = self.db_connection.execute_query(query)[1].fetchall()
        
        self.ui.source_combo.addItem("All")

        for source in result:
            self.ui.source_combo.addItem(str(source[0]))

    def remove_all_rows(self):
        # Get the number of rows currently in the table
        num_rows = self.ui.result_table.rowCount()

        # Remove rows in reverse order to avoids index shifting issues 
        for i in range(num_rows - 1, -1, -1):
            self.ui.result_table.removeRow(i)


    