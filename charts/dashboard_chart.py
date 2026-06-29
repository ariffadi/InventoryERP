import matplotlib.pyplot as plt

from repositories.product_repository import ProductRepository
from repositories.transaction_repository import TransactionRepository


class DashboardChart:

    def __init__(self):
        self.product_repository = ProductRepository()
        self.transaction_repository = TransactionRepository()

    def show_stock_chart(self):

        products = self.product_repository.get_all()

        nama = []
        stok = []

        for item in products:
            nama.append(item["nama"])
            stok.append(item["stok_awal"] + item["masuk"] - item["keluar"])

        plt.figure(figsize=(10, 5))

        bars = plt.bar(nama, stok)

        plt.title("Stok Produk", fontsize=14)
        plt.xlabel("Produk")
        plt.ylabel("Jumlah")

        plt.grid(axis="y", linestyle="--", alpha=0.4)

        for bar in bars:
            plt.text(
                bar.get_x() + bar.get_width()/2,
                bar.get_height(),
                int(bar.get_height()),
                ha="center",
                va="bottom"
            )

        plt.tight_layout()
        plt.show()

    def show_transaction_chart(self):

        products = self.product_repository.get_all()

        nama = []
        masuk = []
        keluar = []

        for item in products:

            nama.append(item["nama"])
            masuk.append(item["masuk"])
            keluar.append(item["keluar"])

        x = range(len(nama))
        width = 0.35

        plt.figure(figsize=(10,5))

        bar1 = plt.bar(
            [i-width/2 for i in x],
            masuk,
            width,
            label="Masuk"
        )

        bar2 = plt.bar(
            [i+width/2 for i in x],
            keluar,
            width,
            label="Keluar"
        )

        plt.xticks(x, nama)

        plt.title("Barang Masuk vs Barang Keluar")

        plt.grid(axis="y", linestyle="--", alpha=0.4)

        plt.legend()

        for bars in [bar1, bar2]:

            for bar in bars:

                plt.text(
                    bar.get_x()+bar.get_width()/2,
                    bar.get_height(),
                    int(bar.get_height()),
                    ha="center",
                    va="bottom",
                    fontsize=8
                )

        plt.tight_layout()
        plt.show()

    def show_status_chart(self):

        products = self.product_repository.get_all()

        aman = 0
        menipis = 0
        habis = 0

        for item in products:

            stok = item["stok_awal"] + item["masuk"] - item["keluar"]

            if stok == 0:
                habis += 1
            elif stok <= item["stok_minimum"]:
                menipis += 1
            else:
                aman += 1

        plt.figure(figsize=(7,7))

        plt.pie(
            [aman, menipis, habis],
            labels=["Aman", "Menipis", "Habis"],
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Status Produk")

        plt.tight_layout()

        plt.show()

    def show_transaction_trend(self):

        data = self.transaction_repository.get_daily_transactions()

        tanggal = []
        total = []

        for item in data:
            tanggal.append(item["tanggal"])
            total.append(item["total"])

        plt.figure(figsize=(10,5))

        plt.plot(
            tanggal,
            total,
            marker="o",
            linewidth=2
        )

        plt.title("Trend Transaksi Harian")

        plt.xlabel("Tanggal")

        plt.ylabel("Jumlah Transaksi")

        plt.grid(True)

        plt.tight_layout()

        plt.show()