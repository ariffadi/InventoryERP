from services.dashboard_service import DashboardService
from services.inventory_service import InventoryService
from services.transaction_service import TransactionService


class ReportService:

    def financial_summary(self):

        dashboard = self.dashboard()

        return [

        ("Total Produk", dashboard["total_produk"]),

        ("Barang Masuk", dashboard["barang_masuk"]),

        ("Barang Keluar", dashboard["barang_keluar"]),

        ("Total Stock", dashboard["total_stok"]),

        ("Inventory Value", dashboard["inventory_value"]),

        ("Total Omzet", dashboard["omzet"]),

        ("Produk Menipis", dashboard["produk_menipis"]),

        ("Produk Habis", dashboard["produk_habis"])

    ]

    def __init__(self):

        self.dashboard_service = DashboardService()
        self.inventory_service = InventoryService()
        self.transaction_service = TransactionService()

    def dashboard(self):

        return self.dashboard_service.get_dashboard()

    def transactions(self):

        return self.transaction_service.get_all_transactions()

    def top_selling(self):

        return self.dashboard_service.get_top_selling_products()

    def products(self):

        products = self.inventory_service.get_all_products()

        result = []

        for item in products:

            stok_akhir = (
                item["stok_awal"]
                + item["masuk"]
                - item["keluar"]
            )

            if stok_akhir == 0:
                status = "🔴 HABIS"

            elif stok_akhir <= item["stok_minimum"]:
                status = "🟡 MENIPIS"

            else:
                status = "🟢 AMAN"

            inventory_value = stok_akhir * item["harga"]

            result.append({

                "kode": item["kode"],

                "nama": item["nama"],

                "kategori": item["kategori"],

                "stok_awal": item["stok_awal"],

                "masuk": item["masuk"],

                "keluar": item["keluar"],

                "stok_akhir": stok_akhir,

                "stok_minimum": item["stok_minimum"],

                "status": status,

                "harga": item["harga"],

                "inventory_value": inventory_value

            })

        return result

    def critical_products(self):

        products = self.products()

        result = []

        for item in products:

            if item["status"] == "🟢 AMAN":
                continue

            selisih = item["stok_akhir"] - item["stok_minimum"]

            if selisih <= -10:

                prioritas = "🔴 Tinggi"

            elif selisih <= -5:

                prioritas = "🟠 Sedang"

            else:

                prioritas = "🟡 Rendah"

            result.append({

                "kode": item["kode"],

                "nama": item["nama"],

                "kategori": item["kategori"],

                "stok": item["stok_akhir"],

                "minimum": item["stok_minimum"],

                "selisih": selisih,

                "prioritas": prioritas,

                "status": item["status"]

            })

        return result