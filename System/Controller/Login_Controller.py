from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from UI_Screen.Login_Screen import Ui_MainWindow
from enums import Pages
from Model.User import User

class LoginController(QMainWindow):
    user_passed = pyqtSignal(User)
    def __init__(self, router, db_connection):
        super(LoginController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router
        self.db_connection = db_connection
        
        # Connect the button to function 
        self.ui.register_button.clicked.connect(self.navigate_register)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.forget_password_button.clicked.connect(self.navigate_forget_password)

    def navigate_register(self):
        self.router.setCurrentIndex(Pages.REGISTER.value)
        self.reset_field()

    def navigate_dashboard(self):
        self.router.setCurrentIndex(Pages.DASHBOARD.value)
        self.reset_field()
    
    def navigate_forget_password(self):
        self.router.setCurrentIndex(Pages.FORGET_PASSWORD.value)
        self.reset_field()


    def reset_field(self):
        self.ui.error_login.setText("")
        self.ui.email_edit.setText("")
        self.ui.password_edit.setText("")

    # User login
    def login(self):
        email = self.ui.email_edit.text()
        password = self.ui.password_edit.text()

        # check if email and password field is empty
        if (not email or not password):
            self.ui.error_login.setText("*Please enter your email address and password.")
        else:   
            # Create user for login
            user = User(email, password, "", self.db_connection)
            if (user.login()):
                # Send the logged user information for other page
                self.user_passed.emit(user)
                self.navigate_dashboard()
            else:
                self.ui.error_login.setText("*The email and password you entered did not match with our record. Please double-check and try again.")
        
        