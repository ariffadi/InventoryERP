from services.report_service import ReportService


class ReportController:

    def __init__(self):

        self.service = ReportService()

    # =====================================================

    def dashboard(self):

        return self.service.dashboard()

    # =====================================================

    def transactions(self):

        return self.service.transactions()

    # =====================================================

    def products(self):

        return self.service.products()

    # =====================================================

    def critical_products(self):

        return self.service.critical_products()

    # =====================================================

    def top_selling(self):

        return self.service.top_selling()

    # =====================================================

    def financial_summary(self):

        return self.service.financial_summary()