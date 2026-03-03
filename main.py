import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QToolBar
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QMenu


class SocialHub(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Social Hub")
        self.setGeometry(100, 100, 1400, 900)

        # 1️⃣Create tabs first
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.tabs.removeTab)
        self.setCentralWidget(self.tabs)

        # 2️⃣ Create toolbar
        toolbar = QToolBar("Navigation")
        self.addToolBar(toolbar)

        # 3️⃣ Add toolbar buttons

        new_tab_action = QAction("➕ New Tab", self)
        new_tab_menu = QMenu()
        new_tab_menu.addAction("X", lambda: self.add_tab("https://x.com", "X"))
        new_tab_menu.addAction("WhatsApp", lambda: self.add_tab("https://web.whatsapp.com", "WhatsApp"))
        new_tab_menu.addAction("Instagram", lambda: self.add_tab("https://instagram.com", "Instagram"))
        new_tab_menu.addAction("Reddit", lambda: self.add_tab("https://reddit.com", "Reddit"))
        new_tab_action.setMenu(new_tab_menu)
        toolbar.addAction(new_tab_action)

        # Back, Forward, Reload, Home
        back_action = QAction("← Back", self)
        back_action.triggered.connect(self.go_back)
        toolbar.addAction(back_action)

        forward_action = QAction("Forward →", self)
        forward_action.triggered.connect(self.go_forward)
        toolbar.addAction(forward_action)

        reload_action = QAction("⟳ Reload", self)
        reload_action.triggered.connect(self.reload_tab)
        toolbar.addAction(reload_action)

        home_action = QAction("🏠 Home", self)
        home_action.triggered.connect(self.go_home)
        toolbar.addAction(home_action)

        # 4️⃣ Add initial social media tabs
        self.add_tab("https://x.com", "X")
        self.add_tab("https://web.whatsapp.com", "WhatsApp")
        self.add_tab("https://instagram.com", "Instagram")
        self.add_tab("https://reddit.com", "Reddit")

    def create_browser(self, url):
        """Create browser with custom profile and Chrome UA for WhatsApp"""
        profile = QWebEngineProfile("MyProfile", self)
        profile.setPersistentStoragePath("/home/anmol/REPOS-prac/Social_hub/data/browser_data")
        profile.setCachePath("/home/anmol/REPOS-prac/Social_hub/data/browser_cache")

        page = QWebEnginePage(profile, self)
        browser = QWebEngineView()
        browser.setPage(page)

        # Spoof Chrome UA for WhatsApp
        browser.page().profile().setHttpUserAgent(
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        )

        browser.setUrl(QUrl(url))
        return browser

    def add_tab(self, url, name):
        browser = self.create_browser(url)
        self.tabs.addTab(browser, name)

    # Toolbar actions
    def current_browser(self):
        return self.tabs.currentWidget()

    def go_back(self):
        if self.current_browser():
            self.current_browser().back()

    def go_forward(self):
        if self.current_browser():
            self.current_browser().forward()

    def reload_tab(self):
        if self.current_browser():
            self.current_browser().reload()

    def go_home(self):
        if self.current_browser():
            # Go to the tab’s first URL
            index = self.tabs.currentIndex()
            home_urls = ["https://x.com", "https://web.whatsapp.com", "https://instagram.com", "https://reddit.com"]
            if index < len(home_urls):
                self.current_browser().setUrl(QUrl(home_urls[index]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SocialHub()
    window.show()
    sys.exit(app.exec())
