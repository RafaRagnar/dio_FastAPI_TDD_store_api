def product_data():
    """
    Esta função de fábrica retorna um dicionário representando dados de um
    único produto.

    Os dados incluem:
        * name (str): Nome do produto.
        * quantity (int): Quantidade em estoque.
        * price (str): Preço do produto (formato string).
        * status (bool): Indica se o produto está ativo.

    Este dicionário pode ser utilizado para criar instâncias de modelos de
    produto ou para fornecer dados de exemplo para testes.
    """
    return {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


def products_data():
    """
    Esta função de fábrica retorna uma lista de dicionários representando dados
    de vários produtos.

    Cada dicionário na lista segue o mesmo formato da função `product_data`.

    Esta lista pode ser utilizada para criar vários produtos de uma só vez ou
    para fornecer dados de exemplo para testes.
    """
    return [
        {
            "name": "Iphone 11 Pro Max",
            "quantity": 20,
            "price": "4.500",
            "status": True
            },
        {
            "name": "Iphone 12 Pro Max",
            "quantity": 15,
            "price": "5.500",
            "status": True
            },
        {
            "name": "Iphone 13 Pro Max",
            "quantity": 5,
            "price": "6.500",
            "status": True
            },
        {
            "name": "Iphone 15 Pro Max",
            "quantity": 3,
            "price": "10.500",
            "status": False,
        },
    ]
