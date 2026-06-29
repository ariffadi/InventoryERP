import customtkinter as ctk

from ui.gui.components.dialogs.base_dialog import BaseDialog


class ConfirmDialog(BaseDialog):

    def __init__(
        self,
        master,
        message,
        title="Konfirmasi"
    ):

        super().__init__(
            master,
            title=title,
            width=450,
            height=240
        )

        self.result = False

        # ==============================================

        icon = ctk.CTkLabel(
            self.container,
            text="⚠️",
            font=("Segoe UI Emoji", 42)
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
            wraplength=360,
            justify="center"
        )

        message_label.pack(
            pady=(15, 25)
        )

        button_frame = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )

        button_frame.pack()

        ctk.CTkButton(
            button_frame,
            text="Batal",
            width=120,
            command=self.cancel
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            button_frame,
            text="Ya",
            width=120,
            fg_color="#D32F2F",
            hover_color="#B71C1C",
            command=self.confirm
        ).pack(
            side="left",
            padx=10
        )

    # ==============================================

    def confirm(self):

        self.result = True

        self.close()

    # ==============================================

    def cancel(self):

        self.result = False

        self.close()