import os
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the page >>>></h1>"

@app.route('/about-me')
def aboutme():
    post_list = [
        "Ho & ten: Nguyen Duy Hoang",
        "Sinh Ngay: 3/ 5/ 1997",
        "Dang lam: Học viên",
        "Hobbies: Thich nghe nhac, choi game"
    ]
    return render_template("about_me.html",
                            article_tile = "Personal",
                            post_list = post_list)

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)
if __name__ == '__main__':
  app.run(debug=True)
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
