from flask import Flask
from config import Config
from extensions import db, bcrypt,mail,login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    from main.routes import main
    from auth.routes import auth
    app.register_blueprint(main, url_prefix = "/main")
    app.register_blueprint(auth)
    login_manager.login_view = "auth.login"

    with app.app_context():
        db.create_all()

    return app

#criando app 
app = create_app()


if __name__ == "__main__":
    app.run(debug = True)