from flask import Blueprint,redirect,render_template,url_for,flash,request
from auth.forms import RegistroForm, LoginForm, EmailForm,  SenhaForm
from models import Usuario
from extensions import db,bcrypt,mail
from sqlalchemy import or_
from config import Config
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from flask_login import login_user,logout_user


auth = Blueprint("auth", __name__)

#configurando o envio
enviar_email = URLSafeTimedSerializer(Config.SECRET_KEY)

@auth.route("/", methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter(or_(Usuario.usuario == form.identificador.data, Usuario.email == form.identificador.data)).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario)
            return redirect(url_for('main.home'))
        else:
            flash("Usuario ou Senha invalido", "erro")
    return render_template("login.html", form = form)


@auth.route("/cadastrar", methods = ["GET", "POST"])
def cadastrar():
    form = RegistroForm()
    if form.validate_on_submit():
        novo_usuario = Usuario(
            usuario = form.nome.data,
            email = form.email.data,
            senha = bcrypt.generate_password_hash(form.senha.data).decode("utf-8")
        )

        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template("cadastro.html", form = form)


@auth.route("/confirmar_email", methods = ["GET", "POST"])
def confirmar_email():
    form = EmailForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email = form.email.data).first()
        if usuario:
            print("Usuário encontrado:", usuario)
            token = enviar_email.dumps(usuario.email)
            msg = Message(
                "Troca senha",
                sender="ronaldteste2017@gmail.com",
                recipients=[usuario.email]
            )
            msg.body = url_for("auth.resetar_senha", token=token, _external=True)
            mail.send(msg)
            flash("Email enviado com sucesso, veja sua caixa de entrada")
        else:
            flash("EMAIL NÃO ENCONTRADO", "erro")        
    return render_template("confirmar_email.html", form = form)


@auth.route("/resetar_senha",methods = ["GET", "POST"])
def resetar_senha():
    form = SenhaForm()
    token = request.args.get("token")
    try:
        email = enviar_email.loads(token , max_age=1800)
        if form.validate_on_submit():
            usuario = Usuario.query.filter_by(email = email).first()
            if usuario:
                usuario.senha = bcrypt.generate_password_hash(form.senha.data).decode("utf-8")
                db.session.commit()
                return redirect(url_for('auth.login'))            
        return render_template("trocar_senha.html" , form = form , token = token)
    except Exception as e:
        print("ERRO:", e)
        flash("O seu Link expirou, solicite outro", "erro")
        return redirect(url_for('auth.confirmar_email'))
@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


        