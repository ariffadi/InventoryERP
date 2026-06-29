import customtkinter as ctk
from tkinter import messagebox

from ui.gui.theme import Theme

from ui.gui.controllers.product_controller import ProductController


class TransactionDialog(ctk.CTkToplevel):

    def __init__(
        self,
        master,
        title="Tambah Transaksi"
    ):

        super().__init__(master)

        self.title(title)

        self.geometry("520x620")

        self.resizable(False, False)

        self.transient(master)

        self.grab_set()

        self.product_controller = ProductController()

        self.result = None

        self.transaction_id = None

        self.product_map = {}

        self.id_to_name = {}

        self.create_widgets()

        self.after(
            100,
            self.qty.focus_set
        )

        self.bind(
            "<Return>",
            lambda e: self.save()
        )

        self.bind(
            "<Escape>",
            lambda e: self.destroy()
        )

    # =====================================================

    def create_widgets(self):

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # =====================================================
        # PRODUCT
        # =====================================================

        ctk.CTkLabel(
            container,
            text="Produk",
            font=Theme.FONT_NORMAL
        ).pack(
            anchor="w"
        )

        products = self.product_controller.get_product_list()

        self.product_map = {}

        self.id_to_name = {}

        values = []

        for item in products:

            text = f"{item['kode']} - {item['nama']}"

            values.append(text)

            self.product_map[text] = item["id"]

            self.id_to_name[item["id"]] = text

        if not values:

            values.append("-")

        self.product_box = ctk.CTkComboBox(
            container,
            values=values,
            state="readonly"
        )

        self.product_box.pack(
            fill="x",
            pady=(5, 15)
        )

        self.product_box.set(values[0])

        # =====================================================
        # JENIS
        # =====================================================

        ctk.CTkLabel(
            container,
            text="Jenis",
            font=Theme.FONT_NORMAL
        ).pack(
            anchor="w"
        )

        self.jenis = ctk.CTkComboBox(
            container,
            values=[
                "IN",
                "OUT"
            ],
            state="readonly"
        )

        self.jenis.pack(
            fill="x",
            pady=(5, 15)
        )

        self.jenis.set("IN")

        # =====================================================
        # QTY
        # =====================================================

        ctk.CTkLabel(
            container,
            text="Qty",
            font=Theme.FONT_NORMAL
        ).pack(
            anchor="w"
        )

        self.qty = ctk.CTkEntry(
            container
        )

        self.qty.pack(
            fill="x",
            pady=(5, 15)
        )

        self.qty.insert(
            0,
            "1"
        )

        self.qty.bind(
            "<KeyRelease>",
            self.calculate_total
        )

        # =====================================================
        # HARGA
        # =====================================================

        ctk.CTkLabel(
            container,
            text="Harga",
            font=Theme.FONT_NORMAL
        ).pack(
            anchor="w"
        )

        self.harga = ctk.CTkEntry(
            container
        )

        self.harga.pack(
            fill="x",
            pady=(5, 15)
        )

        self.harga.insert(
            0,
            "0"
        )

        self.harga.bind(
            "<KeyRelease>",
            self.calculate_total
        )
                # =====================================================
        # TOTAL
        # =====================================================

        ctk.CTkLabel(
            container,
            text="Total",
            font=Theme.FONT_NORMAL
        ).pack(
            anchor="w"
        )

        self.total = ctk.CTkEntry(
            container,
            state="readonly"
        )

        self.total.pack(
            fill="x",
            pady=(5, 15)
        )

        self.total.configure(state="normal")
        self.total.insert(0, "0")
        self.total.configure(state="readonly")

        # =====================================================
        # KETERANGAN
        # =====================================================

        ctk.CTkLabel(
            container,
            text="Keterangan",
            font=Theme.FONT_NORMAL
        ).pack(
            anchor="w"
        )

        self.keterangan = ctk.CTkTextbox(
            container,
            height=80
        )

        self.keterangan.pack(
            fill="x",
            pady=(5, 20)
        )

        # =====================================================
        # BUTTON
        # =====================================================

        button_frame = ctk.CTkFrame(
            container,
            fg_color="transparent"
        )

        button_frame.pack(fill="x")

        ctk.CTkButton(
            button_frame,
            text="Batal",
            width=120,
            command=self.destroy
        ).pack(
            side="left"
        )

        ctk.CTkButton(
            button_frame,
            text="Simpan",
            width=120,
            command=self.save
        ).pack(
            side="right"
        )

        self.calculate_total()

        # =====================================================

    def calculate_total(self, event=None):

        try:

            qty = int(self.qty.get())

        except Exception:

            qty = 0

        try:

            harga = float(self.harga.get())

        except Exception:

            harga = 0

        total = qty * harga

        self.total.configure(state="normal")

        self.total.delete(0, "end")

        self.total.insert(
            0,
            f"{total:,.0f}"
        )

        self.total.configure(state="readonly")
    
        # =====================================================

    def set_data(self, data):

        self.transaction_id = data["id"]

        if data["product_id"] in self.id_to_name:

            self.product_box.set(
                self.id_to_name[data["product_id"]]
            )

        self.jenis.set(
            data["jenis"]
        )

        self.qty.delete(0, "end")
        self.qty.insert(
            0,
            str(data["qty"])
        )

        self.harga.delete(0, "end")
        self.harga.insert(
            0,
            str(data["harga"])
        )

        self.keterangan.delete(
            "1.0",
            "end"
        )

        self.keterangan.insert(
            "1.0",
            data["keterangan"] or ""
        )

        self.calculate_total()

        # =====================================================

    def validate(self):

        if self.product_box.get() not in self.product_map:

            messagebox.showwarning(
                "Validasi",
                "Produk belum dipilih."
            )

            return False

        try:

            qty = int(
                self.qty.get()
            )

            if qty <= 0:

                raise Exception()

        except Exception:

            messagebox.showwarning(
                "Validasi",
                "Qty tidak valid."
            )

            return False

        try:

            harga = float(
                self.harga.get()
            )

            if harga <= 0:

                raise Exception()

        except Exception:

            messagebox.showwarning(
                "Validasi",
                "Harga tidak valid."
            )

            return False

        return True
    
        # =====================================================

    def save(self):

        if not self.validate():
            return

        self.result = {

            "id": self.transaction_id,

            "product_id": self.product_map[
                self.product_box.get()
            ],

            "jenis": self.jenis.get(),

            "qty": int(
                self.qty.get()
            ),

            "harga": float(
                self.harga.get()
            ),

            "keterangan": self.keterangan.get(
                "1.0",
                "end"
            ).strip()

        }

        self.destroy()