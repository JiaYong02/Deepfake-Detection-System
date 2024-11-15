from PyQt5.QtWidgets import QMessageBox

class MessageManager():
    def show_message(icon, title, message):
        message_box = QMessageBox()
        message_box.setIcon(icon)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.exec_()

    def message_with_action(icon, title, message, info = ""):
        message_box = QMessageBox()
        message_box.setIcon(icon)
        message_box.setWindowTitle(title)
        message_box.setText(message)
        message_box.setInformativeText(info)
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Get user choice
        choice = message_box.exec_()

        if choice == QMessageBox.Yes:
            return True
        
        return False