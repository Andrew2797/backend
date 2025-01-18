from uuid import uuid4
from typing import List

from src.database.models import db, Product, Review


def get_products() -> List[Product]:
    return db.session.query(Product).all()


def get_product(prod_id: str) -> Product:
    return db.session.query(Product).where(Product.id == prod_id).first()


def add_product(
        name: str,
        description: str,
        img_url: str,
        price: float
) -> str:
    product = Product(
    id=uuid4().hex,
    name=name,
    description=description,
    img_url=img_url,
    price=price
    )
    db.session.add(product)
    db.session.commit()
    return product.id


def edit_product(
        prod_id: str,
        name: str,
        description: str,
        img_url: str,
        price: float
) -> str:
    product = db.session.query(Product).where(Product,id == prod_id).first()
    product.name = name 
    product.description = description
    product.img_url = img_url
    product.price = price
    db.session.commit()
    return "Successful"


def del_product(prod_id: str) -> str:
    product = db.session.query(Product).where(Product.id == prod_id).first()
    db.session.delete(product)
    db.session.commit()
    return "Successful"


def add_review_by_product(reviwe: Review, prod_id: id) -> str:
    product = db.session.query(Product).where(Product.id == prod_id).first()
    product.reviews.append(product)
    db.session.commit()
    return "Successful" 

