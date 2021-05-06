from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_fun():
        return '<b>' \
               f'{function()}' \
               f'</b>'
    return wrapper_fun


def make_emphesis(function):
    def wrapper_fun():
        return '<em>' \
               f'{function()}' \
               f'</em>'
    return wrapper_fun


def make_underline(function):
    def wrapper_fun():
        return '<u>' \
               f'{function()}' \
               f'</u>'
    return wrapper_fun


@app.route('/')
@make_bold
@make_emphesis
@make_underline
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)