from flask import Flask,render_template
from app import app


@app.route('/')
def test():
    return 'It works!'


# @app.route('/about')
# def about():
#     return render_template("about.html")