import tkinter.ttk as ttk

import customtkinter as ctk


class DataTable(ctk.CTkFrame):

    def __init__(
        self,
        master,
        columns,
        height=10
    
    ):
        super().__init__(master)

        self.columns = columns
        self._sort_column = None
        self._sort_reverse = False

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=height
        )

        for column in columns:

            self.tree.heading(
                column,
                text=column,
                command=lambda c=column: self.sort_by(c)
            )

            self.tree.column(
                column,
                width=140,
                anchor="center",
                stretch=True
            )

        # =====================================================
        # Scrollbars
        # =====================================================

        self.v_scroll = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview
        )

        self.h_scroll = ttk.Scrollbar(
            self,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=self.v_scroll.set,
            xscrollcommand=self.h_scroll.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.v_scroll.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.h_scroll.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # =====================================================

    def clear(self):

        self.tree.delete(*self.tree.get_children())

    # =====================================================

    def insert(self, values):

        self.tree.insert(
            "",
            "end",
            values=values
        )

    # =====================================================

    def set_data(self, rows):

        self.clear()

        for row in rows:
            self.insert(row)

    # =====================================================

    def get_selected(self):

        selected = self.tree.selection()

        if not selected:
            return None

        return self.tree.item(
            selected[0]
        )["values"]

    # =====================================================

    def get_selected_id(self):

        values = self.get_selected()

        if values is None:
            return None

        return values[0]
    
        # =====================================================

    def get_selected_row(self):

        selected = self.tree.selection()

        if not selected:
            return None

        return self.tree.item(selected[0])
    
        # =====================================================

    def remove_selected(self):

        selected = self.tree.selection()

        if selected:

            self.tree.delete(selected[0])

        # =====================================================

    def select_first(self):

        self.focus_first()

        # =====================================================

    def is_empty(self):

        return len(self.tree.get_children()) == 0

    # =====================================================

    def focus_first(self):

        children = self.tree.get_children()

        if not children:
            return

        self.tree.focus(children[0])
        self.tree.selection_set(children[0])

    # =====================================================

    def sort_by(self, column):

        rows = [
            (
                self.tree.set(item, column),
                item
            )
            for item in self.tree.get_children("")
        ]

        rows.sort(
            reverse=self._sort_reverse
        )

        for index, (_, item) in enumerate(rows):

            self.tree.move(
                item,
                "",
                index
            )

        self._sort_reverse = not self._sort_reverse

        # =====================================================

    # =====================================================

    def set_columns(self, columns):

        self.columns = columns

        self.tree.configure(
            columns=columns
        )

        self.tree["show"] = "headings"

        for column in columns:

            self.tree.heading(
                column,
                text=column,
                command=lambda c=column: self.sort_by(c)
            )

            self.tree.column(
                column,
                width=140,
                anchor="center",
                stretch=True
            )

        # =====================================================

    def set_column_width(
        self,
        column,
        width
    ):

        self.tree.column(
            column,
            width=width
        )

        # =====================================================

    def auto_size(self):

        for column in self.columns:

            width = max(
                120,
                len(column) * 12
            )

            self.tree.column(
                column,
                width=width
            )

        # =====================================================

    def clear_selection(self):

        self.tree.selection_remove(
            self.tree.selection()
        )

        # =====================================================

    def row_count(self):

        return len(
            self.tree.get_children()
        )
    
    

    def refresh(self):

        self.tree.update_idletasks()