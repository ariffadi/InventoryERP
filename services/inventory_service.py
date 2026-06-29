from repositories.product_repository import ProductRepository
from utils.logger import logger
from repositories.transaction_repository import TransactionRepository


class InventoryService:

    def __init__(self):

        self.repository = ProductRepository()
        self.transaction_repository = TransactionRepository()

    def add_product(
        self,
        kode,
        nama,
        kategori_id,
        stok_awal,
        stok_minimum,
        harga
    ):

        kode = kode.strip().upper()
        nama = nama.strip()

        if not kode:
            raise ValueError("Kode produk tidak boleh kosong.")

        if not nama:
            raise ValueError("Nama produk tidak boleh kosong.")

        if stok_awal < 0:
            raise ValueError("Stok awal tidak boleh negatif.")

        if stok_minimum < 0:
            raise ValueError("Stok minimum tidak boleh negatif.")

        if harga <= 0:
            raise ValueError("Harga harus lebih dari nol.")

        if self.repository.get_by_code(kode):
            raise ValueError("Kode produk sudah digunakan.")

        self.repository.add(
            kode,
            nama,
            kategori_id,
            stok_awal,
            stok_minimum,
            harga
        )
        logger.info(f"Produk ditambahkan | {kode} - {nama}")

    def get_all_products(self):

        return self.repository.get_all()

    def search_product(self, keyword):

        return self.repository.search(keyword)

    def get_product(self, product_id):

        return self.repository.get_by_id(product_id)

    def update_product(
        self,
        product_id,
        kode,
        nama,
        kategori_id,
        stok_awal,
        stok_minimum,
        harga
    ):

        kode = kode.strip().upper()
        nama = nama.strip()

        if not kode:
            raise ValueError("Kode produk tidak boleh kosong.")

        if not nama:
            raise ValueError("Nama produk tidak boleh kosong.")

        if stok_awal < 0:
            raise ValueError("Stok awal tidak boleh negatif.")

        if stok_minimum < 0:
            raise ValueError("Stok minimum tidak boleh negatif.")

        if harga <= 0:
            raise ValueError("Harga harus lebih dari nol.")

        product = self.repository.get_by_code(kode)

        if product and product["id"] != product_id:
            raise ValueError("Kode produk sudah digunakan.")

        self.repository.update(
            product_id,
            kode,
            nama,
            kategori_id,
            stok_awal,
            stok_minimum,
            harga
        )
        logger.info(f"Produk diperbarui | {kode}")

    def delete_product(self, product_id):

        product = self.repository.get_by_id(product_id)

        if not product:
            raise ValueError("Produk tidak ditemukan.")

        if self.transaction_repository.has_transaction(product_id):
            raise ValueError(
                "Produk tidak dapat dihapus karena sudah memiliki riwayat transaksi."
            )

        self.repository.delete(product_id)
        logger.info(
            f"Produk dihapus | ID={product_id}"
)
    
        # =====================================================

    def get_product_list(self):

        return self.repository.get_all()