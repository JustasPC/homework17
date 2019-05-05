from flask import Flask, render_template
from flask import request
from flask import make_response
import random

import datetime

app = Flask(__name__)


@app.route("/")
def index():
    title = 'Pagrindinis'
    time = datetime.datetime.now()
    return render_template("index.html", title=title, time=time)


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method=="GET":
        title="Apie mane"

        user_name = request.cookies.get("user_name")
        user_name = request.cookies.get('user_name')
        return render_template("about.html", title=title, name=user_name)
    elif request.method=="POST":
        title = "Issiusta sekmingai"
        contact_name = request.form.get('contact-name')
        contact_email = request.form.get('contact-email')
        contact_message = request.form.get('contact-message')

        response = make_response(render_template("success.html", title=title))
        response.set_cookie('user_name', contact_name)

        return response


@app.route("/game", methods=["GET", "POST"])
def game():
    title = 'Guess the number game'
    cookie = request.cookies.get("secret_number")
    if request.method=="GET":
        if not cookie:
            s_number = random.randint(1, 30)
            print('*************************************')
            print('cookie not found, generated:', s_number)
            print('*************************************')
            cookie = str(s_number)
        print('*************************************')
        print('cookie set, secret number is:', cookie)
        print('*************************************')
        response = make_response(render_template("guessthenumber.html", title=title))
        response.set_cookie("secret_number", cookie)
    if request.method=="POST":
        guess = request.form.get('guess')
        print('*************************************')
        print('guess accepted, secret number is:', cookie)
        print('guess is:', guess)
        print('*************************************')
        if str(guess)==str(cookie):
            print("right")
            info ="Congrats!!!! You guessed right! secret number was indeed "+str(guess)
            response = make_response(render_template("result.html", title=title, result=info))
            print("Old cookie will be deleted")
            response.set_cookie("secret_number", expires=0)
        else:
            print('wrong')
            if int(cookie) > int(guess):
                text = ". Try bigger number."
            else:
                text = ". Try lesser number."
            info = "Sorry, this number is not right:" + str(guess) +text
            response = make_response(render_template("result.html", title=title, result=info))
            print("Old cookie will used again")
            response.set_cookie("secret_number", cookie) #Guess same number later
    return response









@app.route("/portfolio")
def portfolio():
    title = 'Portfelis'
    print('test')
    return render_template("portfolio.html", title=title)


if __name__ == '__main__':
    app.run()
