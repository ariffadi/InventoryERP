from datetime import datetime

from config.report_config import ReportConfig
from reports.base_sheet import BaseSheet
from services.report_service import ReportService


class DashboardSheet(BaseSheet):

    def __init__(self, workbook):

        super().__init__(workbook, "Dashboard")

        self.report = ReportService()

    def build(self):

        data = self.report.dashboard()

        self.write_title(
            ReportConfig.DASHBOARD_TITLE
        )

        self.write_label_value(
            3,
            "Tanggal Report",
            datetime.now().strftime("%d-%m-%Y %H:%M")
        )

        self.write_label_value(5, "Total Produk", data["total_produk"])
        self.write_label_value(6, "Barang Masuk", data["barang_masuk"])
        self.write_label_value(7, "Barang Keluar", data["barang_keluar"])
        self.write_label_value(8, "Total Stok", data["total_stok"])
        self.write_label_value(9, "Inventory Value", data["inventory_value"])
        self.write_label_value(10, "Total Omzet", data["omzet"])
        self.write_label_value(11, "Produk Menipis", data["produk_menipis"])
        self.write_label_value(12, "Produk Habis", data["produk_habis"])
