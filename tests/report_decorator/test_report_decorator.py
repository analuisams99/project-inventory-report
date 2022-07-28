from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


list_mock = [
    {
        "data_de_fabricacao": "2022-07-02",
        "data_de_validade": "2022-08-02",
        "nome_da_empresa": "Bombril",
    },
    {
        "data_de_fabricacao": "2022-07-03",
        "data_de_validade": "2022-07-31",
        "nome_da_empresa": "Bombril",
    },
    {
        "data_de_fabricacao": "2022-07-04",
        "data_de_validade": "2022-07-12",
        "nome_da_empresa": "Bombril",
    },
    {
        "data_de_fabricacao": "2022-07-05",
        "data_de_validade": "2022-07-14",
        "nome_da_empresa": "Assolan",
    },
]

expected_return_simple = (
    "\033[32mData de fabricação mais antiga:\033[0m "
    "\033[36m2022-07-02\033[0m\n"
    "\033[32mData de validade mais próxima:\033[0m "
    "\033[36m2022-07-12\033[0m\n"
    "\033[32mEmpresa com mais produtos:\033[0m "
    "\033[31mBombril\033[0m"
)

expected_return_complete = (
    f"{expected_return_simple}\n"
    f"Produtos estocados por empresa:\n"
    f"- Bombril: 3\n"
    f"- Assolan: 1\n"
)


def test_decorar_relatorio():
    assert (
        ColoredReport(SimpleReport).generate(list_mock)
        == expected_return_simple
    )
    assert (
        ColoredReport(CompleteReport).generate(list_mock)
        == expected_return_complete
    )
