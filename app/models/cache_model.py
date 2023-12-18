from app import db

class Cache(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(50), unique=True, nullable=False)
    data = db.Column(db.String, nullable=False)
