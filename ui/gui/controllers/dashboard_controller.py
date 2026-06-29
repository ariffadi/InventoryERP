from services.dashboard_service import DashboardService


class DashboardController:

    def __init__(self):

        self.service = DashboardService()

    # =====================================================

    def get_dashboard(self):

        return self.service.get_dashboard()

    # =====================================================

    def get_critical_products(self):

        return self.service.get_critical_products()

    # =====================================================

    def get_top_selling_products(self):

        return self.service.get_top_selling_products()

    # =====================================================

    def refresh(self):

        return self.get_dashboard()