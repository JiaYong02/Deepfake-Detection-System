from PyQt5.QtWidgets import QMainWindow
from UI_Screen.Verification_Screen import Ui_MainWindow
from enums import Pages
from Model.User import User
import smtplib
import hashlib
import random
import time

class VerificationController(QMainWindow):
    def __init__(self, router, db_connection, forget_password_controller):
        super(VerificationController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.router = router
        self.db_connection = db_connection
        self.forget_password_controller = forget_password_controller
        self.user_email = None

        # Receive email from forget_password_controller
        self.forget_password_controller.email_passed.connect(self.receive_email)
        

        self.ui.resend_otp_button.clicked.connect(self.request_verification_code)
        self.ui.back_button.clicked.connect(self.back)
        self.ui.confirm_button.clicked.connect(self.validate_otp)

     # Access the email address passed from ForgetPasswordController
    def receive_email(self, email):
        self.user_email = email
        # Generate and send otp
        self.request_verification_code()

    def reset_field(self):
        self.ui.otp_edit.setText("")
        self.ui.error_otp.setText("")

    # Navigate to change password page
    def navigate_change_password(self):
        self.router.setCurrentIndex(Pages.CHANGE_PASSWORD.value)
        self.reset_field()
    
    # Go back to forget password page
    def back(self):
        self.router.setCurrentIndex(Pages.FORGET_PASSWORD.value)

    # validate entered otp 
    def validate_otp(self):
        # Get user input otp and encrypt it
        user_otp = self.hash_otp(self.ui.otp_edit.text())

        # Query to check if otp is valid
        query = f"""
                    SELECT otp, expiry_time FROM otp_records 
                    WHERE email = '{self.user_email}' AND 
                    expiry_time > {int(time.time())}
                    ORDER BY expiry_time DESC
                """
        result = self.db_connection.execute_query(query)[1].fetchall()

        if (not result):
            self.ui.error_otp.setText("Invalid OTP. Please try again")
        # Match otp of the latest OTP request
        elif (user_otp != result[0][0]):
            self.ui.error_otp.setText("Invalid OTP. Please try again")
        # Check the expiry time of the latest OTP requested 
        elif (result[0][1] < time.time()):
            self.ui.error_otp.setText("You entered an expired OTP. Please try again")
        else:
            self.navigate_change_password()
        

    # Send email with OTP to user
    def request_verification_code(self):
        # Generate otp
        otp = str(random.randint(100000, 999999))
        
        # Encrypt and save otp to database
        self.save_otp(otp)

        sender_email = "jiayong711@gmail.com"
        sender_password = "vowpgzxisbpnyidg"  
        smtp_server = "smtp.gmail.com"
        user_email = self.user_email
        port = 587  

        message = f"Subject: Password Change OTP\n\nYour OTP for password change is: {otp}. This code will expire in 5 minutes"

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, user_email, message)

            
    # Save otp in database
    def save_otp(self,otp):
        # encrypt opt
        otp_hash = self.hash_otp(otp)

        # otp expiry time = current time + 5 minutes
        email = self.user_email
        expiry_time = int(time.time()) + 300

        # Save to database
        query = f"INSERT INTO otp_records (email, otp, expiry_time) VALUES ('{email}','{otp_hash}','{expiry_time}')"
        self.db_connection.execute_query(query)
        

    # perform hashing to otp
    def hash_otp(self, otp):
        otp = otp.encode('utf-8')

        # Initializing the sha256() method
        sha256 = hashlib.sha256()

        # Passing the byte stream as an argument
        sha256.update(otp)

        return sha256.hexdigest()