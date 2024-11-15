from UI_Screen.Profile_Screen import Ui_MainWindow
from Controller.Main_Window import MainWindow
from enums import Pages
from Model.User import User
from Utility.message_manager import MessageManager
from PyQt5.QtWidgets import QMessageBox
from Utility.validation_module import *
class ProfileController(MainWindow):
    def __init__(self, router, db_connection, login_controller):
        self.ui = Ui_MainWindow()
        super(ProfileController, self).__init__(self.ui, router)
        self.db_connection = db_connection
        self.login_controller = login_controller
        self.logged_user = None
        self.edit_mode = None
        
        # Receive logged user from login_controller
        self.login_controller.user_passed.connect(self.receive_user)

        # Connect button
        self.ui.edit_name_button.clicked.connect(self.edit_name)
        self.ui.edit_password_button.clicked.connect(self.change_password)
        self.ui.cancel_button.clicked.connect(self.reset_field)
        self.ui.save_button.clicked.connect(self.update_user_data)
        

    # Get logged user information
    def receive_user(self, logged_user):
        self.logged_user = logged_user
        self.reset_field()

    def reset_field(self):
        self.ui.email_edit.setText(self.logged_user.email)
        self.ui.name_edit.setText(self.logged_user.full_name)
        self.ui.password_edit.setText(self.logged_user.password)
        self.ui.current_pass_edit.setText("")
        self.ui.new_pass_edit.setText("")
        self.ui.confirm_pass_edit.setText("")
        self.ui.current_pass_error.setText("")
        self.ui.new_pass_error.setText("")
        self.ui.confirm_pass_error.setText("")
        self.ui.name_error.setText("")
        self.ui.name_edit.setReadOnly(True)
        self.set_pass_visible(False)
        self.set_edit_mode(False)

    def edit_name(self):
        self.set_pass_visible(False)
        self.set_edit_mode(True)
        self.ui.name_edit.setReadOnly(False)
        self.edit_mode = "name"

    def change_password(self):
        self.set_pass_visible(True)
        self.set_edit_mode(True)
        self.ui.name_edit.setReadOnly(True)
        self.edit_mode = "password"
    

    def set_pass_visible(self, bool):
        # hide or unhide button and label
        self.ui.current_pass_edit.setVisible(bool)
        self.ui.current_pass_label.setVisible(bool)
        self.ui.new_pass_edit.setVisible(bool)
        self.ui.new_pass_label.setVisible(bool)
        self.ui.confirm_pass_edit.setVisible(bool)
        self.ui.confirm_pass_label.setVisible(bool)
    
    def set_edit_mode(self, bool):        
        self.ui.edit_name_button.setVisible(not bool)
        self.ui.edit_password_button.setVisible(not bool)
        self.ui.save_button.setVisible(bool)
        self.ui.cancel_button.setVisible(bool)

    # Edit name or password
    def update_user_data(self):
        # Edit user name
        if self.edit_mode == "name":
            # Validation
            err_name = full_name_validation(self.ui.name_edit.text())

            self.ui.name_error.setText(err_name)

            # update name if no error
            if (err_name == ""):
                # Update field
                self.logged_user.full_name = self.ui.name_edit.text()

                # Update database
                query = "UPDATE user SET full_name = (?) WHERE email = (?)"

                value = (self.logged_user.full_name, self.logged_user.email)

                error = self.db_connection.execute_query(query, value)[0]

                # Display error message
                if (error != ""):
                    MessageManager.show_message(QMessageBox.Critical, "Failed to update name", str(error))
                else:
                    MessageManager.show_message(QMessageBox.Information, "Name saved", "Your full name is updated successfully")
                self.reset_field()
        # Change password
        else:
            current_pass = self.ui.current_pass_edit.text()
            new_pass = self.ui.new_pass_edit.text()
            con_pass = self.ui.confirm_pass_edit.text()

            # validate user input
            error_current = current_old_password_validation(current_pass, self.logged_user.password)
            error_new_pass = password_validation(new_pass)
            error_con_pass = confirm_password_validation(new_pass, con_pass)

            # Set error message 
            self.ui.current_pass_error.setText(error_current)
            self.ui.new_pass_error.setText(error_new_pass)
            self.ui.confirm_pass_error.setText(error_con_pass)

            # Update password if no error
            if error_current == "" and error_new_pass == "" and error_con_pass == "":
                query = "UPDATE user SET password = (?) WHERE email = (?)"

                value = (new_pass, self.logged_user.email)

                self.logged_user.password = new_pass

                error = self.db_connection.execute_query(query, value)[0]
            
                # Display error message
                if (error != ""):
                    MessageManager.show_message(QMessageBox.Critical, "Failed to update password", error)
                else:
                    MessageManager.show_message(QMessageBox.Information, "Password saved", "Your password is updated successfully")

                self.reset_field()



    
    
    
        