from db import db



class ResultsModel(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    raceName = db.Column(db.String(80))
    time = db.Column(db.String(80))
    # time = db.Column(db.Integer)

    def __init__(self, firstName, lastName,raceName,time):
        self.firstName = firstName
        self.lastName = lastName
        self.raceName = raceName
        self.passtimeword = time
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()