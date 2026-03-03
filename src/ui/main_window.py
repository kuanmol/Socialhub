from PyQt6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QToolBar,
    QMenu,
)
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

from src.config import SOCIAL_SITES
from src.browser_factory import BrowserFactory


class SocialHub(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Social Hub")
        self.resize(1400, 900)

        self._setup_ui()
        self._add_initial_tabs()

    def _setup_ui(self):
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.tabs.removeTab)
        self.setCentralWidget(self.tabs)

        toolbar = QToolBar("Main Navigation")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # New Tab Menu
        new_tab_action = QAction("➕ New Tab", self)
        new_tab_menu = QMenu(self)

        for site in SOCIAL_SITES:
            act = new_tab_menu.addAction(
                f"{site['icon']} {site['name']}",
                lambda checked=False, s=site: self.add_new_tab(
                    url=s["url"],
                    title=s["name"],
                    profile_name=s["profile_name"],
                    spoof_ua=s.get("spoof_chrome_ua", False)
                )
            )

        new_tab_action.setMenu(new_tab_menu)
        toolbar.addAction(new_tab_action)

        # Navigation controls
        actions = [
            ("← Back", self.go_back),
            ("Forward →", self.go_forward),
            ("⟳ Reload", self.reload_current),
            ("🏠 Home", self.go_home),
        ]
        for text, slot in actions:
            action = QAction(text, self)
            action.triggered.connect(slot)
            toolbar.addAction(action)

    def _add_initial_tabs(self):
        for site in SOCIAL_SITES:
            self.add_new_tab(
                url=site["url"],
                title=site["name"],
                profile_name=site["profile_name"],
                spoof_ua=site.get("spoof_chrome_ua", False)
            )

    def add_new_tab(self, url: str, title: str, profile_name: str, spoof_ua: bool = False):
        browser = BrowserFactory.create_browser(
            parent=self,
            url=url,
            profile_name=profile_name,
            spoof_ua=spoof_ua
        )
        index = self.tabs.addTab(browser, title)
        self.tabs.setCurrentIndex(index)

    def current_browser(self) -> QWebEngineView | None:
        widget = self.tabs.currentWidget()
        return widget if isinstance(widget, QWebEngineView) else None

    def go_back(self):
        if br := self.current_browser():
            br.back()

    def go_forward(self):
        if br := self.current_browser():
            br.forward()

    def reload_current(self):
        if br := self.current_browser():
            br.reload()

    def go_home(self):
        if br := self.current_browser():
            idx = self.tabs.currentIndex()
            if 0 <= idx < len(SOCIAL_SITES):
                br.setUrl(QUrl(SOCIAL_SITES[idx]["url"]))
