from openpyxl.chart import BarChart
from openpyxl.chart import Reference


class ChartSheet:

    def __init__(self, workbook):

        self.workbook = workbook

    def build(self):

        sheet = self.workbook.create_sheet("Charts")

        dashboard = self.workbook["Dashboard"]

        chart = BarChart()

        data = Reference(

            dashboard,

            min_col=2,

            min_row=5,

            max_row=10

        )

        category = Reference(

            dashboard,

            min_col=1,

            min_row=5,

            max_row=10

        )

        chart.add_data(

            data,

            titles_from_data=False

        )

        chart.set_categories(category)

        chart.title = "Inventory Dashboard"

        chart.height = 10

        chart.width = 18

        sheet.add_chart(

            chart,

            "B2"

        )