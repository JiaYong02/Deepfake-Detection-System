# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Change_Password_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 60, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 0, 611, 651))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255,255,255)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(760, 360, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_button.setFont(font)
        self.confirm_button.setStyleSheet("QPushButton#confirm_button{\n"
"    background-color:rgb(52, 128, 235);\n"
"    border:none;\n"
"    color:rgb(255,255,255);\n"
"    border-radius: 15px\n"
"}\n"
"QPushButton#confirm_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgb(19, 38, 99)\n"
"}")
        self.confirm_button.setAutoDefault(False)
        self.confirm_button.setObjectName("confirm_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(640, 170, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(640, 190, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.password_edit.setFont(font)
        self.password_edit.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);")
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setPlaceholderText("")
        self.password_edit.setObjectName("password_edit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(640, 256, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.confirm_password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.confirm_password_edit.setGeometry(QtCore.QRect(640, 276, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.confirm_password_edit.setFont(font)
        self.confirm_password_edit.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);")
        self.confirm_password_edit.setText("")
        self.confirm_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_edit.setPlaceholderText("")
        self.confirm_password_edit.setObjectName("confirm_password_edit")
        self.back_login_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_login_button.setGeometry(QtCore.QRect(787, 410, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.back_login_button.setFont(font)
        self.back_login_button.setStyleSheet("QPushButton#back_login_button{\n"
"    border:none;\n"
"    color: rgb(29, 98, 168)\n"
"}\n"
"QPushButton#back_login_button:pressed{\n"
"    color:rgb(19, 38, 99)\n"
"}")
        self.back_login_button.setObjectName("back_login_button")
        self.error_password = QtWidgets.QLabel(self.centralwidget)
        self.error_password.setGeometry(QtCore.QRect(640, 222, 421, 16))
        self.error_password.setStyleSheet("color:rgb(255,0,0)")
        self.error_password.setText("")
        self.error_password.setObjectName("error_password")
        self.error_con_password = QtWidgets.QLabel(self.centralwidget)
        self.error_con_password.setGeometry(QtCore.QRect(640, 309, 421, 16))
        self.error_con_password.setStyleSheet("color:rgb(255,0,0)")
        self.error_con_password.setText("")
        self.error_con_password.setObjectName("error_con_password")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 250, 291, 111))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Icon/Logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 571, 661))
        self.label_8.setStyleSheet("")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Icon/background 2.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label.raise_()
        self.label_2.raise_()
        self.confirm_button.raise_()
        self.label_3.raise_()
        self.password_edit.raise_()
        self.label_7.raise_()
        self.confirm_password_edit.raise_()
        self.back_login_button.raise_()
        self.error_password.raise_()
        self.error_con_password.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Change Your Password"))
        self.confirm_button.setText(_translate("MainWindow", "Confirm"))
        self.label_3.setText(_translate("MainWindow", "New Password:"))
        self.label_7.setText(_translate("MainWindow", "Confirm Password:"))
        self.back_login_button.setText(_translate("MainWindow", "Back to login page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())