from db import db


class RidersModel(db.Model):
    __tablename__ = 'riders'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_firstName(cls, firstname):
        return cls.query.filter_by(firstname=firstname).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
