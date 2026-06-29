from config.report_config import ReportConfig

from reports.base_sheet import BaseSheet

from services.report_service import ReportService


class FinancialSheet(BaseSheet):

    def __init__(self, workbook):

        super().__init__(workbook, "Financial")

        self.report = ReportService()

    def build(self):

        summary = self.report.financial_summary()

        self.write_title("FINANCIAL SUMMARY")

        headers = ReportConfig.FINANCIAL_HEADERS

        self.create_table(

            row=4,

            headers=headers,

            data=summary

        )