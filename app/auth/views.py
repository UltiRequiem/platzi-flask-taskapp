from . import auth
from app.forms import LoginForm

@auth.route('/login')
def login():
    context = {'login_form': LoginForm()}
    return ''

