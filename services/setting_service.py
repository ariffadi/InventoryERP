from config.settings_manager import SettingsManager


class SettingService:

    # =====================================================

    def get_settings(self):

        return SettingsManager.all()

    # =====================================================

    def get(self, key):

        return SettingsManager.get(key)

    # =====================================================

    def set(self, key, value):

        SettingsManager.set(key, value)

    # =====================================================

    def save_settings(self, data):

        for key, value in data.items():

            SettingsManager.set(
                key,
                value
            )