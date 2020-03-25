from db import db
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.results import ResultsModel


class Results(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lastName',
                        type=str
                        )
    parser.add_argument('raceName',
                        type=str
                        ) 
    parser.add_argument('time',
                        type=str
                        )                                        
    def get(self):
        sql = 'select * from results'
        result = db.engine.execute(sql)
        data = [row[0] for row in result]
        print (data)
        return {'data': data}


    def post(self, firstName):
        data = Results.parser.parse_args()
        
        item = ResultsModel(firstName, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201
    

