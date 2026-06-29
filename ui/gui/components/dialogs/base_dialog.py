import customtkinter as ctk


class BaseDialog(ctk.CTkToplevel):

    WIDTH = 420
    HEIGHT = 220

    def __init__(
        self,
        master,
        title="Dialog",
        width=None,
        height=None
    ):

        super().__init__(master)

        width = width or self.WIDTH
        height = height or self.HEIGHT

        self.title(title)

        self.geometry(
            f"{width}x{height}"
        )

        self.resizable(False, False)

        self.transient(master)

        self.grab_set()

        self.center_window()

        self.bind(
            "<Escape>",
            lambda e: self.close()
        )

        # ===========================================

        self.container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ===============================================

    def center_window(self):

        self.update_idletasks()

        width = self.winfo_width()
        height = self.winfo_height()

        x = (
            self.winfo_screenwidth() // 2
            - width // 2
        )

        y = (
            self.winfo_screenheight() // 2
            - height // 2
        )

        self.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # ===============================================

    def close(self):

        self.grab_release()

        self.destroy()