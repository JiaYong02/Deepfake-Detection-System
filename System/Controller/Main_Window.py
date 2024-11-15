from PyQt5.QtWidgets import QMainWindow
from enums import Pages
from Utility.message_manager import MessageManager
from Utility.task import Task
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, ui, router):
        super(MainWindow, self).__init__()
        self.ui = ui
        self.ui.setupUi(self)
        self.router = router
        self.task = Task() # To keep track of worker (detection task)

        # Connect the button to function 
        self.ui.notification_button.clicked.connect(self.navigate_notification)
        self.ui.dashboard_button.clicked.connect(self.navigate_dashboard)
        self.ui.result_button.clicked.connect(self.navigate_result)
        self.ui.upload_video_button.clicked.connect(self.navigate_upload_video)
        self.ui.profile_button.clicked.connect(self.navigate_profile)
        self.ui.logout_button.clicked.connect(self.logout)

    def navigate_notification(self):
        self.router.setCurrentIndex(Pages.NOTIFICATION.value)
    
    def navigate_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)

    def navigate_result(self):
        self.router.setCurrentIndex(Pages.RESULT.value)

    def navigate_upload_video(self):
        self.router.setCurrentIndex(Pages.UPLOAD_VIDEO.value)

    def navigate_profile(self):
        self.router.setCurrentIndex(Pages.PROFILE.value)

    def logout(self):
        # Display message box
        if (MessageManager.message_with_action(QMessageBox.Warning, "Logout", "Are you sure you want to logout?", "All detection task will be terminated.")):
            # Terminate and remove all detection task for the user
            self.task.clear_session()
            # Navigate to login page
            self.router.setCurrentIndex(Pages.LOGIN.value)


    

