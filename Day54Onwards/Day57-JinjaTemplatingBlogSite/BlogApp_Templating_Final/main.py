from flask import Flask, render_template
import requests

app = Flask(__name__)
data = []
@app.route('/')
def home():
    global data
    response = requests.get("https://api.npoint.io/a4db86b233874f273d63")
    data = response.json()
    return render_template("index.html",blog_posts = data)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    for item in data:
        print(item)
        if int(item['id']) == post_id:
            print('here')
            return render_template("post.html", title = item['title'], content=item['content'])

if __name__ == "__main__":
    app.run(debug=True)
