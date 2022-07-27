from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        11,
        "Minoxidil",
        "KIRKLAND SIGNATURE",
        "2022-02-01",
        "2023-02-01",
        "1CK1123",
        "instrucao 11",
    )

    assert product.id == 11
    assert product.nome_do_produto == "Minoxidil"
    assert product.nome_da_empresa == "KIRKLAND SIGNATURE"
    assert product.data_de_fabricacao == "2022-02-01"
    assert product.data_de_validade == "2023-02-01"
    assert product.numero_de_serie == "1CK1123"
    assert product.instrucoes_de_armazenamento == "instrucao 11"
