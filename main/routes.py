from flask import Blueprint


main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "bem vindo ao teste 1"