from flask import request, make_response, redirect, render_template, session
import unittest

from keep_alive import keep_alive, app

@app.cli.command()
def test():
    unittest.TextTestRunner().run(unittest.TestLoader().discover('tests'))

@app.route('/')
def index():
    session['user_ip'] = request.remote_addr
    return make_response(redirect('/zero'))

@app.route('/zero', methods=['GET'])
def zero():
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {'user_ip': user_ip, 'todos':['Comprar cafeina', 'Enviar solicitudes de compra'], 'username': username}

    return render_template('hello.html', **context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

if __name__ == '__main__':
    keep_alive()
