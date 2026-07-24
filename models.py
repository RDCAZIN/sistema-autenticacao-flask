from extensions import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(60), nullable = False, unique = True)
    senha = db.Column(db.Text, nullable = False)
