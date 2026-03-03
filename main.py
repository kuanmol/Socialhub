import sys

from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from PyQt6.QtCore import QUrl

class SocialHub(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Social Hub")
        self.setGeometry(100, 100, 1400, 900)

        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        # WhatsApp
        whatsapp = QWebEngineView()
        whatsapp.load(QUrl("https://web.whatsapp.com"))
        tabs.addTab(whatsapp, "WhatsApp")

        # X
        x = QWebEngineView()
        x.load(QUrl("https://x.com"))
        tabs.addTab(x, "X")

        # Reddit
        reddit = QWebEngineView()
        reddit.load(QUrl("https://www.reddit.com"))
        tabs.addTab(reddit, "Reddit")

        # Instagram
        instagram = QWebEngineView()
        instagram.load(QUrl("https://www.instagram.com"))
        tabs.addTab(instagram, "Instagram")

app = QApplication(sys.argv)
window = SocialHub()
window.show()
sys.exit(app.exec())