from config.report_config import ReportConfig

from reports.base_sheet import BaseSheet

from services.report_service import ReportService


class CriticalSheet(BaseSheet):

    def __init__(self, workbook):

        super().__init__(workbook, "Critical Stock")

        self.report = ReportService()

    def build(self):

        products = self.report.critical_products()

        self.write_title("CRITICAL STOCK REPORT")

        rows = []

        for item in products:

            rows.append([

                item["kode"],

                item["nama"],

                item["kategori"],

                item["stok"],

                item["minimum"],

                item["selisih"],

                item["prioritas"],

                item["status"]

            ])

        self.create_table(

            row=4,

            headers=ReportConfig.CRITICAL_HEADERS,

            data=rows

        )