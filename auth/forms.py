from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length,EqualTo

class RegistroForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirma_senha = PasswordField("Confirma_Senha", validators=[DataRequired(), Length(min=6), EqualTo("senha", message="As senhas precisam ser iguais.")])
    submit = SubmitField("Cadastrar")


class LoginForm(FlaskForm):
    identificador = StringField("Usuario ou Email", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

class EmailForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Continuar")

class SenhaForm(FlaskForm):
    senha = PasswordField("Nova Senha", validators=[DataRequired(), Length(min=6)])
    confirma_senha = PasswordField("Confirma", validators=[DataRequired(), EqualTo("senha", message="As senhas precisam ser iguais.")])
    submit = SubmitField("Confirma")
