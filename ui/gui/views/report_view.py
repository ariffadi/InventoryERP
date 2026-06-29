import customtkinter as ctk
from tkinter import filedialog, messagebox
from reports.excel_report import ExcelReport
from ui.gui.theme import Theme
from ui.gui.components.toolbar import Toolbar
from ui.gui.components.data_table import DataTable
from ui.gui.controllers.report_controller import ReportController


class ReportView(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.controller = ReportController()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_toolbar()

        self.create_filter()

        self.create_table()

        self.load_dashboard_report()

    # =====================================================

    def create_toolbar(self):

        self.toolbar = Toolbar(
            self,
            title="Reports",
            add_command=self.export_excel,
            refresh_command=self.refresh
        )

        self.toolbar.add_button.configure(
            text="Export Excel"
        )

        self.toolbar.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

    # =====================================================

    def create_filter(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 10)
        )

        ctk.CTkLabel(
            frame,
            text="Jenis Report",
            font=Theme.FONT_NORMAL
        ).pack(
            side="left",
            padx=(0, 10)
        )

        self.report_type = ctk.CTkComboBox(
            frame,
            values=[
                "Dashboard",
                "Products",
                "Transactions",
                "Critical Products",
                "Top Selling"
            ],
            width=220,
            command=self.change_report
        )

        self.report_type.pack(
            side="left"
        )

        self.report_type.set("Dashboard")

    # =====================================================

    def create_table(self):

        self.table = DataTable(
            self,
            (
                "Field",
                "Value"
            )
        )

        self.table.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

            # =====================================================

    def change_report(self, value):

        if value == "Dashboard":

            self.load_dashboard_report()

        elif value == "Products":

            self.load_product_report()

        elif value == "Transactions":

            self.load_transaction_report()

        elif value == "Critical Products":

            self.load_critical_report()

        elif value == "Top Selling":

            self.load_top_selling_report()

    # =====================================================

    def load_dashboard_report(self):

        self.table.tree.configure(
            columns=("Field", "Value")
        )

        self.table.tree["show"] = "headings"

        self.table.tree.heading("Field", text="Field")
        self.table.tree.heading("Value", text="Value")

        self.table.tree.column("Field", width=250)
        self.table.tree.column("Value", width=250)

        self.table.clear()

        for item in self.controller.financial_summary():

            self.table.insert(item)

    # =====================================================

    def load_product_report(self):

        self.table.tree.configure(
            columns=(
                "Kode",
                "Nama",
                "Kategori",
                "Stok",
                "Status",
                "Inventory Value"
            )
        )

        self.table.tree["show"] = "headings"

        columns = (
            "Kode",
            "Nama",
            "Kategori",
            "Stok",
            "Status",
            "Inventory Value"
        )

        for col in columns:

            self.table.tree.heading(col, text=col)

            self.table.tree.column(
                col,
                width=150,
                anchor="center"
            )

        self.table.clear()

        rows = self.controller.products()

        for item in rows:

            self.table.insert((
                item["kode"],
                item["nama"],
                item["kategori"],
                item["stok_akhir"],
                item["status"],
                f"Rp {item['inventory_value']:,.0f}"
            ))

    # =====================================================

    def load_transaction_report(self):

        self.table.tree.configure(
            columns=(
                "Tanggal",
                "Kode",
                "Nama",
                "Jenis",
                "Qty",
                "Total"
            )
        )

        self.table.tree["show"] = "headings"

        columns = (
            "Tanggal",
            "Kode",
            "Nama",
            "Jenis",
            "Qty",
            "Total"
        )

        for col in columns:

            self.table.tree.heading(col, text=col)

            self.table.tree.column(
                col,
                width=140,
                anchor="center"
            )

        self.table.clear()

        rows = self.controller.transactions()

        for item in rows:

            self.table.insert((
                item["tanggal"],
                item["kode"],
                item["nama"],
                item["jenis"],
                item["qty"],
                f"Rp {item['total']:,.0f}"
            ))

    # =====================================================

    def load_critical_report(self):

        self.table.tree.configure(
            columns=(
                "Kode",
                "Nama",
                "Stok",
                "Minimum",
                "Status",
                "Prioritas"
            )
        )

        self.table.tree["show"] = "headings"

        columns = (
            "Kode",
            "Nama",
            "Stok",
            "Minimum",
            "Status",
            "Prioritas"
        )

        for col in columns:

            self.table.tree.heading(col, text=col)

            self.table.tree.column(
                col,
                width=140,
                anchor="center"
            )

        self.table.clear()

        rows = self.controller.critical_products()

        for item in rows:

            self.table.insert((
                item["kode"],
                item["nama"],
                item["stok"],
                item["minimum"],
                item["status"],
                item["prioritas"]
            ))

    # =====================================================

    def load_top_selling_report(self):

        self.table.tree.configure(
            columns=(
                "Kode",
                "Nama",
                "Terjual"
            )
        )

        self.table.tree["show"] = "headings"

        columns = (
            "Kode",
            "Nama",
            "Terjual"
        )

        for col in columns:

            self.table.tree.heading(col, text=col)

            self.table.tree.column(
                col,
                width=180,
                anchor="center"
            )

        self.table.clear()

        rows = self.controller.top_selling()

        for item in rows:

            self.table.insert((
                item["kode"],
                item["nama"],
                item["terjual"]
            ))

    # =====================================================

    def refresh(self):

        self.change_report(
            self.report_type.get()
        )

    # =====================================================

    # =====================================================

    def export_excel(self):

        filename = filedialog.asksaveasfilename(

            title="Export Excel",

            defaultextension=".xlsx",

            filetypes=[
                ("Excel Workbook", "*.xlsx")
            ]

        )

        if not filename:
            return

        try:

            report = ExcelReport()

            report.export(filename)

            messagebox.showinfo(
                "Export",
                f"Report berhasil dibuat.\n\n{filename}"
            )

        except Exception as e:

            messagebox.showerror(
                "Export",
                str(e)
            )