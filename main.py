from flask import Flask,g,abort, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)


Bootstrap(app)



@app.route('/')
def get_all_posts():

    return render_template("index.html")




if __name__ == "__main__":
    # app.run(debug=True,port=5001)
    app.run(host="0.0.0.0",port=5000)