import customtkinter as ctk

from repositories.transaction_repository import TransactionRepository

from ui.gui.theme import Theme


class RecentTransaction(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.repository = TransactionRepository()

        self.create_title()

        self.create_table()

    def create_title(self):

        title = ctk.CTkLabel(
            self,
            text="Recent Transactions",
            font=Theme.FONT_SUBTITLE
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(15,10)
        )

    def create_table(self):

        transactions = self.repository.get_all()[:10]

        header = ctk.CTkFrame(self)

        header.pack(
            fill="x",
            padx=10
        )

        ctk.CTkLabel(
            header,
            text="Tanggal",
            width=120
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            header,
            text="Produk",
            width=220
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            header,
            text="Jenis",
            width=80
        ).pack(
            side="left"
        )

        ctk.CTkLabel(
            header,
            text="Qty",
            width=60
        ).pack(
            side="left"
        )

        for trx in transactions:

            row = ctk.CTkFrame(self)

            row.pack(
                fill="x",
                padx=10,
                pady=2
            )

            ctk.CTkLabel(
                row,
                text=trx["tanggal"][:10],
                width=120
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                row,
                text=trx["nama"],
                width=220,
                anchor="w"
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                row,
                text=trx["jenis"],
                width=80
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                row,
                text=str(trx["qty"]),
                width=60
            ).pack(
                side="left"
            )