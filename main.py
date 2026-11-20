import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template('index.html', all_posts=posts)

@app.route('/blog/<int:number>')
def get_blog(number):
    posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    requested_post = None
    for post in posts:
        if post['id'] == number:
            requested_post = post

    return render_template('post.html', req_post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)



