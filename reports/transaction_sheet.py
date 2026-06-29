from config.report_config import ReportConfig
from reports.base_sheet import BaseSheet
from services.report_service import ReportService


class TransactionSheet(BaseSheet):

    def __init__(self, workbook):

        super().__init__(workbook, "Transactions")

        self.report = ReportService()

    def build(self):

        transaksi = self.report.transactions()

        self.write_title("TRANSACTION HISTORY")

        rows = []

        for item in transaksi:

            rows.append([

                item["tanggal"],

                item["kode"],

                item["nama"],

                item["jenis"],

                item["qty"],

                item["harga"],

                item["total"],

                item["keterangan"]

            ])

        self.create_table(

            row=4,

            headers=ReportConfig.TRANSACTION_HEADERS,

            data=rows

        )