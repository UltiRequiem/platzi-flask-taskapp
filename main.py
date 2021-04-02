from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask.helpers import url_for

from threading import Thread

import unittest
import random

from app import create_app
from app.forms import LoginForm

app = create_app()

todos = ['Comprar Cafeina', 'Enviar 2 Solicitud de compra',
         'Entregar video a productor']

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
