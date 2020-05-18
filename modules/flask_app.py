"""Module that represents directions to different pages"""
from flask import Flask, render_template

flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    """
    Returns the home web page.
    """
    return render_template('index.html')


@flask_app.route('/complexsearch')
def complex():
    """
    Returns the web page for complex
    search.
    """
    return render_template("complexsearch.html")


@flask_app.route('/mealplans')
def meal_generating():
    """
    Returns the web page for meal generator.
    """
    return render_template("mealplans.html")
