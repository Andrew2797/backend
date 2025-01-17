import logging
import sys

from requests_html import HTMLSession

from src.database.models import Product, db


URL = "https://rozetka.com.ua/news-articles-promotions/promotions/275149_sale_lego/"
LOG = logging.getLogger(__name__)
logging.basicConfig(logging.INFO, stream=sys.stdout)


def get_products(url):
    session = HTMLSession
    response = session.get(url)

    products = response.html.xpath('//p[@class="goods-tile__title ng-star-inserted"]/@href')
    for i, product in enumerate(products, start=1):
        LOG.info(f"Товар номер {i} відправлено на опрацювання")
        save_product(product)


def save_product(url):
    session = HTMLSession()
    response = session.get(url)

    name = response.html.xpath('//p[@class="title__font ng-star-inserted"]/text()')[0]
    img_url = response.html.xpath('//div[@class="main-slider__wrap ng-star-inserted"]//img/@src')[0]
    description = response.html.xpath('//div[@class="rich ng-star-inserted"]//text()')
    description = "\n".join(description)
    price = response.html.xpath('//p[contains(@class, "product-price__big")]/text()')[0].replace("&nbsp;", "")
    product = Product(
        name=name
        img_url=img_url
        description=description
        price=price
    )
    
        
    

    db.session.add(product)
    db.session.commit()
    LOG.info(F"Товар '{name}' успішно збережено")
