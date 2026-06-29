import customtkinter as ctk
from tkinter import messagebox

from services.category_service import CategoryService
from ui.gui.theme import Theme


class ProductDialog(ctk.CTkToplevel):

    def __init__(
        self,
        master,
        title="Tambah Produk"
    ):
        super().__init__(master)

        self.title(title)
        self.geometry("500x560")
        self.resizable(False, False)

        self.transient(master)
        self.grab_set()

        self.category_service = CategoryService()

        self.result = None
        self.product_id = None

        self.category_map = {}
        self.id_to_name = {}

        self.create_widgets()

        self.after(100, self.kode.focus_set)

        self.bind("<Return>", lambda e: self.save())
        self.bind("<Escape>", lambda e: self.destroy())

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

        # -------------------------------------------------

        ctk.CTkLabel(
            container,
            text="Kode Produk",
            font=Theme.FONT_NORMAL
        ).pack(anchor="w")

        self.kode = ctk.CTkEntry(container)

        self.kode.pack(
            fill="x",
            pady=(5, 15)
        )

        # -------------------------------------------------

        ctk.CTkLabel(
            container,
            text="Nama Produk",
            font=Theme.FONT_NORMAL
        ).pack(anchor="w")

        self.nama = ctk.CTkEntry(container)

        self.nama.pack(
            fill="x",
            pady=(5, 15)
        )

        # -------------------------------------------------

        ctk.CTkLabel(
            container,
            text="Kategori",
            font=Theme.FONT_NORMAL
        ).pack(anchor="w")

        kategori = self.category_service.get_all_categories()

        self.category_map = {
            item["nama"]: item["id"]
            for item in kategori
        }

        self.id_to_name = {
            item["id"]: item["nama"]
            for item in kategori
        }

        values = list(self.category_map.keys())

        if not values:
            values = ["-"]

        self.category_box = ctk.CTkComboBox(
            container,
            values=values,
            state="readonly"
        )

        if values:
            self.category_box.set(values[0])

        self.category_box.pack(
            fill="x",
            pady=(5, 15)
        )

        # -------------------------------------------------

        ctk.CTkLabel(
            container,
            text="Stok Awal",
            font=Theme.FONT_NORMAL
        ).pack(anchor="w")

        self.stok_awal = ctk.CTkEntry(container)

        self.stok_awal.insert(0, "0")

        self.stok_awal.pack(
            fill="x",
            pady=(5, 15)
        )

        # -------------------------------------------------

        ctk.CTkLabel(
            container,
            text="Stok Minimum",
            font=Theme.FONT_NORMAL
        ).pack(anchor="w")

        self.stok_minimum = ctk.CTkEntry(container)

        self.stok_minimum.insert(0, "0")

        self.stok_minimum.pack(
            fill="x",
            pady=(5, 15)
        )

        # -------------------------------------------------

        ctk.CTkLabel(
            container,
            text="Harga",
            font=Theme.FONT_NORMAL
        ).pack(anchor="w")

        self.harga = ctk.CTkEntry(container)

        self.harga.insert(0, "0")

        self.harga.pack(
            fill="x",
            pady=(5, 25)
        )

        # -------------------------------------------------

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

    # =====================================================

    def set_data(self, data):

        self.product_id = data.get("id")

        self.kode.delete(0, "end")
        self.kode.insert(0, str(data.get("kode", "")))

        self.nama.delete(0, "end")
        self.nama.insert(0, str(data.get("nama", "")))

        kategori_id = data.get("kategori_id")

        if kategori_id in self.id_to_name:
            self.category_box.set(
                self.id_to_name[kategori_id]
            )

        self.stok_awal.delete(0, "end")
        self.stok_awal.insert(
            0,
            str(data.get("stok_awal", 0))
        )

        self.stok_minimum.delete(0, "end")
        self.stok_minimum.insert(
            0,
            str(data.get("stok_minimum", 0))
        )

        self.harga.delete(0, "end")
        self.harga.insert(
            0,
            str(data.get("harga", 0))
        )

    # =====================================================

    def validate(self):

        if not self.kode.get().strip():
            messagebox.showwarning(
                "Validasi",
                "Kode produk wajib diisi."
            )
            self.kode.focus_set()
            return False

        if not self.nama.get().strip():
            messagebox.showwarning(
                "Validasi",
                "Nama produk wajib diisi."
            )
            self.nama.focus_set()
            return False

        if self.category_box.get() not in self.category_map:
            messagebox.showwarning(
                "Validasi",
                "Kategori belum dipilih."
            )
            return False

        try:
            int(self.stok_awal.get())
        except Exception:
            messagebox.showwarning(
                "Validasi",
                "Stok awal harus berupa angka."
            )
            return False

        try:
            int(self.stok_minimum.get())
        except Exception:
            messagebox.showwarning(
                "Validasi",
                "Stok minimum harus berupa angka."
            )
            return False

        try:
            float(self.harga.get())
        except Exception:
            messagebox.showwarning(
                "Validasi",
                "Harga harus berupa angka."
            )
            return False

        return True

    # =====================================================

    def save(self):

        if not self.validate():
            return

        self.result = {

            "id": self.product_id,

            "kode": self.kode.get().strip(),

            "nama": self.nama.get().strip(),

            "kategori_id": self.category_map[
                self.category_box.get()
            ],

            "stok_awal": int(self.stok_awal.get()),

            "stok_minimum": int(
                self.stok_minimum.get()
            ),

            "harga": float(self.harga.get())

        }

        self.destroy()