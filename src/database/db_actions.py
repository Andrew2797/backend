from uuid import uuid4
from typing import List

from src.database.models import Product, Review, User
from src.database.base import db


def get_products() -> List[Product]:
    #return db.get_or_404(db.session.query(Product))
    return db.session.query(Product).all()


def get_product(prod_id: str) -> Product:
    db.one_or_404(db.session.query(Product).where(Product.id == prod_id))
    #return db.session.query(Product).where(Product.id == prod_id).first()


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
    product = db.one_or_404(db.session.query(Product).where(Product,id == prod_id))
    product.name = name 
    product.description = description
    product.img_url = img_url
    product.price = price
    db.session.commit()
    return "Successful"


def del_product(prod_id: str) -> str:
    product = db.one_or_404(db.session.query(Product).where(Product.id == prod_id))
    db.session.delete(product)
    db.session.commit()
    return "Successful"


def add_review_by_product(reviwe: Review, prod_id: id) -> str:
    product = db.one_or_404(db.session.query(Product).where(Product.id == prod_id))
    product.reviews.append(product)
    db.session.commit()
    return "Successful" 


def get_reviews() -> List[Review]:
    return db.session.query(Review).all()


def get_review(review_id: str) -> Review:
    return db.one_or_404(db.session.query(Review).where(Review.id == review_id))


def edit_review(review_id: str, content: str, author: str) -> str:
    review = db.one_or_404(db.session.query(Review).where(Review.id == review_id))
    review.content = content
    review.author = author
    db.session.commit()
    return "Successful"


def del_review(review_id: str) -> str:
    review = db.one_or_404(db.session.query(Review).where(Review.id == review_id))
    db.session.delete(review)
    db.session.commit()
    return "Successful"


def add_user(
    email: str,
    password: str,
    first_name: str|None = None,
    last_name: str|None = None
) -> str:
    user = User(
        id=uuid4().hex,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )
    db.session.add(user)
    db.session.commit()
    return "Successful"

def get_user(user_id: str):
    return db.one_or_404(db.session.query(User))


def get_tokens(email: str, password:str) -> dict|None:
    user = db.one_or_404(db.session.query(User).where(User.email==email))
    return user.get_tokens(password)
