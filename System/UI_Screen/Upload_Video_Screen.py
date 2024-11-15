# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Upload_Video_Screen.ui'
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
"    background-color:rgb(52, 128, 235);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon/upload_icon_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 931, 341))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(255,255,255)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 30, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.video_source_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.video_source_edit.setGeometry(QtCore.QRect(490, 100, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.video_source_edit.setFont(font)
        self.video_source_edit.setStyleSheet("border :1px outset gray;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"")
        self.video_source_edit.setText("")
        self.video_source_edit.setObjectName("video_source_edit")
        self.upload_button = QtWidgets.QPushButton(self.centralwidget)
        self.upload_button.setGeometry(QtCore.QRect(594, 300, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.upload_button.setFont(font)
        self.upload_button.setStyleSheet("QPushButton#upload_button{\n"
"    background-color:rgb(52, 128, 235);\n"
"    border:none;\n"
"    color:rgb(255,255,255);\n"
"    border-radius: 15px\n"
"}\n"
"QPushButton#upload_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgb(19, 38, 99)\n"
"}")
        self.upload_button.setAutoDefault(False)
        self.upload_button.setObjectName("upload_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 380, 931, 251))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(255,255,255)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 380, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(626, 410, 141, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.progress_table = QtWidgets.QTableWidget(self.centralwidget)
        self.progress_table.setGeometry(QtCore.QRect(260, 430, 871, 181))
        self.progress_table.setMinimumSize(QtCore.QSize(0, 0))
        self.progress_table.setStyleSheet("")
        self.progress_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.progress_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.progress_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.progress_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.progress_table.setGridStyle(QtCore.Qt.SolidLine)
        self.progress_table.setObjectName("progress_table")
        self.progress_table.setColumnCount(6)
        self.progress_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.progress_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.progress_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.progress_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.progress_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.progress_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.progress_table.setHorizontalHeaderItem(5, item)
        self.progress_table.horizontalHeader().setVisible(True)
        self.progress_table.horizontalHeader().setCascadingSectionResizes(False)
        self.progress_table.horizontalHeader().setMinimumSectionSize(47)
        self.progress_table.verticalHeader().setCascadingSectionResizes(False)
        self.video_tree_list = QtWidgets.QTreeWidget(self.centralwidget)
        self.video_tree_list.setGeometry(QtCore.QRect(260, 140, 871, 151))
        self.video_tree_list.setStyleSheet("border: 1px solid black;\n"
"")
        self.video_tree_list.setObjectName("video_tree_list")
        self.video_tree_list.headerItem().setText(0, "1")
        self.video_tree_list.header().setVisible(False)
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(1047, 98, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.remove_button.setFont(font)
        self.remove_button.setStyleSheet("QPushButton#remove_button{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#remove_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.remove_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icon/trash_icon_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_button.setIcon(icon6)
        self.remove_button.setIconSize(QtCore.QSize(25, 25))
        self.remove_button.setAutoDefault(False)
        self.remove_button.setObjectName("remove_button")
        self.browse_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_file_button.setGeometry(QtCore.QRect(961, 98, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.browse_file_button.setFont(font)
        self.browse_file_button.setStyleSheet("QPushButton#browse_file_button{\n"
"    background-color: rgb(156, 203, 240);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#browse_file_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.browse_file_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icon/file_icon_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_file_button.setIcon(icon7)
        self.browse_file_button.setIconSize(QtCore.QSize(25, 25))
        self.browse_file_button.setAutoDefault(False)
        self.browse_file_button.setObjectName("browse_file_button")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(1090, 98, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("QPushButton#reset_button{\n"
"    background-color: rgb(0, 227, 11);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#reset_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.reset_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icon/reset_icon_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon8)
        self.reset_button.setIconSize(QtCore.QSize(25, 25))
        self.reset_button.setAutoDefault(False)
        self.reset_button.setObjectName("reset_button")
        self.browse_folder_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_folder_button.setGeometry(QtCore.QRect(1004, 98, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.browse_folder_button.setFont(font)
        self.browse_folder_button.setStyleSheet("QPushButton#browse_folder_button{\n"
"    background-color: rgb(245, 206, 12);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#browse_folder_button:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}")
        self.browse_folder_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icon/folder_icon_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_folder_button.setIcon(icon9)
        self.browse_folder_button.setIconSize(QtCore.QSize(25, 25))
        self.browse_folder_button.setAutoDefault(False)
        self.browse_folder_button.setObjectName("browse_folder_button")
        self.existing_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.existing_radio.setGeometry(QtCore.QRect(260, 100, 121, 31))
        self.existing_radio.setObjectName("existing_radio")
        self.new_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.new_radio.setGeometry(QtCore.QRect(380, 100, 101, 31))
        self.new_radio.setObjectName("new_radio")
        self.source_combo = QtWidgets.QComboBox(self.centralwidget)
        self.source_combo.setGeometry(QtCore.QRect(490, 100, 281, 31))
        self.source_combo.setStyleSheet("border :1px outset gray;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"")
        self.source_combo.setObjectName("source_combo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(24, 13, 161, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Icon/Logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
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
        self.label_3.setText(_translate("MainWindow", "Upload Video"))
        self.video_source_edit.setPlaceholderText(_translate("MainWindow", "Video Source"))
        self.upload_button.setText(_translate("MainWindow", "Upload"))
        self.label_6.setText(_translate("MainWindow", "Detection Progress"))
        self.progress_table.setSortingEnabled(False)
        item = self.progress_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Upload Date"))
        item = self.progress_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Upload Time"))
        item = self.progress_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Number of Video"))
        item = self.progress_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Source"))
        item = self.progress_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Progress"))
        item = self.progress_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Action"))
        self.existing_radio.setText(_translate("MainWindow", "Existing Source"))
        self.new_radio.setText(_translate("MainWindow", "New Source"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())