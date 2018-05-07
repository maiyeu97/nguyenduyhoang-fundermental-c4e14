from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') # When user
def index():    #
    post_list = [
        "Toi la nguoi",
        "La loai nguoi gi",
        "Nguoi tot",
        "Nhat the gioi"
    ]
    return render_template("index.html",
                            article_tile="TOI LA AI",
                            post_list=post_list)

@app.route('/blog')
def blog():
    posts = [
        {
        'content': "Toi la nguoi",
        'author': "HOANG"
        },
        {
        'content': "La loai nguoi gi",
        'author': "HOANG"
        }
    ]
    return render_template("blog.html",
                            posts=posts)

@app.route('/sayhi/<name>')
def sayhi(name):
    return "Hello" + name

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)


@app.route('/Heading')
def heading():
    return "<h1>CHU TO DAM</h1>"


if __name__== '__main__':
    app.run(debug=True)
