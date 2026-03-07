# design tokens and helpers for CTW application

# color tokens
BACKGROUND_PRIMARY = "#0D0F14"
BACKGROUND_SECONDARY = "#181A20"
SURFACE = "#1E2128"
SURFACE_HOVER = "#242830"
SURFACE_ELEVATED = "#2A2E37"

TEXT_PRIMARY = "#E1E3E8"
TEXT_SECONDARY = "#A0A4B0"
TEXT_MUTED = "#6C707A"

ACCENT_PRIMARY = "#00A8FF"
ACCENT_HOVER = "#0091E6"

SUCCESS = "#4CAF50"
WARNING = "#FFC107"
ERROR = "#F44336"
INFO = "#2196F3"

BORDER_SUBTLE = "#30343D"
BORDER_DEFAULT = "#3C4049"

BADGE_API = "#3A86FF"
BADGE_SCRAPER = "#8338EC"
BADGE_CACHE = "#FFBE0B"
BADGE_MANUAL = "#FF006E"

# radius tokens (px)
RADIUS_SMALL = 2
RADIUS_MEDIUM = 6
RADIUS_LARGE = 12

# spacing tokens (px)
SPACING_XS = 4
SPACING_SM = 8
SPACING_MD = 12
SPACING_LG = 16
SPACING_XL = 20
SPACING_XXL = 24

# elevation shadows (Qt uses QGraphicsDropShadowEffect so these are helpers)
ELEVATION_1 = "0 1px 3px rgba(0,0,0,0.3)"
ELEVATION_2 = "0 2px 8px rgba(0,0,0,0.4)"
ELEVATION_3 = "0 4px 12px rgba(0,0,0,0.5)"


def get_stylesheet():
    """Return the global QSS stylesheet string using the defined tokens."""
    return f"""
        QWidget {{
            background-color: {BACKGROUND_PRIMARY};
            color: {TEXT_PRIMARY};
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }}

        QLineEdit, QPlainTextEdit, QTextEdit, QSpinBox, QComboBox {{
            background-color: {SURFACE};
            color: {TEXT_PRIMARY};
            border: 1px solid {BORDER_DEFAULT};
            border-radius: {RADIUS_SMALL}px;
            padding: 4px;
        }}

        QPushButton {{
            background-color: {SURFACE};
            color: {TEXT_PRIMARY};
            border: none;
            border-radius: {RADIUS_MEDIUM}px;
            padding: 6px 14px;
        }}
        QPushButton:hover {{ background-color: {SURFACE_HOVER}; }}
        QPushButton:pressed {{ background-color: {BORDER_DEFAULT}; }}

        QScrollBar:vertical {{
            background: {BACKGROUND_PRIMARY};
            width: 8px;
        }}
        QScrollBar::handle:vertical {{
            background: {BORDER_DEFAULT};
            border-radius: 4px;
        }}

        .accent {{ color: {ACCENT_PRIMARY}; }}
    """