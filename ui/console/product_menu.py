from services.inventory_service import InventoryService
from services.category_service import CategoryService

inventory_service = InventoryService()
category_service = CategoryService()


def tampilkan_kategori():
    kategori = category_service.get_all_categories()

    print("\nDAFTAR KATEGORI")
    print("-" * 30)

    for item in kategori:
        print(f"{item['id']}. {item['nama']}")


def tambah_produk():

    print("\n=== TAMBAH PRODUK ===")

    tampilkan_kategori()

    try:
        kode = input("Kode Produk   : ")
        nama = input("Nama Produk   : ")
        kategori = int(input("Kategori ID   : "))
        stok_awal = int(input("Stok Awal     : "))
        stok_minimum = int(input("Stok Minimum  : "))
        harga = float(input("Harga         : "))

        inventory_service.add_product(
            kode,
            nama,
            kategori,
            stok_awal,
            stok_minimum,
            harga
        )

        print("\n✅ Produk berhasil ditambahkan.")

    except Exception as error:
        print(f"\n❌ {error}")

def lihat_produk():

    produk = inventory_service.get_all_products()

    print("\n" + "=" * 130)
    print("DAFTAR PRODUK".center(130))
    print("=" * 130)

    print(
        f"{'ID':<5}"
        f"{'KODE':<12}"
        f"{'NAMA':<25}"
        f"{'KATEGORI':<18}"
        f"{'AWAL':>8}"
        f"{'MASUK':>8}"
        f"{'KELUAR':>10}"
        f"{'AKHIR':>8}"
        f"{'STATUS':>15}"
        f"{'HARGA':>18}"
    )

    print("-" * 130)

    for item in produk:

        stok_akhir = (
            item["stok_awal"] +
            item["masuk"] -
            item["keluar"]
        )

        if stok_akhir == 0:
            status = "🔴 HABIS"

        elif stok_akhir <= item["stok_minimum"]:
            status = "🟡 MENIPIS"

        else:
            status = "🟢 AMAN"

        print(
            f"{item['id']:<5}"
            f"{item['kode']:<12}"
            f"{item['nama']:<25}"
            f"{item['kategori']:<18}"
            f"{item['stok_awal']:>8}"
            f"{item['masuk']:>8}"
            f"{item['keluar']:>10}"
            f"{stok_akhir:>8}"
            f"{status:>15}"
            f"{'Rp {:,.0f}'.format(item['harga']):>18}"
        )

    print("=" * 130)

def edit_produk():

    lihat_produk()

    try:

        product_id = int(input("\nID Produk yang akan diubah : "))

        product = inventory_service.get_product(product_id)

        if not product:
            print("\n❌ Produk tidak ditemukan.")
            return

        tampilkan_kategori()

        kode = input(f"Kode [{product['kode']}] : ") or product["kode"]
        nama = input(f"Nama [{product['nama']}] : ") or product["nama"]

        kategori = input(f"Kategori ID [{product['kategori_id']}] : ")
        kategori = int(kategori) if kategori else product["kategori_id"]

        stok_awal = input(f"Stok Awal [{product['stok_awal']}] : ")
        stok_awal = int(stok_awal) if stok_awal else product["stok_awal"]

        stok_minimum = input(f"Stok Minimum [{product['stok_minimum']}] : ")
        stok_minimum = int(stok_minimum) if stok_minimum else product["stok_minimum"]

        harga = input(f"Harga [{product['harga']}] : ")
        harga = float(harga) if harga else product["harga"]

        inventory_service.update_product(
            product_id,
            kode,
            nama,
            kategori,
            stok_awal,
            stok_minimum,
            harga
        )

        print("\n✅ Produk berhasil diperbarui.")

    except Exception as error:
        print(f"\n❌ {error}")

def cari_produk():

    keyword = input("\nMasukkan nama atau kode produk : ").strip()

    if not keyword:
        print("\n❌ Kata kunci tidak boleh kosong.")
        return

    produk = inventory_service.search_product(keyword)

    if not produk:
        print("\n❌ Produk tidak ditemukan.")
        return

    print("\n" + "=" * 130)
    print("HASIL PENCARIAN PRODUK".center(130))
    print("=" * 130)

    print(
        f"{'ID':<5}"
        f"{'KODE':<12}"
        f"{'NAMA':<25}"
        f"{'KATEGORI ID':<15}"
        f"{'STOK':>8}"
        f"{'MIN':>8}"
        f"{'HARGA':>18}"
    )

    print("-" * 130)

    for item in produk:

        print(
            f"{item['id']:<5}"
            f"{item['kode']:<12}"
            f"{item['nama']:<25}"
            f"{item['kategori_id']:<15}"
            f"{item['stok_awal']:>8}"
            f"{item['stok_minimum']:>8}"
            f"{'Rp {:,.0f}'.format(item['harga']):>18}"
        )

    print("=" * 130)

def hapus_produk():

    lihat_produk()

    try:

        product_id = int(input("\nID Produk yang akan dihapus : "))

        product = inventory_service.get_product(product_id)

        if not product:
            print("\n❌ Produk tidak ditemukan.")
            return

        konfirmasi = input(
            f"Yakin ingin menghapus '{product['nama']}'? (y/n) : "
        ).lower()

        if konfirmasi != "y":
            print("\nPenghapusan dibatalkan.")
            return

        inventory_service.delete_product(product_id)

        print("\n✅ Produk berhasil dihapus.")

    except Exception as error:
        print(f"\n❌ {error}")


def menu():

    while True:

        print("\n" + "=" * 40)
        print("        PRODUCT MENU")
        print("=" * 40)

        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Cari Produk")
        print("4. Edit Produk")
        print("5. Hapus Produk")
        print("0. Keluar")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            tambah_produk()

        elif pilih == "2":
            lihat_produk()

        elif pilih == "3":
            cari_produk()

        elif pilih == "4":
            edit_produk()

        elif pilih == "5":
            hapus_produk()

        elif pilih == "0":
            print("\nTerima kasih.")
            break

        else:
            print("\n❌ Menu tidak tersedia.")