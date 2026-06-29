from services.inventory_service import InventoryService


class ProductController:

    def __init__(self):

        self.service = InventoryService()

    # =====================================================
    # LOAD DATA
    # =====================================================

    def get_products(self):

        return self.service.get_all_products()

    def refresh(self):

        return self.get_products()
    
        # =====================================================

    def get_product_list(self):

        return self.service.get_product_list()

    # =====================================================
    # SEARCH
    # =====================================================

    def search_products(self, keyword):

        keyword = (keyword or "").strip()

        if keyword == "":
            return self.get_products()

        return self.service.search_product(keyword)

    # =====================================================
    # ADD
    # =====================================================

    def add_product(
        self,
        kode,
        nama,
        kategori_id,
        stok_awal,
        stok_minimum,
        harga
    ):

        self.service.add_product(
            kode,
            nama,
            kategori_id,
            stok_awal,
            stok_minimum,
            harga
        )

        return True

    # =====================================================
    # UPDATE
    # =====================================================

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

        self.service.update_product(
            product_id,
            kode,
            nama,
            kategori_id,
            stok_awal,
            stok_minimum,
            harga
        )

        return True

    # =====================================================
    # DELETE
    # =====================================================

    def delete_product(self, product_id):

        self.service.delete_product(product_id)

        return True

    # =====================================================
    # GET DETAIL
    # =====================================================

    def get_product(self, product_id):

        return self.service.get_product(product_id)

    # =====================================================
    # VALIDATION
    # =====================================================

    def validate(self, data):

        if not data["kode"].strip():
            return False, "Kode produk wajib diisi."

        if not data["nama"].strip():
            return False, "Nama produk wajib diisi."

        if data["kategori_id"] is None:
            return False, "Kategori belum dipilih."

        try:
            stok_awal = int(data["stok_awal"])

            if stok_awal < 0:
                return False, "Stok awal tidak boleh negatif."

        except Exception:
            return False, "Stok awal harus berupa angka."

        try:
            stok_minimum = int(data["stok_minimum"])

            if stok_minimum < 0:
                return False, "Stok minimum tidak boleh negatif."

        except Exception:
            return False, "Stok minimum harus berupa angka."

        try:
            harga = float(data["harga"])

            if harga < 0:
                return False, "Harga tidak boleh negatif."

        except Exception:
            return False, "Harga harus berupa angka."

        return True, ""