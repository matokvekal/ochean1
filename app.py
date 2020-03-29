import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.results import Results
from resources.races import RaceList
from resources.riders import Riders

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
# app.secret_key = 'jowdkedfmwfewise'
api = Api(app)

#temp only for wil local
@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
# api.add_resource(UserList, '/users')
api.add_resource(Results, '/results')
api.add_resource(RaceList, '/races')
api.add_resource(Riders, '/riders')


if __name__ == '__main__':
    # from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
