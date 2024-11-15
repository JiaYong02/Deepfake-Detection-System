from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UI_Screen.Register_Screen import Ui_MainWindow
from enums import Pages
from Model.User import User
from Utility.validation_module import *
from Utility.message_manager import MessageManager
import re

class RegisterController(QMainWindow):
    def __init__(self, router, db_connection):
        super(RegisterController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router
        self.db_connection = db_connection

        # Connect the login button to the navigate_login method
        self.ui.login_button.clicked.connect(self.navigate_login)
        self.ui.register_button.clicked.connect(self.register_user)

    def navigate_login(self):
        self.reset_field()
        self.router.setCurrentIndex(Pages.LOGIN.value)

    # Create new user account
    def register_user(self):
        # Get user input
        email = self.ui.email_edit.text()
        password = self.ui.password_edit.text()
        confirm_password = self.ui.confirm_password_edit.text()
        full_name = self.ui.full_name_edit.text()

        # Input validation
        if self.validate_input(email, password, confirm_password, full_name):
            
            # Create user
            user = User(email, password, full_name, self.db_connection)
            if (user.check_existance()):
                user.register_user()
                # Pop up message to notify user
                MessageManager.show_message(QMessageBox.Information, "Registration", "Your account has been registered successfully!")
                self.navigate_login()
                
            else:
                self.ui.error_email.setText("Email Address existed, Please use another email")

    def validate_input(self, email, password, confirm_password, full_name):
        # validation user input
        err_email = email_validation(email)
        err_password = password_validation(password)
        err_con_pass = confirm_password_validation(password, confirm_password)
        err_name = full_name_validation(full_name)

        # Set error message
        self.ui.error_email.setText(err_email)
        self.ui.error_name.setText(err_name)
        self.ui.error_pass.setText(err_password)
        self.ui.error_con_pass.setText(err_con_pass)

        return (err_email == "" and err_name == "" and err_password == "" and err_con_pass == "")

    # Clear out all the input and error messages
    def reset_field(self):
        self.ui.email_edit.setText("")
        self.ui.password_edit.setText("")
        self.ui.confirm_password_edit.setText("")
        self.ui.full_name_edit.setText("")
        self.ui.error_email.setText("")
        self.ui.error_name.setText("")
        self.ui.error_pass.setText("")
        self.ui.error_con_pass.setText("")

    

        