import customtkinter as ctk
from tkinter import Menu, messagebox

from ui.gui.components.toolbar import Toolbar
from ui.gui.components.search_bar import SearchBar
from ui.gui.components.data_table import DataTable
from ui.gui.components.transaction_dialog import TransactionDialog
from ui.gui.controllers.transaction_controller import TransactionController


class TransactionView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.controller = TransactionController()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.create_toolbar()
        self.create_search()
        self.create_filter()
        self.create_table()
        self.create_context_menu()

        self.load_data()

    # =====================================================

    def create_toolbar(self):

        self.toolbar = Toolbar(
            self,
            title="Transactions",
            add_command=self.add_transaction,
            refresh_command=self.refresh
        )

        self.toolbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

    # =====================================================

    def create_search(self):

        self.search = SearchBar(
            self,
            command=self.search_transaction
        )

        self.search.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 10)
        )

    # =====================================================

    def create_filter(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 10)
        )

        ctk.CTkLabel(
            frame,
            text="Filter Jenis"
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.filter = ctk.CTkComboBox(
            frame,
            values=[
                "Semua",
                "IN",
                "OUT"
            ],
            width=180,
            command=self.filter_transaction
        )

        self.filter.pack(
            side="left"
        )

        self.filter.set("Semua")

    # =====================================================

    def create_table(self):

        self.table = DataTable(
            self,
            (
                "ID",
                "Tanggal",
                "Kode",
                "Produk",
                "Jenis",
                "Qty",
                "Harga",
                "Total"
            )
        )

        self.table.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.table.tree.bind(
            "<Double-1>",
            self.on_double_click
        )

    # =====================================================

    def populate_table(self, rows):

        self.table.clear()

        for item in rows:

            self.table.insert((
                item["id"],
                item["tanggal"],
                item["kode"],
                item["nama"],
                item["jenis"],
                item["qty"],
                f"Rp {float(item['harga']):,.0f}",
                f"Rp {float(item['total']):,.0f}"
            ))

    # =====================================================

    def load_data(self):

        self.populate_table(
            self.controller.get_transactions()
        )

    # =====================================================

    def search_transaction(self):

        self.populate_table(
            self.controller.search_transactions(
                self.search.get()
            )
        )

    # =====================================================

    def filter_transaction(self, value):

        if value == "Semua":

            self.load_data()

            return

        self.populate_table(
            self.controller.get_transactions_by_type(
                value
            )
        )

        # =====================================================

    def refresh(self):

        self.search.clear()
        self.filter.set("Semua")
        self.load_data()

    # =====================================================

    def get_selected_transaction(self):

        transaction_id = self.table.get_selected_id()

        if transaction_id is None:

            messagebox.showwarning(
                "Transaksi",
                "Pilih transaksi terlebih dahulu."
            )

            return None

        return int(transaction_id)

    # =====================================================

    def on_double_click(self, event):

        row = self.table.tree.identify_row(event.y)

        if not row:
            return

        self.table.tree.selection_set(row)

        values = self.table.tree.item(
            row
        )["values"]

        self.edit_transaction(
            int(values[0])
        )

    # =====================================================

    def add_transaction(self):

        dialog = TransactionDialog(
            self,
            title="Tambah Transaksi"
        )

        self.wait_window(dialog)

        if dialog.result is None:
            return

        valid, message = self.controller.validate(
            dialog.result
        )

        if not valid:

            messagebox.showwarning(
                "Validasi",
                message
            )

            return

        try:

            if dialog.result["jenis"] == "IN":

                self.controller.barang_masuk(
                    dialog.result["product_id"],
                    dialog.result["qty"],
                    dialog.result["harga"],
                    dialog.result["keterangan"]
                )

            else:

                self.controller.barang_keluar(
                    dialog.result["product_id"],
                    dialog.result["qty"],
                    dialog.result["harga"],
                    dialog.result["keterangan"]
                )

            messagebox.showinfo(
                "Transaksi",
                "Transaksi berhasil disimpan."
            )

            self.load_data()

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================
    def edit_transaction(self, transaction_id=None):

        if transaction_id is None:

            transaction_id = self.get_selected_transaction()

        if transaction_id is None:
            return

        transaction = self.controller.get_transaction(
            transaction_id
        )

        if transaction is None:

            messagebox.showerror(
                "Transaksi",
                "Data transaksi tidak ditemukan."
            )

            return

        dialog = TransactionDialog(
            self,
            title="Edit Transaksi"
        )

        dialog.set_data(transaction)

        self.wait_window(dialog)

        if dialog.result is None:
            return

        valid, message = self.controller.validate(
            dialog.result
        )

        if not valid:

            messagebox.showwarning(
                "Validasi",
                message
            )

            return

        try:

            self.controller.update_transaction(

                dialog.result["id"],

                dialog.result["product_id"],

                dialog.result["jenis"],

                dialog.result["qty"],

                dialog.result["harga"],

                dialog.result["keterangan"]

            )

            messagebox.showinfo(

                "Transaksi",

                "Transaksi berhasil diperbarui."

            )

            self.load_data()

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================

    def delete_transaction(self):

        transaction_id = self.get_selected_transaction()

        if transaction_id is None:
            return

        if not messagebox.askyesno(
            "Konfirmasi",
            "Hapus transaksi ini?"
        ):
            return

        try:

            self.controller.delete_transaction(
                transaction_id
            )

            messagebox.showinfo(
                "Transaksi",
                "Transaksi berhasil dihapus."
            )

            self.load_data()

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================================

    def create_context_menu(self):

        self.menu = Menu(
            self,
            tearoff=False
        )

        self.menu.add_command(
            label="Edit",
            command=self.edit_transaction
        )

        self.menu.add_command(
            label="Hapus",
            command=self.delete_transaction
        )

        self.table.tree.bind(
            "<Button-3>",
            self.show_context_menu
        )

    # =====================================================

    def show_context_menu(self, event):

        row = self.table.tree.identify_row(event.y)

        if not row:
            return

        self.table.tree.selection_set(row)

        try:

            self.menu.tk_popup(
                event.x_root,
                event.y_root
            )

        finally:

            self.menu.grab_release()

    