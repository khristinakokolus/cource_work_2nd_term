"""Module that represents the connection between flask and dash"""
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from modules.complex_dashboard import app as app1
from modules.meal_gen_dashboard import app as app2
from modules.flask_app import flask_app


application = DispatcherMiddleware(flask_app, {
    '/complex': app1.server,
    '/mealgenerating': app2.server,
})

if __name__ == '__main__':
    run_simple('localhost', 8050, application)
