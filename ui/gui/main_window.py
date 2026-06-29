import customtkinter as ctk

from ui.gui.theme import Theme
from ui.gui.sidebar import Sidebar

from ui.gui.views.dashboard_view import DashboardView
from ui.gui.views.product_view import ProductView
from ui.gui.views.transaction_view import TransactionView
from ui.gui.views.report_view import ReportView
from ui.gui.views.settings_view import SettingsView


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(Theme.APP_TITLE)

        self.geometry(
            f"{Theme.WINDOW_WIDTH}x{Theme.WINDOW_HEIGHT}"
        )

        self.minsize(1300, 750)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.pages = {}

        self.create_sidebar()

        self.create_container()

        self.create_statusbar()

        self.create_pages()

        self.show_page("dashboard")

    # ==================================================

    def create_sidebar(self):

        self.sidebar = Sidebar(
            self,
            self.show_page
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

    # ==================================================

    def create_container(self):

        self.container = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.container.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.container.grid_rowconfigure(
            0,
            weight=1
        )

        self.container.grid_columnconfigure(
            0,
            weight=1
        )

    # ==================================================

    def create_pages(self):

        self.pages["dashboard"] = DashboardView(
            self.container
        )

        self.pages["products"] = ProductView(
            self.container
        )

        self.pages["transactions"] = TransactionView(
            self.container
        )

        self.pages["reports"] = ReportView(
            self.container
        )

        self.pages["settings"] = SettingsView(
            self.container
        )

        for page in self.pages.values():

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

    # ==================================================

    def show_page(self, page_name):

        page = self.pages.get(page_name)

        if page:

            page.tkraise()

            self.statusbar.configure(
                text=f"Ready | {page_name.title()}"
            )

    # ==================================================

    def create_statusbar(self):

        self.statusbar = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w",
            height=30
        )

        self.statusbar.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="ew"
        )