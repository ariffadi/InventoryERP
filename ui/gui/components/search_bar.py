import customtkinter as ctk


class SearchBar(ctk.CTkFrame):

    def __init__(
        self,
        master,
        command=None
    ):

        super().__init__(master)

        self.command = command

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Cari produk..."
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.entry.bind(
            "<KeyRelease>",
            self.on_key_release
        )

        self.entry.bind(
            "<Return>",
            lambda e: self.execute()
        )

        self.entry.bind(
            "<Escape>",
            lambda e: self.clear()
        )

        self.button = ctk.CTkButton(
            self,
            text="Cari",
            width=120,
            command=self.execute
        )

        self.button.pack(
            side="right"
        )

    # ==================================================

    def execute(self):

        if self.command:
            self.command()

    # ==================================================

    def on_key_release(self, event):

        if self.command:
            self.command()

    # ==================================================

    def get(self):

        return self.entry.get().strip()

    # ==================================================

    def clear(self):

        self.entry.delete(
            0,
            "end"
        )

        if self.command:
            self.command()