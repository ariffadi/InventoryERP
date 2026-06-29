import customtkinter as ctk

from ui.gui.theme import Theme
from ui.gui.controllers.setting_controller import SettingController
from ui.gui.components.notification import Notification


class SettingsView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.controller = SettingController()

        self.grid_columnconfigure(0, weight=1)

        self.create_title()

        self.create_general_setting()

        self.create_button()

        self.load_setting()

            # =====================================================

    def create_title(self):

        title = ctk.CTkLabel(

            self,

            text="Settings",

            font=Theme.FONT_TITLE

        )

        title.grid(

            row=0,

            column=0,

            sticky="w",

            padx=20,

            pady=(20, 15)

        )

            # =====================================================

    def create_general_setting(self):

        frame = ctk.CTkFrame(self)

        frame.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=20,

            pady=10

        )

        frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(

            frame,

            text="General",

            font=Theme.FONT_SUBTITLE

        ).grid(

            row=0,

            column=0,

            sticky="w",

            padx=20,

            pady=(15, 10)

        )

        self.confirm_delete = ctk.BooleanVar()

        self.enable_notification = ctk.BooleanVar()

        self.auto_refresh = ctk.BooleanVar()

        self.auto_open_excel = ctk.BooleanVar()

        self.confirm_check = ctk.CTkCheckBox(

            frame,

            text="Confirm Delete",

            variable=self.confirm_delete

        )

        self.confirm_check.grid(

            row=1,

            column=0,

            sticky="w",

            padx=30,

            pady=5

        )

        self.notification_check = ctk.CTkCheckBox(

            frame,

            text="Enable Notification",

            variable=self.enable_notification

        )

        self.notification_check.grid(

            row=2,

            column=0,

            sticky="w",

            padx=30,

            pady=5

        )

        self.refresh_check = ctk.CTkCheckBox(

            frame,

            text="Auto Refresh Dashboard",

            variable=self.auto_refresh

        )

        self.refresh_check.grid(

            row=3,

            column=0,

            sticky="w",

            padx=30,

            pady=5

        )

        self.excel_check = ctk.CTkCheckBox(

            frame,

            text="Auto Open Excel",

            variable=self.auto_open_excel

        )

        self.excel_check.grid(

            row=4,

            column=0,

            sticky="w",

            padx=30,

            pady=(5,15)

        )

        ctk.CTkLabel(

            frame,

            text="Appearance"

        ).grid(

            row=5,

            column=0,

            sticky="w",

            padx=30,

            pady=(10,5)

        )

        self.mode = ctk.CTkComboBox(

            frame,

            values=[

                "System",

                "Light",

                "Dark"

            ]

        )

        self.mode.grid(

            row=6,

            column=0,

            sticky="w",

            padx=30,

            pady=(0,20)

        )
            # =====================================================

    def create_button(self):

        button = ctk.CTkButton(

            self,

            text="Simpan Pengaturan",

            command=self.save_setting

        )

        button.grid(

            row=2,

            column=0,

            pady=20

        )
            # =====================================================

    def load_setting(self):

        data = self.controller.load()

        self.confirm_delete.set(

            data.get(

                "confirm_delete",

                True

            )

        )

        self.enable_notification.set(

            data.get(

                "enable_notification",

                True

            )

        )

        self.auto_refresh.set(

            data.get(

                "auto_refresh_dashboard",

                True

            )

        )

        self.auto_open_excel.set(

            data.get(

                "auto_open_excel",

                False

            )

        )

        self.mode.set(

            data.get(

                "appearance_mode",

                "System"

            )

        )
            # =====================================================

    def save_setting(self):

        data = {

            "confirm_delete":
                self.confirm_delete.get(),

            "enable_notification":
                self.enable_notification.get(),

            "auto_refresh_dashboard":
                self.auto_refresh.get(),

            "auto_open_excel":
                self.auto_open_excel.get(),

            "appearance_mode":
                self.mode.get()

        }

        self.controller.save(data)

        ctk.set_appearance_mode(

            self.mode.get()

        )

        Notification.success(

            self,

            "Pengaturan berhasil disimpan."

        )
        