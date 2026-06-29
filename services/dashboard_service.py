from repositories.product_repository import ProductRepository
from repositories.transaction_repository import TransactionRepository


class DashboardService:

    def __init__(self):

        self.product_repository = ProductRepository()
        self.transaction_repository = TransactionRepository()

    def get_dashboard(self):

        products = self.product_repository.get_all()
        transactions = self.transaction_repository.get_all()

        total_produk = len(products)

        barang_masuk = 0
        barang_keluar = 0
        omzet = 0

        produk_menipis = 0
        produk_habis = 0

        total_stok = 0

        inventory_value = 0

        for trx in transactions:

            if trx["jenis"] == "IN":

                barang_masuk += trx["qty"]

            else:

                barang_keluar += trx["qty"]

                omzet += trx["total"]

        for item in products:

            stok = item["stok_awal"] + item["masuk"] - item["keluar"]

            total_stok += stok

            inventory_value += stok * item["harga"]

            if stok == 0:

                produk_habis += 1

            elif stok <= item["stok_minimum"]:

                produk_menipis += 1

        return {

            "total_produk": total_produk,

            "barang_masuk": barang_masuk,

            "barang_keluar": barang_keluar,

            "total_stok": total_stok,

            "omzet": omzet,

            "produk_menipis": produk_menipis,

            "produk_habis": produk_habis,

            "inventory_value": inventory_value

        }

    def get_critical_products(self):

        products = self.product_repository.get_all()

        critical = []

        for item in products:

            stok = item["stok_awal"] + item["masuk"] - item["keluar"]

            if stok == 0:

                status = "🔴 HABIS"

            elif stok <= item["stok_minimum"]:

                status = "🟡 MENIPIS"

            else:

                continue

            critical.append({

                "id": item["id"],
                "kode": item["kode"],
                "nama": item["nama"],
                "stok": stok,
                "minimum": item["stok_minimum"],
                "status": status

            })

        return critical

    def get_top_selling_products(self):

        products = self.product_repository.get_all()

        data = []

        for item in products:

            data.append({

                "kode": item["kode"],

                "nama": item["nama"],

                "terjual": item["keluar"]

            })

        data.sort(
            key=lambda x: x["terjual"],
            reverse=True
        )

        return data[:10]