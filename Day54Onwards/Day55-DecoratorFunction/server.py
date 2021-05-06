from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h1>Guess a number between 0 to 9</h1>' \
           '<h3>add /number to the Url to see results</h3>' \
           '<img src="https://media3.giphy.com/media/S65GkxL15Z8uGTF8Zl/giphy.gif?cid=ecf05e47h1lprc5ixfh7tgdoclk7gxq3k4qqnr8wg4tnr4dd&rid=giphy.gif&ct=g">'

import random
rand_number = random.randint(0,9)

@app.route('/<int:guess>')
def guess_fun(guess):
    if guess<rand_number:
        return '<h2>You guessed too low</h2>' \
               '<img src="https://media4.giphy.com/media/eJLwreQ3JfIdjWl8lX/giphy.gif?cid=ecf05e47dq72s2ljk8lwy0rwrk5a5z7bmqrlk5uwo1uxsi70&rid=giphy.gif&ct=g">'
    elif guess>rand_number:
        return '<h2>You guessed too high</h2>' \
               '<img src="https://media3.giphy.com/media/KfTsEf7OXeRsIsfPzo/giphy.gif?cid=ecf05e47k83wfyqhuw1ehvrk91xam6l91lccg3jhinm09v6k&rid=giphy.gif&ct=g">'
    else:
        return '<h2>You got it right</h2>' \
               '<img src="https://media3.giphy.com/media/MBboAKn0QbeFrGCb6M/giphy.gif?cid=ecf05e47vhhk6bizn08sprx7yiudfakopvzvassp32df0wxd&rid=giphy.gif&ct=g">'
if __name__ == '__main__':
    app.run(debug=True)