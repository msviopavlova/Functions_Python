from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")


@app.route('/posts')
def blog_posts():
    blog_url = "https://www.npoint.io/docs/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("post.html", posts=all_posts)



if __name__ == "__main__":
    app.run(debug=True)
