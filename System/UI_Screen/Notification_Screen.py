# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notification_Screen.ui'
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("QMainWindow#MainWindow{\n"
"    background-color:rgb(228, 235, 245);\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 211, 651))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(255,255,255)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.notification_button = QtWidgets.QPushButton(self.centralwidget)
        self.notification_button.setGeometry(QtCore.QRect(0, 210, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notification_button.setFont(font)
        self.notification_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.notification_button.setStyleSheet("QPushButton#notification_button{\n"
"    border:none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    background-color:rgb(52, 128, 235);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/notification_icon_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notification_button.setIcon(icon)
        self.notification_button.setIconSize(QtCore.QSize(35, 35))
        self.notification_button.setObjectName("notification_button")
        self.dashboard_button = QtWidgets.QPushButton(self.centralwidget)
        self.dashboard_button.setGeometry(QtCore.QRect(0, 269, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dashboard_button.setFont(font)
        self.dashboard_button.setStyleSheet("QPushButton#dashboard_button{\n"
"    color:rgb(52, 128, 235);\n"
"    border:none;\n"
"    background-color:rgb(255,255,255);\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"}\n"
"QPushButton#dashboard_button:hover{\n"
"    padding-left:40px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon/graph_icon_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboard_button.setIcon(icon1)
        self.dashboard_button.setIconSize(QtCore.QSize(35, 35))
        self.dashboard_button.setObjectName("dashboard_button")
        self.result_button = QtWidgets.QPushButton(self.centralwidget)
        self.result_button.setGeometry(QtCore.QRect(0, 328, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.result_button.setFont(font)
        self.result_button.setStyleSheet("QPushButton#result_button{\n"
"    border:none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    color:rgb(52, 128, 235);\n"
"}\n"
"QPushButton#result_button:hover{\n"
"    padding-left:40px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon/result_icon_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.result_button.setIcon(icon2)
        self.result_button.setIconSize(QtCore.QSize(35, 35))
        self.result_button.setObjectName("result_button")
        self.upload_video_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_video_button.setGeometry(QtCore.QRect(0, 387, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.upload_video_button.setFont(font)
        self.upload_video_button.setStyleSheet("QPushButton#upload_video_button{\n"
"    border:none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    color:rgb(52, 128, 235);\n"
"}\n"
"QPushButton#upload_video_button:hover{\n"
"    padding-left:40px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon/upload_icon_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_video_button.setIcon(icon3)
        self.upload_video_button.setIconSize(QtCore.QSize(35, 35))
        self.upload_video_button.setObjectName("upload_video_button")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(0, 593, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("QPushButton#logout_button{\n"
"    border:none;\n"
"    text-align: left;\n"
"    padding-left: 30px;\n"
"    color:rgb(52, 128, 235);\n"
"}\n"
"QPushButton#logout_button:hover{\n"
"    padding-left:40px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon/logout_icon_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_button.setIcon(icon4)
        self.logout_button.setIconSize(QtCore.QSize(35, 35))
        self.logout_button.setObjectName("logout_button")
        self.profile_button = QtWidgets.QPushButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(53, 95, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.profile_button.setFont(font)
        self.profile_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.profile_button.setStyleSheet("QPushButton#profile_button{\n"
"    border:none;\n"
"}")
        self.profile_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon/user_icon_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_button.setIcon(icon5)
        self.profile_button.setIconSize(QtCore.QSize(120, 120))
        self.profile_button.setObjectName("profile_button")
        self.notification_list = QtWidgets.QListWidget(self.centralwidget)
        self.notification_list.setGeometry(QtCore.QRect(260, 90, 871, 511))
        self.notification_list.setStyleSheet("QListWidget#notification_list{\n"
"    border:none;\n"
"}\n"
"QListWidget#notification_list:item:hover{\n"
"    background-color: none\n"
"}")
        self.notification_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.notification_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.notification_list.setProperty("isWrapping", False)
        self.notification_list.setWordWrap(True)
        self.notification_list.setObjectName("notification_list")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.notification_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.notification_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.notification_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.notification_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.notification_list.addItem(item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 931, 611))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(255,255,255)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(24, 13, 161, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Icon/Logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.notification_button.raise_()
        self.dashboard_button.raise_()
        self.result_button.raise_()
        self.upload_video_button.raise_()
        self.logout_button.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.notification_list.raise_()
        self.label_4.raise_()
        self.profile_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.notification_button.setText(_translate("MainWindow", "Notification"))
        self.dashboard_button.setText(_translate("MainWindow", "Dashboard"))
        self.result_button.setText(_translate("MainWindow", "Result"))
        self.upload_video_button.setText(_translate("MainWindow", "Upload Video"))
        self.logout_button.setText(_translate("MainWindow", "Logout"))
        __sortingEnabled = self.notification_list.isSortingEnabled()
        self.notification_list.setSortingEnabled(False)
        item = self.notification_list.item(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.notification_list.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.notification_list.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.notification_list.item(4)
        item.setText(_translate("MainWindow", "New Item"))
        self.notification_list.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Notification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
