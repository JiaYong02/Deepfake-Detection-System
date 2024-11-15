from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from UI_Screen.Forget_Password_Screen import Ui_MainWindow
from enums import Pages
from Model.User import User


class ForgetPasswordController(QMainWindow):

    email_passed = pyqtSignal(str)
    
    def __init__(self, router, db_connection):
        super(ForgetPasswordController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router
        self.db_connection = db_connection

        # Connect the register button to the navigate_register method
        self.ui.back_login_button.clicked.connect(self.navigate_login)
        self.ui.next_button.clicked.connect(self.navigate_verification)

    def reset_field(self):
        self.ui.error_email.setText("")
        self.ui.email_edit.setText("")

    # Navigate to login page
    def navigate_login(self):
        self.reset_field()
        self.router.setCurrentIndex(Pages.LOGIN.value)

    # Pass email to verification controller
    def navigate_verification(self):
        user_email = self.ui.email_edit.text()

        if (not user_email):
            self.ui.error_email.setText("*Please provide your email address.")
        elif(User(user_email, "", "",self.db_connection).check_existance()):
            self.ui.error_email.setText("*This email address does not exist! Try again.")
        else:
            # Send the email address to the verification page
            self.email_passed.emit(user_email)

            self.reset_field()
            # Navigate to verification page 
            self.router.setCurrentIndex(Pages.VERIFICATION.value)
    
    