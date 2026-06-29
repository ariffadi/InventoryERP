import customtkinter as ctk

from ui.gui.theme import Theme
from ui.gui.main_window import MainWindow


def run():

    Theme.setup()

    app = MainWindow()

    app.mainloop()