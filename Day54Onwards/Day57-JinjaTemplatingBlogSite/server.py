from flask import Flask,render_template
import random
from datetime import datetime

app= Flask(__name__)

current_year = datetime.now().year
@app.route('/')
def home_page():
    rand_int = random.randint(0, 10)
    return render_template('index.html',num=rand_int,year = current_year)

if __name__ == "__main__":
    app.run(debug=True)