import customtkinter as ctk

from ui.gui.theme import Theme


class DashboardCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title,
        value="0",
        icon="📦",
        width=220,
        height=130
    ):

        super().__init__(
            master,
            width=width,
            height=height,
            corner_radius=12
        )

        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)

        self.icon_label = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 26)
        )

        self.icon_label.grid(
            row=0,
            column=0,
            pady=(15, 2)
        )

        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=Theme.FONT_NORMAL
        )

        self.title_label.grid(
            row=1,
            column=0,
            pady=(0, 6)
        )

        self.value_label = ctk.CTkLabel(
            self,
            text=str(value),
            font=("Segoe UI", 22, "bold")
        )

        self.value_label.grid(
            row=2,
            column=0,
            pady=(0, 15)
        )

    # =====================================================

    def set_value(self, value):

        self.value_label.configure(
            text=str(value)
        )

    # =====================================================

    def set_icon(self, icon):

        self.icon_label.configure(
            text=icon
        )

    # =====================================================

    def get_value(self):

        return self.value_label.cget("text")