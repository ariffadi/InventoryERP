import customtkinter as ctk
from ui.gui.components.notification import Notification
from ui.gui.theme import Theme
from ui.gui.components.toolbar import Toolbar
from ui.gui.components.search_bar import SearchBar
from ui.gui.components.data_table import DataTable
from ui.gui.controllers.product_controller import ProductController
from ui.gui.components.product_dialog import ProductDialog



class ProductView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.controller = ProductController()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_toolbar()

        self.create_search()

        self.create_table()

        self.create_context_menu()

        self.load_data()

    # ==================================================

    def create_toolbar(self):

        self.toolbar = Toolbar(
            self,
            title="Products",
            add_command=self.add_product,
            refresh_command=self.refresh
        )

        self.toolbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

    # ==================================================

    def create_search(self):

        self.search = SearchBar(
            self,
            command=self.search_product
        )

        self.search.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 10)
        )

    # ==================================================

    def create_table(self):

        self.table = DataTable(
            self,
            (
                "ID",
                "Kode",
                "Nama",
                "Kategori",
                "Stok",
                "Harga"
            )
        )

        self.table.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        # Double click untuk edit produk
        self.table.tree.bind(
            "<Double-1>",
            self.on_double_click
        )
    # ==================================================

    def load_data(self):

        self.table.clear()

        products = self.controller.get_products()

        for item in products:

            stok = (
                item["stok_awal"] +
                item["masuk"] -
                item["keluar"]
            )

            self.table.insert((
                item["id"],
                item["kode"],
                item["nama"],
                item["kategori"],
                stok,
                f"Rp {item['harga']:,.0f}"
            ))

    # ==================================================

    def search_product(self):

        keyword = self.search.get()

        self.table.clear()

        products = self.controller.search_products(keyword)

        for item in products:

            stok = (
                item["stok_awal"] +
                item["masuk"] -
                item["keluar"]
            )

            self.table.insert((
                item["id"],
                item["kode"],
                item["nama"],
                item["kategori"],
                stok,
                f"Rp {item['harga']:,.0f}"
            ))

# ==================================================

    def refresh(self):

        self.search.clear()

        self.load_data()


# ==================================================

    def get_selected_product(self):

        selected = self.table.tree.selection()

        if not selected:

            Notification.warning(
            self,
            "Pilih produk terlebih dahulu."
        )

            return None

        values = self.table.tree.item(
            selected[0],
            "values"
        )

        return int(values[0])


# ==================================================

    def on_double_click(self, event):

        selected = self.table.tree.selection()

        if not selected:
            return

        product_id = int(
            self.table.tree.item(
                selected[0],
                "values"
            )[0]
        )

        self.edit_product(product_id)

    # ==================================================

    def add_product(self):

        dialog = ProductDialog(
            self,
            title="Tambah Produk"
        )

        self.wait_window(dialog)

        if dialog.result is None:
            return

        valid, message = self.controller.validate(
            dialog.result
        )

        if not valid:

            Notification.warning(
            self,
            message
        )

            return

        self.controller.add_product(
            dialog.result["kode"],
            dialog.result["nama"],
            dialog.result["kategori_id"],
            dialog.result["stok_awal"],
            dialog.result["stok_minimum"],
            dialog.result["harga"]
        )

        Notification.success(
            self,
            "Produk berhasil ditambahkan."
        )

        self.load_data()

# ==================================================

    def edit_product(self, product_id=None):

        if product_id is None:
            product_id = self.get_selected_product()

        if product_id is None:
            return

        product = self.controller.get_product(product_id)

        try:

            self.controller.delete_product(product_id)

        except ValueError as e:

            Notification.error(
                self,
                str(e)
            )
            return

        dialog = ProductDialog(
            self,
            title="Edit Produk"
        )

        dialog.set_data(product)

        self.wait_window(dialog)

        if dialog.result is None:
            return

        valid, message = self.controller.validate(
            dialog.result
        )

        if not valid:

            Notification.warning(
                self,
                message
            )

            return

        self.controller.update_product(
            dialog.result["id"],
            dialog.result["kode"],
            dialog.result["nama"],
            dialog.result["kategori_id"],
            dialog.result["stok_awal"],
            dialog.result["stok_minimum"],
            dialog.result["harga"]
        )

        Notification.success(
            self,
            "Produk berhasil ditambahkan."
        )

        self.load_data()

# ==================================================

    def delete_product(self):

        product_id = self.get_selected_product()

        if product_id is None:
            return

        if not Notification.confirm(
            self,
            "Hapus produk ini?"
        ):

            return

        self.controller.delete_product(product_id)

        Notification.success(
            self,
            "Produk berhasil ditambahkan."
        )

        self.load_data()

# ==================================================

    def create_context_menu(self):

        from tkinter import Menu

        self.menu = Menu(
            self,
            tearoff=False
        )

        self.menu.add_command(
            label="Edit",
            command=self.edit_product
        )

        self.menu.add_command(
            label="Hapus",
            command=self.delete_product
        )

        self.table.tree.bind(
            "<Button-3>",
            self.show_context_menu
        )


# ==================================================

    def show_context_menu(self, event):

        row = self.table.tree.identify_row(event.y)

        if row:

            self.table.tree.selection_set(row)

            self.menu.post(
                event.x_root,
                event.y_root
            )