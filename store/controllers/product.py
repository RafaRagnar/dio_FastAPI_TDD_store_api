from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4

from store.core.exceptions import NotFoundException
from store.schemas.product import (  # E501
    ProductIn,
    ProductOut,
    ProductUpdate,
    ProductUpdateOut,
)
from store.usecases.product import ProductUsecase

router = APIRouter(tags=["products"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    """
    Cria um novo produto.

    Args:
        body (ProductIn): Objeto contendo os dados do produto a ser criado,
        conforme o schema `ProductIn`.
        usecase (ProductUsecase): Dependência para acessar a lógica de negócio
        de produtos.

    Returns:
        ProductOut: Objeto contendo os dados do produto criado, conforme o
        schema `ProductOut`.

    Raises:
        HTTPException: Se a criação falhar, uma exceção HTTP será levantada
        com o código de status apropriado.
    """
    return await usecase.create(body=body)


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> ProductOut:
    """
    Obtém um produto específico por ID.

    Args:
        id (UUID4): ID do produto a ser obtido.
        usecase (ProductUsecase): Dependência para acessar a lógica de negócio
        de produtos.

    Returns:
        ProductOut: Objeto contendo os dados do produto obtido, conforme o
        schema `ProductOut`.

    Raises:
        HTTPException: Se o produto não for encontrado, uma exceção HTTP será
        levantada com o código de status 404 Not Found.
    """
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message) from exc


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: ProductUsecase = Depends()) -> List[ProductOut]:
    """
    Lista todos os produtos.

    Args:
        usecase (ProductUsecase): Dependência para acessar a lógica de negócio
        de produtos.

    Returns:
        List[ProductOut]: Lista de objetos contendo os dados de cada produto,
        conforme o schema `ProductOut`.
    """
    return await usecase.query()


@router.patch(path="/{id}", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductUpdateOut:
    """
    Atualiza um produto existente.

    Args:
        id (UUID4): ID do produto a ser atualizado.
        body (ProductUpdate): Objeto contendo os dados de atualização do
        produto, conforme o schema `ProductUpdate`.
        usecase (ProductUsecase): Dependência para acessar a lógica de negócio
        de produtos.

    Returns:
        ProductUpdateOut: Objeto contendo os dados do produto atualizado,
        conforme o schema `ProductUpdateOut`.

    Raises:
        HTTPException: Se o produto não for encontrado, uma exceção HTTP será
        levantada com o código de status 404 Not Found.
    """
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message) from exc


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> None:
    """
    Exclui um produto específico por ID.

    Args:
        id (UUID4): ID do produto a ser excluído.
        usecase (ProductUsecase): Dependência para acessar a lógica de negócio
        de produtos.

    Raises:
        HTTPException: Se o produto não for encontrado, uma exceção HTTP será
        levantada com o código de status 404 Not Found.
    """
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=exc.message) from exc
