from flask_restful import Resource, reqparse
from models.riders import RidersModel
from db import db
from flask import jsonify


class Riders(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('firstname',
                        type=str,
                        required=True,
                        help="firstname field cannot be blank."
                        )
    parser.add_argument('lastname',
                        type=str,
                        required=True,
                        help="lastname field cannot be blank."
                        )
    # def get(self):
    #     data = {
    #     "raceName": "Bit Gobrin",
    #     "date": "03/01/2019",
    #      }
    #     return {'data': data}
    def get(self):
        sql = 'select * from riders'
        result = db.engine.execute(sql).fetchall()
        # data = [row[0] for row in result]
        # print (data)
        # return {'result': result}
        # return result.json()
        return jsonify({'result': [dict(row) for row in result]})



    def post(self):
        data = Riders.parser.parse_args()

        if RidersModel.find_by_firstName(data['firstname']):
            return {"message": "A user with that firstname already exists"}, 400

        riders = RidersModel(data['firstname'], data['lastname'])
        riders.save_to_db()

        return {"message": "rider created successfully."}, 201

# class RidersList(Resource):
#     def get(self):
#         return {'users': list(map(lambda x: x.json(), RidersModel.query.all()))}
