from flask import Flask , render_template, url_for


app = Flask(__name__)
posts = [{'author':'Gurkirat', 'post_date':'1 Jan 2023', 'post_title':'Blog 1', 'post_content':'This is content of post 1'},{'author':'Karan', 'post_date':'10 Jan 2023', 'post_title':'Blog 2', 'post_content':'This is content of post 2'}]



@app.route("/home")
@app.route("/")
def homepage():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about_page():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, port=8003)
