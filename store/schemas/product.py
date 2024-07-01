from typing import Optional

from pydantic import BaseModel, Field

from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    ...


class ProductUpdate(ProductBase):
    quantity: Optional[int | None] = Field(None, description="Product quantity")
    price: Optional[float | None] = Field(None, description="Product price")
    status: Optional[bool | None] = Field(None, description="Product status")


class ProductUpdateOut(ProductUpdate):
    ...
    ...
