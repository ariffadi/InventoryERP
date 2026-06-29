from services.transaction_service import TransactionService


class TransactionController:

    def __init__(self):

        self.service = TransactionService()

    # =====================================================
    # LOAD DATA
    # =====================================================

    def get_transactions(self):

        return self.service.get_all_transactions()

    def refresh(self):

        return self.get_transactions()

    # =====================================================
    # SEARCH
    # =====================================================

    def search_transactions(self, keyword):

        return self.service.search_transaction(keyword)

    # =====================================================
    # FILTER
    # =====================================================

    def get_transactions_by_type(self, jenis):

        return self.service.get_transactions_by_type(jenis)

    def get_transactions_by_date(self, tanggal):

        return self.service.get_transactions_by_date(tanggal)

    # =====================================================
    # DETAIL
    # =====================================================

    def get_transaction(self, transaction_id):

        return self.service.get_transaction(transaction_id)

    # =====================================================
    # DELETE
    # =====================================================

    def delete_transaction(self, transaction_id):

        self.service.delete_transaction(transaction_id)

        return True

    # =====================================================
    # UPDATE
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

        self.service.update_transaction(
            transaction_id,
            product_id,
            jenis,
            qty,
            harga,
            keterangan
        )

        return True

    # =====================================================
    # BARANG MASUK
    # =====================================================

    def barang_masuk(
        self,
        product_id,
        qty,
        harga,
        keterangan=""
    ):

        self.service.barang_masuk(
            product_id,
            qty,
            harga,
            keterangan
        )

        return True

    # =====================================================
    # BARANG KELUAR
    # =====================================================

    def barang_keluar(
        self,
        product_id,
        qty,
        harga,
        keterangan=""
    ):

        self.service.barang_keluar(
            product_id,
            qty,
            harga,
            keterangan
        )

        return True

    # =====================================================
    # VALIDATION
    # =====================================================

    def validate(self, data):

        if data["product_id"] is None:
            return False, "Produk harus dipilih."

        if data["jenis"] not in ("IN", "OUT"):
            return False, "Jenis transaksi tidak valid."

        try:
            qty = int(data["qty"])

            if qty <= 0:
                return False, "Qty harus lebih besar dari nol."

        except Exception:
            return False, "Qty harus berupa angka."

        try:
            harga = float(data["harga"])

            if harga <= 0:
                return False, "Harga harus lebih besar dari nol."

        except Exception:
            return False, "Harga harus berupa angka."

        return True, ""