import customtkinter as ctk

from ui.gui.components.dialogs.base_dialog import BaseDialog


class ErrorDialog(BaseDialog):

    def __init__(
        self,
        master,
        message,
        title="Error"
    ):

        super().__init__(
            master,
            title=title,
            width=420,
            height=230
        )

        icon = ctk.CTkLabel(
            self.container,
            text="❌",
            font=("Segoe UI Emoji", 40)
        )

        icon.pack(
            pady=(0, 10)
        )

        title_label = ctk.CTkLabel(
            self.container,
            text=title,
            font=("Segoe UI", 20, "bold")
        )

        title_label.pack()

        message_label = ctk.CTkLabel(
            self.container,
            text=message,
            wraplength=340,
            justify="center"
        )

        message_label.pack(
            pady=(15, 20)
        )

        ctk.CTkButton(
            self.container,
            text="Tutup",
            width=120,
            command=self.close
        ).pack()