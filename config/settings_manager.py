import json
from pathlib import Path


class SettingsManager:

    FILE = Path("config/settings.json")

    # =====================================================

    @classmethod
    def load(cls):

        if not cls.FILE.exists():

            return {}

        with open(
            cls.FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # =====================================================

    @classmethod
    def save(cls, data):

        with open(
            cls.FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # =====================================================

    @classmethod
    def get(cls, key, default=None):

        data = cls.load()

        return data.get(
            key,
            default
        )

    # =====================================================

    @classmethod
    def set(cls, key, value):

        data = cls.load()

        data[key] = value

        cls.save(data)

    # =====================================================

    @classmethod
    def all(cls):

        return cls.load()