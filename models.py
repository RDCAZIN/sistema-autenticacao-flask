from extensions import db
from flask_login import UserMixin
from extensions import login_manager

class Usuario(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(60), nullable = False, unique = True)
    senha = db.Column(db.Text, nullable = False)


#LOGIN 

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))