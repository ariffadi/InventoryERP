from reports.style import ReportStyle
from reports.table_builder import TableBuilder


class BaseSheet:

    def __init__(self, workbook, title):

        self.sheet = workbook.create_sheet(title)

        self.table = TableBuilder(self.sheet)

    def write_title(self, title):

        self.sheet["A1"] = title

        self.sheet["A1"].font = ReportStyle.TITLE_FONT

    def write_label_value(self, row, label, value):

        self.sheet[f"A{row}"] = label
        self.sheet[f"B{row}"] = value

        self.sheet[f"A{row}"].font = ReportStyle.LABEL_FONT

        self.sheet[f"A{row}"].border = ReportStyle.BORDER
        self.sheet[f"B{row}"].border = ReportStyle.BORDER

    def create_table(self, row, headers, data):

        self.table.create(
            row,
            headers,
            data
        )