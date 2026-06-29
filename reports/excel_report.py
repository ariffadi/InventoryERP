from datetime import datetime

from reports.report_builder import ReportBuilder
from reports.dashboard_sheet import DashboardSheet
from reports.product_sheet import ProductSheet
from reports.transaction_sheet import TransactionSheet
from reports.critical_sheet import CriticalSheet
from reports.financial_sheet import FinancialSheet
from reports.chart_sheet import ChartSheet

from utils.logger import logger


class ExcelReport:

    def __init__(self):

        self.builder = ReportBuilder()

    # =====================================================

    def export(self, filename=None):

        self.builder.remove_default_sheet()

        DashboardSheet(
            self.builder.workbook
        ).build()

        ProductSheet(
            self.builder.workbook
        ).build()

        TransactionSheet(
            self.builder.workbook
        ).build()

        CriticalSheet(
            self.builder.workbook
        ).build()

        FinancialSheet(
            self.builder.workbook
        ).build()

        ChartSheet(
            self.builder.workbook
        ).build()

        # ----------------------------------------------

        if filename is None:

            filename = (
                "Inventory_Report_"
                + datetime.now().strftime("%Y%m%d_%H%M%S")
                + ".xlsx"
            )

        self.builder.save(filename)

        logger.info(
            f"Export Excel berhasil | {filename}"
        )

        return filename