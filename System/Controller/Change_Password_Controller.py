from PyQt5.QtWidgets import QMainWindow, QMessageBox
from UI_Screen.Change_Password_Screen import Ui_MainWindow
from enums import Pages
from Utility.validation_module import *
from Utility.message_manager import MessageManager

class ChangePasswordController(QMainWindow):
    def __init__(self, router, db_connection, forget_password_controller):
        super(ChangePasswordController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router
        self.db_connection = db_connection
        self.forget_password_controller = forget_password_controller
        self.user_email = None

        # Connect the register button to the navigate_register method
        self.ui.back_login_button.clicked.connect(self.navigate_login)
        self.ui.confirm_button.clicked.connect(self.change_password)

        # Receive email from forget_password_controller
        self.forget_password_controller.email_passed.connect(self.receive_email)

    def reset_field(self):
        self.ui.confirm_password_edit.setText("")
        self.ui.password_edit.setText("")
        self.ui.error_password.setText("")
        self.ui.error_con_password.setText("")

    def receive_email(self, email):
        self.user_email = email

    def navigate_login(self):
        self.router.setCurrentIndex(Pages.LOGIN.value)


    # Change user password
    def change_password(self):
        err_pass = password_validation(self.ui.password_edit.text())
        err_con_pass = confirm_password_validation(self.ui.password_edit.text(), self.ui.confirm_password_edit.text())

        # Check error message
        if err_pass == "" and err_con_pass == "":
            # update password
            query = f"UPDATE user SET password = '{self.ui.password_edit.text()}' WHERE email = '{self.user_email}'"
            self.db_connection.execute_query(query)
            self.reset_field()
            # Show success message using QMessageBox
            MessageManager.show_message(QMessageBox.Information, "Change password", "Your password has been updated successfully!")

        
            self.navigate_login()
        else:
            # Show error message
            self.ui.error_password.setText(err_pass)
            self.ui.error_con_password.setText(err_con_pass)

        
