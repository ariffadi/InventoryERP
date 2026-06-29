from services.dashboard_service import DashboardService
from charts.dashboard_chart import DashboardChart

dashboard = DashboardService()
chart = DashboardChart()

def critical_stock():

    data = dashboard.get_critical_products()

    print("\n" + "=" * 90)
    print("CRITICAL STOCK REPORT".center(90))
    print("=" * 90)

    print(
        f"{'ID':<5}"
        f"{'KODE':<12}"
        f"{'NAMA':<30}"
        f"{'STOK':>10}"
        f"{'MINIMUM':>12}"
        f"{'STATUS':>18}"
    )

    print("-" * 90)

    if not data:
        print("Tidak ada produk yang menipis atau habis.")

    else:

        for item in data:

            print(
                f"{item['id']:<5}"
                f"{item['kode']:<12}"
                f"{item['nama']:<30}"
                f"{item['stok']:>10}"
                f"{item['minimum']:>12}"
                f"{item['status']:>18}"
            )

    print("=" * 90)

    input("\nTekan ENTER untuk kembali...")

def top_selling():

    data = dashboard.get_top_selling_products()

    print("\n" + "=" * 80)
    print("TOP 10 PRODUK TERLARIS".center(80))
    print("=" * 80)

    print(
        f"{'NO':<5}"
        f"{'KODE':<12}"
        f"{'NAMA':<35}"
        f"{'TOTAL TERJUAL':>20}"
    )

    print("-" * 80)

    nomor = 1

    for item in data:

        print(
            f"{nomor:<5}"
            f"{item['kode']:<12}"
            f"{item['nama']:<35}"
            f"{item['terjual']:>20}"
        )

        nomor += 1

    print("=" * 80)

    input("\nTekan ENTER...")

def inventory_value():

    data = dashboard.get_dashboard()

    print("\n" + "=" * 60)
    print("INVENTORY VALUE".center(60))
    print("=" * 60)

    print()

    print(f"Nilai Persediaan Saat Ini")

    print()

    print(f"Rp {data['inventory_value']:,.0f}")

    print()

    print("=" * 60)

    input("\nTekan ENTER...")

def menu():

    while True:

        data = dashboard.get_dashboard()

        print("\n" + "=" * 60)
        print("INVENTORY ERP DASHBOARD".center(60))
        print("=" * 60)

        print(f"📦 Total Produk      : {data['total_produk']}")
        print(f"📥 Barang Masuk      : {data['barang_masuk']}")
        print(f"📤 Barang Keluar     : {data['barang_keluar']}")
        print(f"📦 Total Stok        : {data['total_stok']}")
        print(f"💰 Total Omzet       : Rp {data['omzet']:,.0f}")
        print(f"⚠ Produk Menipis    : {data['produk_menipis']}")
        print(f"❌ Produk Habis      : {data['produk_habis']}")

        print("\n" + "=" * 60)
        print("1. Grafik Stok")
        print("2. Grafik Barang Masuk vs Keluar")
        print("3. Pie Chart Status")
        print("4. Trend Transaksi")
        print("5. Critical Stock Report")
        print("6. Top 10 Produk Terlaris")
        print("7. Inventory Value")
        print("0. Kembali")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            chart.show_stock_chart()

        elif pilih == "2":
            chart.show_transaction_chart()

        elif pilih == "3":
            chart.show_status_chart()

        elif pilih == "4":
            chart.show_transaction_trend()
        
        elif pilih == "5":
            critical_stock()
        
        elif pilih == "6":
            top_selling()

        elif pilih == "7":
            inventory_value()

        elif pilih == "0":
            break

        else:
            print("\n❌ Menu tidak tersedia.")