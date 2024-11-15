# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result_Screen.ui'
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
"    color:rgb(52, 128, 235);\n"
"}\n"
"QPushButton#notification_button:hover{\n"
"    padding-left:40px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/notification_icon_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
"    background-color:rgb(52, 128, 235);\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon/result_icon_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.result_table = QtWidgets.QTableWidget(self.centralwidget)
        self.result_table.setGeometry(QtCore.QRect(260, 150, 871, 451))
        self.result_table.setStyleSheet("text-align: center;")
        self.result_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(7)
        self.result_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(6, item)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(650, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:rgb(140, 137, 137)")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 102, 16, 31))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.source_combo = QtWidgets.QComboBox(self.centralwidget)
        self.source_combo.setGeometry(QtCore.QRect(710, 100, 151, 31))
        self.source_combo.setObjectName("source_combo")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(470, 100, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:rgb(140, 137, 137)")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.from_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.from_date_edit.setGeometry(QtCore.QRect(310, 100, 131, 31))
        self.from_date_edit.setCalendarPopup(True)
        self.from_date_edit.setObjectName("from_date_edit")
        self.to_date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.to_date_edit.setGeometry(QtCore.QRect(500, 100, 131, 31))
        self.to_date_edit.setCalendarPopup(True)
        self.to_date_edit.setObjectName("to_date_edit")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(260, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:rgb(140, 137, 137)")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(870, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(140, 137, 137)")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.result_combo = QtWidgets.QComboBox(self.centralwidget)
        self.result_combo.setGeometry(QtCore.QRect(930, 100, 151, 31))
        self.result_combo.setObjectName("result_combo")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(1090, 94, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("QPushButton#search_button{\n"
"    background-color: rgb(52, 128, 235);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#search_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.search_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icon/search_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon6)
        self.search_button.setIconSize(QtCore.QSize(29, 29))
        self.search_button.setAutoDefault(False)
        self.search_button.setObjectName("search_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(24, 13, 161, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Icon/Logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2.raise_()
        self.label.raise_()
        self.notification_button.raise_()
        self.dashboard_button.raise_()
        self.result_button.raise_()
        self.upload_video_button.raise_()
        self.logout_button.raise_()
        self.profile_button.raise_()
        self.label_3.raise_()
        self.result_table.raise_()
        self.label_19.raise_()
        self.line.raise_()
        self.source_combo.raise_()
        self.label_18.raise_()
        self.from_date_edit.raise_()
        self.to_date_edit.raise_()
        self.label_17.raise_()
        self.label_20.raise_()
        self.result_combo.raise_()
        self.search_button.raise_()
        self.label_4.raise_()
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
        self.label_3.setText(_translate("MainWindow", "Detection Result"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Upload Date"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Upload Time"))
        item = self.result_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Completion Time"))
        item = self.result_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Source"))
        item = self.result_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total Video"))
        item = self.result_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total Deepfake"))
        item = self.result_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Action"))
        self.label_19.setText(_translate("MainWindow", "Source:"))
        self.label_18.setText(_translate("MainWindow", "To:"))
        self.label_17.setText(_translate("MainWindow", "From:"))
        self.label_20.setText(_translate("MainWindow", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
