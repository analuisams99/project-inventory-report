from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list: list):
        simple_report = super().generate(list)
        return (
            f"{simple_report}\n"
            f"{self.get_products_stocked_by_company(self, list)}"
        )

    def get_products_stocked_by_company(self, list):
        all_companies = super().get_all_companies(list)
        companies_inventory = Counter(all_companies).most_common()
        result = "Produtos estocados por empresa:\n"
        for data in companies_inventory:
            result += f"- {data[0]}: {data[1]}\n"
        return result
