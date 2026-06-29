from datetime import datetime
from utils.logger import logger
from repositories.transaction_repository import TransactionRepository
from repositories.product_repository import ProductRepository


class TransactionService:

    def __init__(self):

        self.transaction_repository = TransactionRepository()
        self.product_repository = ProductRepository()

    def barang_masuk(self, product_id, qty, harga, keterangan=""):

        product = self.product_repository.get_by_id(product_id)

        if not product:
            raise ValueError("Produk tidak ditemukan.")

        if qty <= 0:
            raise ValueError("Qty harus lebih dari nol.")

        if harga <= 0:
            raise ValueError("Harga harus lebih dari nol.")

        total = qty * harga

        self.transaction_repository.add(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            product_id,
            "IN",
            qty,
            harga,
            total,
            keterangan
        )
        logger.info(
            f"Barang Masuk | Product={product_id} Qty={qty}"
            )

    def barang_keluar(self, product_id, qty, harga, keterangan=""):

        product = self.product_repository.get_by_id(product_id)

        if not product:
            raise ValueError("Produk tidak ditemukan.")

        produk = self.product_repository.get_all()

        stok_akhir = 0

        for item in produk:

            if item["id"] == product_id:

                stok_akhir = (
                    item["stok_awal"] +
                    item["masuk"] -
                    item["keluar"]
                )

                break

        if qty <= 0:
            raise ValueError("Qty harus lebih dari nol.")

        if qty > stok_akhir:
            raise ValueError(
                f"Stok tidak mencukupi. Stok tersedia : {stok_akhir}"
            )

        total = qty * harga

        self.transaction_repository.add(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            product_id,
            "OUT",
            qty,
            harga,
            total,
            keterangan
        )
        logger.info(
            f"Barang Keluar | Product={product_id} Qty={qty}"
        )

    def get_all_transactions(self):

        return self.transaction_repository.get_all()

    # =====================================================

    def get_transaction(self, transaction_id):

        return self.transaction_repository.get_by_id(
            transaction_id
        )

    def get_transactions_by_type(self, jenis):

        return self.transaction_repository.get_by_type(jenis)

    def get_transactions_by_date(self, tanggal):

        return self.transaction_repository.get_by_date(tanggal)
    
        # =====================================================

    def delete_transaction(self, transaction_id):

        transaction = self.transaction_repository.get_by_id(
            transaction_id
        )

        if not transaction:
            raise ValueError(
                "Data transaksi tidak ditemukan."
            )

        self.transaction_repository.delete(
            transaction_id
        )

        logger.info(
            f"Transaksi dihapus | ID={transaction_id}"
        )
    
        # =====================================================

    def update_transaction(
        self,
        transaction_id,
        product_id,
        jenis,
        qty,
        harga,
        keterangan=""
    ):

        transaction = self.transaction_repository.get_by_id(
            transaction_id
        )

        if not transaction:
            raise ValueError(
                "Data transaksi tidak ditemukan."
            )

        product = self.product_repository.get_by_id(
            product_id
        )

        if not product:
            raise ValueError(
                "Produk tidak ditemukan."
            )

        qty = int(qty)
        harga = float(harga)

        if qty <= 0:
            raise ValueError(
                "Qty harus lebih besar dari nol."
            )

        if harga <= 0:
            raise ValueError(
                "Harga harus lebih besar dari nol."
            )

        if jenis == "OUT":

            produk = self.product_repository.get_all()

            stok_akhir = 0

            for item in produk:

                if item["id"] == product_id:

                    stok_akhir = (
                        (item["stok_awal"] or 0)
                        + (item["masuk"] or 0)
                        - (item["keluar"] or 0)
                    )

                    break

            # Kembalikan qty transaksi lama jika sebelumnya OUT
            if (
                transaction["jenis"] == "OUT"
                and transaction["product_id"] == product_id
            ):
                stok_akhir += transaction["qty"]

            if qty > stok_akhir:

                raise ValueError(
                    f"Stok tidak mencukupi. Stok tersedia : {stok_akhir}"
                )

        total = qty * harga

        self.transaction_repository.update(
            transaction_id,
            transaction["tanggal"],
            product_id,
            jenis,
            qty,
            harga,
            total,
            keterangan
        )

        logger.info(
            f"Transaksi diperbarui | ID={transaction_id}"
        )

    # =====================================================

    def search_transaction(self, keyword):

        keyword = (keyword or "").strip()

        if keyword == "":
            return self.get_all_transactions()

        return self.transaction_repository.search(
            keyword
        )