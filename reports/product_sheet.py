from config.report_config import ReportConfig
from reports.base_sheet import BaseSheet
from services.report_service import ReportService


class ProductSheet(BaseSheet):

    def __init__(self, workbook):

        super().__init__(workbook, "Products")

        self.report = ReportService()

    def build(self):

        products = self.report.products()

        self.write_title("PRODUCT LIST")

        rows = []

        for item in products:

            rows.append([
                item["kode"],
                item["nama"],
                item["kategori"],
                item["stok_awal"],
                item["masuk"],
                item["keluar"],
                item["stok_akhir"],
                item["stok_minimum"],
                item["status"],
                item["harga"],
                item["inventory_value"]
            ])

        self.create_table(
            row=4,
            headers=ReportConfig.PRODUCT_HEADERS,
            data=rows
        )

        self.create_table(
            row=4,
            headers=ReportConfig.PRODUCT_HEADERS,
            data=rows
        )