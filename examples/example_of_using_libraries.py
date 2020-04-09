"""Module that represents the example of using needed libraries for work"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import json
import pandas as pd
import plotly.express as px
from flask import Flask
import requests

BASE_URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com" \
           "/recipes/res/information?includeNutrition=true"
HEADERS = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "..."
}
RECIPE_ID = '716429'


# this module uses a predefined id number of recipe
# this is to directly show an example of work
# using all the needed python libraries


def read_url(base_url, headers, num):
    """
    Information retrieval of the recipe using API.
    """
    base_url = base_url.replace('res', num)
    response = requests.request("GET", base_url,
                                headers=headers)
    return response.text


def data_analysis(data):
    """
    The function that receives the information from
    API and uses the possible one.
    Returns the list with the name of the dish, the
    names of dish substances and their amount in mg.
    """

    data_js = json.loads(data)
    info_lst = []
    lst_vitamines = []
    lst_amounts = []
    for key in data_js.keys():
        if key == 'title':
            title = data_js[key]
            info_lst.append(title)
        elif key == 'nutrition':
            for nutrients in data_js['nutrition']['nutrients']:
                for key_nut in nutrients.keys():
                    if key_nut == "title" and \
                            nutrients['unit'] == 'mg':
                        title_value = nutrients[key_nut]
                        lst_vitamines.append(title_value)
                    elif key_nut == "amount" and \
                            nutrients['unit'] == 'mg':
                        value = nutrients[key_nut]
                        lst_amounts.append(value)
    info_lst.append(lst_vitamines)
    info_lst.append(lst_amounts)
    return info_lst


def plot_info(info_lst):
    """
    Makes a diagram from information.
    """
    data_nutrition = pd.DataFrame(dict(Substance=info_lst[1],
                                       Amount=info_lst[2]))
    data = px.bar(data_nutrition, x='Substance', y='Amount',
                  color="Substance")
    return data


server = Flask(__name__)


@server.route('/')
def index():
    """
    Testing the use of Flask with Dash.
    """
    return 'Testing Flask app'


def app(data, info_lst):
    """
    Returns the example of Dash app.
    """
    app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/dash/'
    )
    app.layout = html.Div(children=[
        html.H1(children="Example of using Dash"),
        html.H2(children=f'The dish is {info_lst[0]}'),
        html.H2(children="All the substances are in mg"),
        dcc.Graph(id='example-graph', figure=data)
    ])
    return app


if __name__ == '__main__':
    information = read_url(BASE_URL, HEADERS, RECIPE_ID)
    info_lst = data_analysis(information)
    data = plot_info(info_lst)
    new_app = app(data, info_lst)
    new_app.run_server(debug=True)

