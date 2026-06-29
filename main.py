from database.migrate import migrate

from ui.console.product_menu import menu as product_menu
from ui.console.transaction_menu import menu as transaction_menu
from ui.console.dashboard_menu import menu as dashboard_menu

from ui.gui.app import run as run_gui


def console_mode():

    while True:

        print("\n" + "=" * 45)
        print("      INVENTORY ERP SYSTEM")
        print("=" * 45)

        print("1. Kelola Produk")
        print("2. Transaksi")
        print("3. Dashboard")
        print("4. GUI Mode")
        print("0. Keluar")

        pilih = input("\nPilih Menu : ")

        if pilih == "1":
            product_menu()

        elif pilih == "2":
            transaction_menu()

        elif pilih == "3":
            dashboard_menu()

        elif pilih == "4":
            run_gui()

        elif pilih == "0":
            print("\nTerima kasih.")
            break

        else:
            print("\n❌ Menu tidak tersedia.")


def main():

    migrate()

    console_mode()


if __name__ == "__main__":
    main()