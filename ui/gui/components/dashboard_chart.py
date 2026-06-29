import customtkinter as ctk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from repositories.transaction_repository import TransactionRepository


class DashboardChart(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.repository = TransactionRepository()

        self.figure = Figure(figsize=(7, 3.5), dpi=100)

        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            self
        )

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.load_chart()

    def load_chart(self):

        self.ax.clear()

        data = self.repository.get_daily_transactions()

        tanggal = []
        total = []

        for item in data:

            tanggal.append(item["tanggal"])

            total.append(item["total"])

        self.ax.plot(
            tanggal,
            total,
            marker="o",
            linewidth=2
        )

        self.ax.set_title("Trend Transaksi Harian")

        self.ax.set_xlabel("Tanggal")

        self.ax.set_ylabel("Jumlah")

        self.ax.grid(True)

        self.figure.tight_layout()

        self.canvas.draw()