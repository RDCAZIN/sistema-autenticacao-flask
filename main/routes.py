from flask import Blueprint
from flask_login import logout_user, login_required
from flask import redirect, url_for


main = Blueprint("main", __name__)

@main.route("/")
@login_required
def home():
    return "bem vindo ao teste 1"

