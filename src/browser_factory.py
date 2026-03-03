from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
from PyQt6.QtCore import QUrl

from .config import BASE_DATA_DIR, DEFAULT_USER_AGENT


class BrowserFactory:
    @staticmethod
    def create_browser(
        parent=None,
        url: str = "",
        profile_name: str = "default",
        spoof_ua: bool = False,
    ) -> QWebEngineView:
        storage_path = BASE_DATA_DIR / "profiles" / profile_name / "storage"
        cache_path    = BASE_DATA_DIR / "profiles" / profile_name / "cache"

        storage_path.mkdir(parents=True, exist_ok=True)
        cache_path.mkdir(parents=True, exist_ok=True)

        profile = QWebEngineProfile(profile_name, parent)
        profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
        )
        profile.setPersistentStoragePath(str(storage_path))
        profile.setCachePath(str(cache_path))

        if spoof_ua:
            profile.setHttpUserAgent(DEFAULT_USER_AGENT)

        page = QWebEnginePage(profile, parent)
        browser = QWebEngineView()
        browser.setPage(page)
        browser.setUrl(QUrl(url))

        return browser