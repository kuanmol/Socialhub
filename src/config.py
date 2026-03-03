from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

BASE_DATA_DIR = PROJECT_ROOT / "data"

SOCIAL_SITES = [
    {
        "name": "X",
        "url": "https://x.com",
        "profile_name": "x_profile",
        "icon": "𝕏",
    },
    {
        "name": "WhatsApp",
        "url": "https://web.whatsapp.com",
        "profile_name": "whatsapp_profile",
        "icon": "💬",
        "spoof_chrome_ua": True,
    },
    {
        "name": "Instagram",
        "url": "https://www.instagram.com",
        "profile_name": "instagram_profile",
        "icon": "📷",
    },
    {
        "name": "Reddit",
        "url": "https://www.reddit.com",
        "profile_name": "reddit_profile",
        "icon": "⛺",
    },
]

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)