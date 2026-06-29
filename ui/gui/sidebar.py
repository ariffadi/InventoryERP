import customtkinter as ctk

from ui.gui.theme import Theme


class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        navigate
    ):

        super().__init__(
            master,
            width=Theme.SIDEBAR_WIDTH,
            corner_radius=0
        )

        self.navigate = navigate

        self.grid_propagate(False)

        self.create_logo()

        self.create_menu()

        self.create_footer()

    # ==================================================

    def create_logo(self):

        title = ctk.CTkLabel(
            self,
            text="📦 Inventory ERP",
            font=Theme.FONT_TITLE
        )

        title.pack(
            pady=(30, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Management System",
            font=Theme.FONT_SMALL
        )

        subtitle.pack(
            pady=(0, 25)
        )

    # ==================================================

    def create_menu(self):

        menus = [

            ("🏠 Dashboard", "dashboard"),

            ("📦 Products", "products"),

            ("💳 Transactions", "transactions"),

            ("📄 Reports", "reports"),

            ("⚙ Settings", "settings")

        ]

        for text, page in menus:

            button = ctk.CTkButton(

                self,

                text=text,

                command=lambda p=page: self.navigate(p)

            )

            button.pack(

                fill="x",

                padx=15,

                pady=5

            )

    # ==================================================

    def create_footer(self):

        ctk.CTkLabel(
            self,
            text=""
        ).pack(
            expand=True
        )

        exit_button = ctk.CTkButton(

            self,

            text="🚪 Exit",

            fg_color="#C62828",

            hover_color="#B71C1C",

            command=self.master.destroy

        )

        exit_button.pack(

            fill="x",

            padx=15,

            pady=20

        )