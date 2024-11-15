import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from enums import Pages
from Controller import (
    Login_Controller, Register_Controller, 
    Forget_Password_Controller, Verification_Controller, Change_Password_Controller,
    Dashboard_Controller, Notification_Controller, Result_Controller, Upload_Video_Controller,
    Profile_Controller, Result_Details_Controller

)
from Utility.DatabaseConnection import DatabaseConnection



def add_pages(router, db_connection):
    login_page = Login_Controller.LoginController(router, db_connection)
    router.addWidget(login_page)

    register_page = Register_Controller.RegisterController(router, db_connection)
    router.addWidget(register_page)

    forget_password_page = Forget_Password_Controller.ForgetPasswordController(router, db_connection)
    router.addWidget(forget_password_page)

    verification_page = Verification_Controller.VerificationController(router, db_connection, forget_password_page)
    router.addWidget(verification_page)

    change_password_page = Change_Password_Controller.ChangePasswordController(router, db_connection, forget_password_page)
    router.addWidget(change_password_page)

    upload_video_page = Upload_Video_Controller.UploadVideoController(router, db_connection, login_page)
    router.addWidget(upload_video_page)

    dashboard_page = Dashboard_Controller.DashboardController(router, db_connection, login_page, upload_video_page)
    router.addWidget(dashboard_page)

    result_page = Result_Controller.ResultController(router, db_connection, login_page, upload_video_page)
    router.addWidget(result_page)

    notification_page = Notification_Controller.NotificationController(router, db_connection, login_page, upload_video_page)
    router.addWidget(notification_page)

    profile_page = Profile_Controller.ProfileController(router, db_connection, login_page)
    router.addWidget(profile_page)

    result_details_page = Result_Details_Controller.ResultDetailsController(router, db_connection, result_page)
    router.addWidget(result_details_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    router = QtWidgets.QStackedWidget()
    db_connection = DatabaseConnection()
    add_pages(router, db_connection)
    
    router.setGeometry(100, 100, 1183, 653)
    router.setCurrentIndex(Pages.LOGIN.value)
    router.setWindowTitle("Realip")
    router.setFixedSize(1183, 653)
    router.show()
    sys.exit(app.exec_())
