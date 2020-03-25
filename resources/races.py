from db import db
from sqlalchemy import text
from flask_restful import Resource
from models.store import StoreModel


class RaceList(Resource):
    def get(self):
        data = {
        "raceName": "Bit Gobrin",
        "date": "03/01/2019",
         }
        return {'data': data}

