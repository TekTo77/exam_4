"""Оформление окна импорта."""
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

APP_TITLE = "Чудо Обувь — система оформления заказов"

FONT_FAMILY = "Calibri"

FONT_SIZES = {
    "small": 9,
    "body": 10,
    "emphasis": 11,
    "card_title": 12,
    "login_title": 15,
    "title": 18,
    "brand": 20,
}

WINDOW = {
    "size": (1120, 760),
    "minimum": (900, 620),
    "import_size": (940, 700),
    "import_minimum": (820, 560),
}

SPACING = {
    "page": 24,
    "card_gap": 10,
    "header_top": 18,
    "header_bottom": 12,
    "login_x": 42,
    "login_y": 32,
    "button": (12, 7),
    "table_row": 36,
}

COLORS = {
    "background": "#F3F6FA",
    "surface": "#FFFFFF",
    "secondary": "#E6EDF8",
    "secondary_hover": "#D3DFF1",
    "accent": "#4B6FA8",
    "accent_dark": "#355481",
    "on_accent": "#FFFFFF",
    "border": "#D8E0EC",
    "danger": "#C65757",
    "danger_dark": "#A83F3F",
    "low_stock": "#FF8080",
    "low_stock_background": "#FFF0F0",
    "text": "#243247",
    "muted": "#67758A",
}

WINDOW_ICON_PATH = None

IMAGE_FIT = "contain"
