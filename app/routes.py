from app import app #from our app folder, we need to import instance from app



# @app.route('/home')
# def homePage():
#     return{
#         "Oh Hello there" : "CLUTCH!"
#     }

from flask import render_template


@app.route('/')
def homePage():
    return render_template("index.html")

@app.route('/login')
def loginPage():
    return render_template("login.html")