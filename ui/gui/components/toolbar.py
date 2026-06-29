import customtkinter as ctk

from ui.gui.theme import Theme


class Toolbar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title,
        add_command=None,
        refresh_command=None
    ):

        super().__init__(
            master,
            corner_radius=10
        )

        self.pack_propagate(False)

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=Theme.FONT_TITLE
        )

        self.title.pack(
            side="left",
            padx=20,
            pady=15
        )

        self.refresh_button = ctk.CTkButton(
            self,
            text="🔄 Refresh",
            width=120,
            command=refresh_command
        )

        self.refresh_button.pack(
            side="right",
            padx=10
        )

        self.add_button = ctk.CTkButton(
            self,
            text="+ Tambah",
            width=120,
            command=add_command
        )

        self.add_button.pack(
            side="right",
            padx=10
        )