"""Module that represents main functions for the program work"""
import json
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import modules.default_information
import modules.errors

BASE_URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "..."
    }


def check_input(add_url, more_options):
    """
    (str, list)

    Checks the input of the user.
    """
    if add_url == modules.default_information.DEFAULT_COMPLEX_URL:
        if "," in more_options[0]:
            return "mistake"
        elif more_options[3] is not None and len(more_options[3].split()) > 1:
            more_options[3] = more_options[3].split()
        elif more_options[4] is not None and len(more_options[4].split()) > 1:
            more_options[4] = more_options[4].split()
        return more_options
    elif add_url == modules.default_information.DEFAULT_MEAL_PLANNER_URL:
        if more_options[1] is not None:
            if int(more_options[1]) > 4000 or int(more_options[1]) < 500:
                return "mistake"
        elif more_options[3] is not None and len(more_options[3].split()) > 1:
            more_options[3] = more_options[3].split()
        return more_options


def get_data_from_url(base_url, add_url, option, more_options=None):
    """
    (str, str, str, list) -> dict

    Gets information using API.
    """
    if add_url != "information":
        check = check_input(add_url, more_options)
        if check == "mistake":
            return "The input is wrong!"
    if add_url == 'information':
        full_url = base_url + str(option) + f"/information?includeNutrition=true"
    elif add_url == 'complexSearch':
        more_options = check
        default_values = modules.default_information.DEFAULT_DICT_COMPLEX
        querystring = {}
        for i in range(len(more_options)):
            key = default_values[i]
            value = more_options[i]
            if value is not None:
                querystring[key] = value
        if "includeIngredients" in querystring.keys() and\
                not isinstance(querystring["includeIngredients"], str):
            str_include = ""
            for item in querystring["includeIngredients"]:
                str_include += item + "%2C "
            str_include = str_include[:-4]
            querystring["includeIngredients"] = str_include
        if "excludeIngredients" in querystring.keys() and\
                not isinstance(querystring["excludeIngredients"], str):
            str_exclude = ""
            for item in querystring["excludeIngredients"]:
                str_exclude += item + "%2C "
            str_exclude = str_exclude[:-4]
            querystring["excludeIngredients"] = str_exclude
        full_url = base_url + "complexSearch"
    elif add_url == 'mealplans/generate':
        more_options = check
        default_values = modules.default_information.DEFAULT_DICT_MEALS_VALUES
        querystring = {}
        for i in range(len(more_options)):
            key = default_values[i]
            value = more_options[i]
            if value is not None:
                querystring[key] = value
        if "excludeIngredients" in querystring.keys() and \
                not isinstance(querystring["excludeIngredients"], str):
            str_exclude = ""
            for item in querystring["excludeIngredients"]:
                str_exclude += item + "%2C "
            str_exclude = str_exclude[:-4]
            querystring["excludeIngredients"] = str_exclude
        full_url = base_url + add_url

    if add_url == "information":
        response = requests.request("GET", full_url, headers=headers)
    else:
        response = requests.request("GET", full_url, headers=headers,
                                    params=querystring)

    data = json.loads(response.text)
    return data


def check_data(data):
    """
    (dict) -> str

    Checks if the data from API is valid.
    """
    if data == []:
        return "no data"
    elif data == modules.errors.NO_RESULTS_COMPLEX or \
            data == modules.errors.NO_RESULTS_MEALS:
        return "no such results"
    elif data == modules.errors.BAD_REQUEST:
        return "bad request"
    else:
        return "information OK"


def data_from_recipe_ids(recipes_data):
    """
    (DynamicArray) -> list

    Function that uses recipes' ids to get
    information for recipes' analysis.
    """
    recipes = []
    for id in recipes_data:
        data = get_data_from_url(BASE_URL, 'information', id)
        recipes.append(data)
    return recipes


def ingredients_table(recipes, ingredients):
    """
    (DynamicArray, DynamicArray) -> Figure

    Function that makes a table from the information
    about the ingredients of the dishes.
    """
    fig = go.Figure(data=[go.Table(header=dict(values=[i for i in recipes], line_color='#B22222',
                                               fill_color="#E9967A"),
                                   cells=dict(values=[[i for i in item]
                                                      for item in ingredients],
                                              line_color='#B22222', fill_color="white"))])
    return fig


def plot_nutrition(main_subs, value):
    """
    (Array, str) -> Figure

    Function that makes bar chart from the
    nutrition composition information.
    """
    data_to_pandas = {"Percent of daily needs": main_subs[1], value: main_subs[0]}
    data_to_plot = pd.DataFrame(data_to_pandas, columns=["Percent of daily needs", value])
    data_plot = px.bar(data_to_plot, x="Percent of daily needs", y=value, color="Percent of daily needs",
                       orientation='h')
    return data_plot
