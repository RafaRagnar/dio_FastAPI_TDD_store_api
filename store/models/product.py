from store.models.base import CreateBaseModel
from store.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaseModel):
    """
    Classe de modelo para produtos.

    Esta classe herda de duas classes:
        * `ProductIn`: Classe do schema de entrada de produto, provavelmente
          contendo propriedades para dados como nome, descrição, preço, etc.
          (ver arquivo `store.schemas.product.py`).
        * `CreateBaseModel`: Classe base para modelos de criação de dados, 
          fornecendo campos como `id`, `created_at`, e `updated_at` (ver
          arquivo `store.models.base.py`).

    A classe `ProductModel` combina os campos do schema de entrada de produto
    (`ProductIn`) com os campos padronizados de criação (`CreateBaseModel`)
    para representar um modelo completo de produto na aplicação.
    """
    ...
