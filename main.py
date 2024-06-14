import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot AI")
        self.setMinimumSize(700, 500)

        # Text Display Widget
        self.text_display_window = QTextEdit(self)
        self.text_display_window.setGeometry(10, 10, 460, 320)
        self.text_display_window.setReadOnly(True)

        # input area
        self.input_widget = QLineEdit(self)
        self.input_widget.setGeometry(10, 340, 460, 35)

        # Button Widget
        self.button = QPushButton("Send", self)
        self.button.setGeometry(480, 340, 60, 35)

        self.show()


class ChatBot:
    pass


app = QApplication(sys.argv)
chatbot_window = ChatBotWindow()
sys.exit(app.exec())
