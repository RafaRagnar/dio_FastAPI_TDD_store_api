from store.usecases.product import product_usecase
from tests.conftest import product_in


async def test_usecases_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    # assert isinstance(result, ProductOut)
    assert result is None