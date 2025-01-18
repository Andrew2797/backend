import os

from dotenv import load_dotenv
from flask import Flask,jsonify
from flask_restful import Resource, Api

from src.database.models import db
from src.data import parse_data


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")
db.init_app(app)
api =Api(app)


#with app.app_context():
    #db.create_all()
    #parse_data.get_products()


class ProductAPI(Resource):
    def get(product_id: int=0):
        if product_id 
