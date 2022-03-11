from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///comments.db")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    #app.run(host"0.0.0.0")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/comment", methods=["GET","POST"])
def comment():
    if request.method == "POST":
        name = request.form.get("name")
        comment = request.form.get("comment")
        print(name)
        print(comment)
        db.execute("INSERT INTO comments (name, comment) VALUES(?, ?)", name, comment)
        return render_template("portfolio.html")
    else:
        comments = db.execute("SELECT * FROM comments")
        return render_template("comment.html", comments=comments)