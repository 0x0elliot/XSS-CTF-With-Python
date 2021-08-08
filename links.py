from flask import Blueprint, render_template, session, request, redirect, url_for, flash
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from recaptcha import checkRecaptcha, config
import threading
from headless import visit_with_cookies
import json

with open('config.py', "r") as file:
    content = file.read()
    config = json.loads(content)
    


open_headless_sessions = 0

links = Blueprint("links", __name__, template_folder = "static/templates")


@links.route('/')
def redirect_():
    return redirect("/submit")

@links.route('/submit', methods = ["GET", "POST"])
def submit():
    message = ""

    if request.method == "POST":

        link_submitted = request.form['link']
        recaptcha_response = request.form['g-recaptcha-response']

        if (checkRecaptcha(recaptcha_response, config['RECAPTCHA_PRIVATE_KEY'])) == False:
            return render_template('submit.html', message = "Captcha Failed. Please try again later.", config = config)

        elif (link_submitted.startswith('http://') or link_submitted.startswith('https://')) == False:
            return render_template('submit.html', message = "Link does not start with https/http.", config = config)
        
        message = "Will visit your site in a bit!"

        #headless browser code

        try:
            t1 = threading.Thread(target = visit_with_cookies, args = (link_submitted,))
            t1.start()
        
        except:
            return render_template('submit.html', message = "An error happened. Please try again.", config = config)

        return render_template("submit.html", message = message, config = config)
    
    elif request.method == "GET":
        return render_template("submit.html", config = config)

@links.route('/api/test')
def test():
    if "key" in dict(request.args):
        return request.args['key']+" like this! see? i am an API guru!"
    
    else:
        return "Use the parameter 'key' to make it reflect."



@links.route('/<some_value>')
def not_found(some_value):
    return render_template("notfound.html", some_value = some_value)
