from UI_Screen.Notification_Screen import Ui_MainWindow
from Controller.Main_Window import MainWindow
from enums import Pages
from Model.User import User
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QFont

class NotificationController(MainWindow):
    def __init__(self, router, db_connection, login_controller, upload_video_controller):
        self.ui = Ui_MainWindow()
        super(NotificationController, self).__init__(self.ui, router)
        self.db_connection = db_connection
        self.login_controller = login_controller
        self.upload_video_controller = upload_video_controller

        # Receive logged user from login_controller
        self.login_controller.user_passed.connect(self.receive_user)

        # Receive signal from upload video controller to update the notification
        self.upload_video_controller.detection_complete_signal.connect(self.get_notification)


    # Get logged user information
    def receive_user(self, logged_user):
        self.logged_user = logged_user
        self.get_notification()

    # Retrieve notification data from the database 
    def get_notification(self):
        # clear the list to avoid duplicates
        self.ui.notification_list.clear()

        
        query = f"SELECT title, content, created_date, created_time FROM notification WHERE user_id = '{self.logged_user.email}' ORDER BY notification_id DESC"

        notification_data = self.db_connection.execute_query(query)[1].fetchall()

        for notification in notification_data:
            # Add title
            title_item = QListWidgetItem(notification[0])
            title_item.setFont(QFont("Arial", 12, QFont.Bold))
            self.ui.notification_list.addItem(title_item)

            # add date time of notification
            post_time = f"{notification[2]} - {notification[3]}"
            self.ui.notification_list.addItem(post_time)

            # add content
            self.ui.notification_list.addItem(notification[1])
            self.ui.notification_list.addItem("")

        
        

   