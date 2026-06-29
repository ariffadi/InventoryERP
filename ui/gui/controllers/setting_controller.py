from services.setting_service import SettingService


class SettingController:

    def __init__(self):

        self.service = SettingService()

    # =====================================================

    def load(self):

        return self.service.get_settings()

    # =====================================================

    def get(self, key):

        return self.service.get(key)

    # =====================================================

    def set(self, key, value):

        self.service.set(
            key,
            value
        )

    # =====================================================

    def save(self, data):

        self.service.save_settings(
            data
        )