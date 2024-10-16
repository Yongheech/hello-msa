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


# 상품 목록 조회
def productlist(db: Session):
    return db.query(Product.name, Product.price,
                    Product.regdate, Product.pno)\
                    .order_by(Product.pno.desc()).all()

# 상품 상세 조회
def productone(db: Session, pno: int):
    return db.query(Product).filter(Product.pno == pno).first()