class SimpleReport:
    @classmethod
    def generate(self, list: list):
        return (
            f"Data de fabricação mais antiga: "
            f"{self.oldest_manufacturing_date(list)}\n"
            "Data de validade mais próxima: "
            f"{self.closest_expiration_date(list)}\n"
            f"Empresa com mais produtos: "
            f"{self.get_company_with_more_products(self, list)}"
        )

    def get_all_companies(list):
        return [row["nome_da_empresa"] for row in list]

    def oldest_manufacturing_date(list):
        manufacturing_date = [row["data_de_fabricacao"] for row in list]
        return min(manufacturing_date)

    def closest_expiration_date(list):
        expiration_date = [row["data_de_validade"] for row in list]
        return min(expiration_date)

    def get_company_with_more_products(self, list):
        company_list = self.get_all_companies(list)
        return max(set(company_list), key=company_list.count)
