import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit
from backend import get_data
import threading


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
        self.button.clicked.connect(self.send_response)

        self.show()

    def send_response(self):
        user_prompt = self.input_widget.text()
        self.text_display_window.append(f"<p style='color: white'>You: {user_prompt}</p>")
        self.input_widget.clear()


app = QApplication(sys.argv)
chatbot_window = ChatBotWindow()
sys.exit(app.exec())
