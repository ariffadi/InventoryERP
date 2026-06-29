import customtkinter as ctk

from ui.gui.components.dashboard_card import DashboardCard
from ui.gui.controllers.dashboard_controller import DashboardController
from ui.gui.components.data_table import DataTable


class DashboardView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.controller = DashboardController()

        self.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.create_title()

        self.create_summary_cards()

        self.create_inventory_cards()

        self.create_critical_table()

        self.create_top_selling_table()

        self.load_dashboard()

    # =====================================================

    def create_title(self):

        title = ctk.CTkLabel(
            self,
            text="Inventory Dashboard",
            font=("Segoe UI", 24, "bold")
        )

        title.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(20, 15)
        )

    # =====================================================

    def create_summary_cards(self):

        self.card_product = DashboardCard(
            self,
            "Total Produk"
        )

        self.card_product.grid(
            row=1,
            column=0,
            padx=15,
            pady=10,
            sticky="nsew"
        )

        self.card_in = DashboardCard(
            self,
            "Barang Masuk"
        )

        self.card_in.grid(
            row=1,
            column=1,
            padx=15,
            pady=10,
            sticky="nsew"
        )

        self.card_out = DashboardCard(
            self,
            "Barang Keluar"
        )

        self.card_out.grid(
            row=1,
            column=2,
            padx=15,
            pady=10,
            sticky="nsew"
        )

        self.card_stock = DashboardCard(
            self,
            "Total Stok"
        )

        self.card_stock.grid(
            row=1,
            column=3,
            padx=15,
            pady=10,
            sticky="nsew"
        )

    # =====================================================

    def create_inventory_cards(self):

        self.card_empty = DashboardCard(
            self,
            "Produk Habis"
        )

        self.card_empty.grid(
            row=2,
            column=0,
            padx=15,
            pady=10,
            sticky="nsew"
        )

        self.card_warning = DashboardCard(
            self,
            "Produk Menipis"
        )

        self.card_warning.grid(
            row=2,
            column=1,
            padx=15,
            pady=10,
            sticky="nsew"
        )

        self.card_value = DashboardCard(
            self,
            "Inventory Value"
        )

        self.card_value.grid(
            row=2,
            column=2,
            padx=15,
            pady=10,
            sticky="nsew"
        )

        self.card_omzet = DashboardCard(
            self,
            "Omzet"
        )

        self.card_omzet.grid(
            row=2,
            column=3,
            padx=15,
            pady=10,
            sticky="nsew"
        )

    # =====================================================

    def create_critical_table(self):

        label = ctk.CTkLabel(
            self,
            text="Critical Products",
            font=("Segoe UI", 18, "bold")
        )

        label.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(20, 5)
        )

        self.critical_table = DataTable(
            self,
            (
                "Kode",
                "Nama",
                "Stok",
                "Minimum",
                "Status"
            ),
            height=5
        )

        self.critical_table.grid(
            row=4,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        # =====================================================

    def create_top_selling_table(self):

        label = ctk.CTkLabel(
            self,
            text="Top Selling Products",
            font=("Segoe UI", 18, "bold")
        )

        label.grid(
            row=5,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(10, 5)
        )

        self.top_table = DataTable(
            self,
            (
                "Kode",
                "Nama",
                "Terjual"
            ),
            height=5
        )

        self.top_table.grid(
            row=6,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

    # =====================================================

    def load_dashboard(self):

        data = self.controller.get_dashboard()

        self.card_product.set_value(
            data["total_produk"]
        )

        self.card_in.set_value(
            data["barang_masuk"]
        )

        self.card_out.set_value(
            data["barang_keluar"]
        )

        self.card_stock.set_value(
            data["total_stok"]
        )

        self.card_empty.set_value(
            data["produk_habis"]
        )

        self.card_warning.set_value(
            data["produk_menipis"]
        )

        self.card_value.set_value(
            f"Rp {data['inventory_value']:,.0f}"
        )

        self.card_omzet.set_value(
            f"Rp {data['omzet']:,.0f}"
        )

        self.load_critical_products()

        self.load_top_selling_products()

    # =====================================================

    def load_critical_products(self):

        self.critical_table.clear()

        rows = self.controller.get_critical_products()[:5]

        for item in rows:

            self.critical_table.insert((
                item["kode"],
                item["nama"],
                item["stok"],
                item["minimum"],
                item["status"]
            ))

    # =====================================================

    def load_top_selling_products(self):

        self.top_table.clear()

        rows = self.controller.get_top_selling_products()[:5]

        for item in rows:

            self.top_table.insert((
                item["kode"],
                item["nama"],
                item["terjual"]
            ))

    # =====================================================

    def refresh(self):

        self.load_dashboard()