from flask import request, make_response, redirect, render_template, session

from threading import Thread

import unittest
import random

from app import create_app

app = create_app()

todos = ['Comprar Cafeina', 'Enviar 2 Solicitud de compra', 'Entregar video a productor']


@app.cli.command()
def test():
    testy = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(testy)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/zero'))
    session['user_ip'] = user_ip

    return response


@app.route('/zero', methods=['GET'])
def zero():
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {'user_ip': user_ip, 'todos': todos, 'username': username}

    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


def run():
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == '__main__':
    keep_alive()
