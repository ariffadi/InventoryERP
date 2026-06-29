from services.transaction_service import TransactionService
from services.inventory_service import InventoryService

transaction_service = TransactionService()
inventory_service = InventoryService()


def tampilkan_produk():

    produk = inventory_service.get_all_products()

    print("\n" + "=" * 120)
    print("DAFTAR PRODUK".center(120))
    print("=" * 120)

    print(
        f"{'ID':<5}"
        f"{'KODE':<12}"
        f"{'NAMA':<25}"
        f"{'KATEGORI':<18}"
        f"{'STOK':>8}"
    )

    print("-" * 120)

    for item in produk:

        stok = item["stok_awal"] + item["masuk"] - item["keluar"]

        print(
            f"{item['id']:<5}"
            f"{item['kode']:<12}"
            f"{item['nama']:<25}"
            f"{item['kategori']:<18}"
            f"{stok:>8}"
        )

    print("=" * 120)


def tampilkan_transaksi(transaksi, judul):

    print("\n" + "=" * 130)
    print(judul.center(130))
    print("=" * 130)

    print(
        f"{'ID':<5}"
        f"{'TANGGAL':<22}"
        f"{'KODE':<12}"
        f"{'NAMA':<25}"
        f"{'JENIS':<8}"
        f"{'QTY':>8}"
        f"{'TOTAL':>18}"
    )

    print("-" * 130)

    if not transaksi:
        print("Tidak ada data transaksi.")
    else:
        for item in transaksi:

            print(
                f"{item['id']:<5}"
                f"{item['tanggal']:<22}"
                f"{item['kode']:<12}"
                f"{item['nama']:<25}"
                f"{item['jenis']:<8}"
                f"{item['qty']:>8}"
                f"{'Rp {:,.0f}'.format(item['total']):>18}"
            )

    print("=" * 130)


def barang_masuk():

    tampilkan_produk()

    try:

        product_id = int(input("\nID Produk : "))
        qty = int(input("Qty Masuk : "))
        harga = float(input("Harga : "))
        keterangan = input("Keterangan : ")

        transaction_service.barang_masuk(
            product_id,
            qty,
            harga,
            keterangan
        )

        print("\n✅ Barang masuk berhasil.")

    except Exception as error:

        print(f"\n❌ {error}")


def barang_keluar():

    tampilkan_produk()

    try:

        product_id = int(input("\nID Produk : "))
        qty = int(input("Qty Keluar : "))
        harga = float(input("Harga Jual : "))
        keterangan = input("Keterangan : ")

        transaction_service.barang_keluar(
            product_id,
            qty,
            harga,
            keterangan
        )

        print("\n✅ Barang keluar berhasil.")

    except Exception as error:

        print(f"\n❌ {error}")


def lihat_transaksi():

    transaksi = transaction_service.get_all_transactions()

    tampilkan_transaksi(
        transaksi,
        "SEMUA TRANSAKSI"
    )


def transaksi_masuk():

    transaksi = transaction_service.get_transactions_by_type("IN")

    tampilkan_transaksi(
        transaksi,
        "TRANSAKSI BARANG MASUK"
    )


def transaksi_keluar():

    transaksi = transaction_service.get_transactions_by_type("OUT")

    tampilkan_transaksi(
        transaksi,
        "TRANSAKSI BARANG KELUAR"
    )


def transaksi_tanggal():

    tanggal = input(
        "\nMasukkan tanggal (YYYY-MM-DD) : "
    )

    transaksi = transaction_service.get_transactions_by_date(
        tanggal
    )

    tampilkan_transaksi(
        transaksi,
        f"TRANSAKSI {tanggal}"
    )


def menu():

    while True:

        print("\n" + "=" * 40)
        print("      TRANSACTION MENU")
        print("=" * 40)

        print("1. Barang Masuk")
        print("2. Barang Keluar")
        print("3. Semua Transaksi")
        print("4. Transaksi Barang Masuk")
        print("5. Transaksi Barang Keluar")
        print("6. Cari Berdasarkan Tanggal")
        print("0. Kembali")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            barang_masuk()

        elif pilih == "2":
            barang_keluar()

        elif pilih == "3":
            lihat_transaksi()

        elif pilih == "4":
            transaksi_masuk()

        elif pilih == "5":
            transaksi_keluar()

        elif pilih == "6":
            transaksi_tanggal()

        elif pilih == "0":
            break

        else:
            print("\n❌ Menu tidak tersedia.")