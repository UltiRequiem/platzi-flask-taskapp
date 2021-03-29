from flask import Flask, request,make_response, redirect, render_template

app = Flask(__name__, template_folder='./templates', static_folder='./static')

todos = ['Comprar Cafeina','Enviar 2 Solicitud de compra', 'Entregar video a productor']
@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/zero'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/zero')
def zero():

    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }

    return render_template('hello.html',**context)

if __name__ == '__main__':
    app.run(debug=True)
