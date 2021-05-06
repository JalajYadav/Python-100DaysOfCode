from flask import Flask,render_template
import requests
app= Flask(__name__)

@app.route('/')
def home_page():
    return "<h1>Enter a Name in the url, like this /guess/<--name--></h1>"


@app.route('/guess/<username>')
def guess_page(username):
    response = requests.get("https://api.agify.io/",params={'name':username})
    response = response.json()
    get_age=response['age']
    response = requests.get("https://api.genderize.io/", params={'name': username})
    response = response.json()
    get_gender = response['gender']
    return render_template('index.html',name=username,gender=get_gender,age=get_age)

if __name__ == "__main__":
    app.run(debug=True)