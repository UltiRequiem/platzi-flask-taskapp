from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from threading import Thread
import unittest
import random


app = Flask(__name__, template_folder='./templates', static_folder='./static')
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = ' SUPER SECRETO'

todos = ['Comprar Cafeina', 'Enviar 2 Solicitud de compra',
         'Entregar video a productor']


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enter')

@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/zero'))
    session['user_ip'] = user_ip

    return response


@app.route('/zero', methods=['GET', 'POST'])
def zero():

    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        
        flash('¡Nombre de usuario registrado con exito ')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

def run():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	t = Thread(target=run)
	t.start()

if __name__ == '__main__':
  keep_alive()
