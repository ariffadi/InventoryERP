import customtkinter as ctk


class Theme:

    APP_TITLE = "Inventory ERP System"

    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 850

    SIDEBAR_WIDTH = 240

    CARD_RADIUS = 10
    DIALOG_RADIUS = 15

    # =====================================================
    # Fonts
    # =====================================================

    FONT_TITLE = ("Segoe UI", 24, "bold")
    FONT_SUBTITLE = ("Segoe UI", 18, "bold")
    FONT_NORMAL = ("Segoe UI", 14)
    FONT_SMALL = ("Segoe UI", 12)

    FONT_DIALOG_TITLE = ("Segoe UI", 20, "bold")
    FONT_DIALOG_MESSAGE = ("Segoe UI", 14)

    # =====================================================
    # Colors
    # =====================================================

    COLOR_PRIMARY = "#2563EB"

    COLOR_SUCCESS = "#16A34A"

    COLOR_WARNING = "#F59E0B"

    COLOR_DANGER = "#DC2626"

    COLOR_INFO = "#0EA5E9"

    COLOR_WHITE = "#FFFFFF"

    COLOR_BORDER = "#D1D5DB"

    COLOR_DIALOG = ("#F9FAFB", "#2B2B2B")

    # =====================================================
    # Dialog Size
    # =====================================================

    DIALOG_WIDTH = 420

    DIALOG_HEIGHT = 230

    DIALOG_PADDING = 20

    BUTTON_WIDTH = 120

    # =====================================================

    @staticmethod
    def setup():

        ctk.set_appearance_mode("System")

        ctk.set_default_color_theme("blue")