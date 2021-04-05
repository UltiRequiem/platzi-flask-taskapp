from flask import request, make_response, redirect, render_template, session
from flask_login import login_required
import unittest
from app.firestore_service import get_users, get_todos
from keep_alive import keep_alive, app

@app.cli.command()
def test():
    unittest.TextTestRunner().run(unittest.TestLoader().discover('tests'))

@app.route('/')
def index():
    session['user_ip'] = request.remote_addr
    return make_response(redirect('/zero'))

@app.route('/zero', methods=['GET'])
@login_required
def zero():
    user_ip = session.get('user_ip')
    username = current_user.id
    context = {'user_ip': user_ip, 'todos':get_todos(user_id=username), 'username': username}
    
    users = get_users()
    
    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    return render_template('hello.html', **context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

if __name__ == '__main__':
    keep_alive()
