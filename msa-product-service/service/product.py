from sqlalchemy.orm import Session

from schema.product import ProductBase
from models.product import Product

# 상품 등록 처리
def register(db: Session, product: ProductBase):
    product = Product(**product.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    print(product)

    return product