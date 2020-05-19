"""Module that represents meal generating dashboard"""
import dash_html_components as html
from dash import Dash, exceptions
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import modules.default_information
import modules.errors
import modules.main_functions
from modules.recipe_search_adt import RecipeSearch
from modules.recipe_data_adt import RecipeData


def pie_chart_mealgenerator(information):
    """
    (Array) -> Figure

    Function that creates a pie chart for the meal
    generator.
    """
    data_to_pandas = pd.DataFrame(information, columns=["Nutrient", "Amount"])
    fig = px.pie(data_to_pandas, values="Amount", names="Nutrient",
                 color_discrete_sequence=px.colors.sequential.RdBu,
                 title="Three main nutrients amount per day")
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'url(assets/stylesheet.css)']

app = Dash(
    __name__,
    requests_pathname_prefix='/mealgenerator/'
)


app.layout = html.Div([
    html.Div([
    html.Div([
        html.H1(children="MEAL GENERATOR WITH ANALYSIS",
                style={'textAlign': 'center', "color": "white", "font-family": 'Bitter',
                       "font-size": "50px", "font-weight": "normal", "line-height": "54px",
                       "margin": "0 0 54px"}),
        ], ),
    html.Div([
        html.Label("Amount of calories FROM 500 TO 4000: ", style={"color": "white"}),
        ],style={"width": "100%", "display": "flex", "align-items": "center",
                 "justify-content": "center",
                 'marginBottom': '1em'}
        ),
    html.Div([
        dcc.Input(id='calories-id', placeholder='Calories...', type='text', debounce=True,
                  style={"border": "2px solid #aaa", "border-radius": "4px",
                         "margin": "8px 0", "outline": "none", "padding": "8px",
                         "box-sizing": "border-box"}),
        html.H1(id='display-a-choice'),
        ],style={"width": "100%", "display": "flex", "align-items": "center",
                 "justify-content": "center",
                 'marginBottom': '1em'}
        ),
    html.Div([
        html.Label("Diet:", style={"color": "white"}),
        ],style={"width": "100%", "display": "flex", "align-items": "center",
                 "justify-content": "center",
                 'marginBottom': '1em'}
        ),
    html.Div([
        dcc.Dropdown(
            id="diet",
            options=[{"label": i, "value": i} for i in default_information.DIETS],
            placeholder="Select Diet...",
            style={'width': '220px', 'font-size': '90%', 'height': '40px',
                   "align-items": "center",
                   "justify-content": "center", 'marginBottom': '1em'}
        ),
        ],style={"width": "100%", "display": "flex", "align-items": "center",
                 "justify-content": "center"}
        ),
    html.Div([
        html.Label("Ingredients to exclude USING COMMAS: ", style={"color": "white"}),
        ],style={"width": "100%", "display": "flex", "align-items": "center",
                 "justify-content": "center",
                 'marginBottom': '1em'}
        ),
    html.Div([
        dcc.Input(id='exclude-id', type='text', placeholder='Ingredients to exclude...',
                  debounce=True,
                  style={"border": "2px solid #aaa", "border-radius": "4px",
                         "margin": "8px 0", "outline": "none", "padding": "8px",
                         "box-sizing": "border-box"}),
        ], style={"width": "100%", "display": "flex", "align-items": "center",
                  "justify-content": "center",
                  'marginBottom': '1em'}
        ),
    html.H1(id='display-a-choice3'),
    html.Div([
        html.Button('Click here to see the results and wait a bit', id='show-secret',
                    className="btn"),
    html.Div(id='body-div')
        ], className="button"),
    ], style={'background-image': 'linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), '
                                  'url("assets/food_web_app.jpg")',
              "background-size": "cover", "background-position": "center",
              'bottom': '0', 'right': '0', 'left': '0',
           'top': '0'}),
        dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(value='tab-1'),
    ]),
    html.Div(id='tabs-example-content')
],
)


@app.callback(
    Output('tabs-example-content', 'children'),
    [Input('calories-id', 'value'),
     Input("diet", 'value'),
     Input('exclude-id', 'value'),
     Input(component_id='show-secret', component_property='n_clicks'),
     Input('tabs-example', 'value')]
)
def update_meal_generating(calories, diet, exclude, click, tab):
    if click is None:
        raise exceptions.PreventUpdate
    elif tab == "tab-1":
        option = None
        more_options = ["day", calories, diet, exclude]
        data = main_functions.get_data_from_url(main_functions.BASE_URL,
                                                        default_information.DEFAULT_MEAL_PLANNER_URL,
                                                        option, more_options)
        if data == "The input is wrong!":
            return html.Div([html.H3("SOME OF YOUR INPUT VALUES ARE WRONG! TRY AGAIN!",
                                     style={'textAlign': 'center', "color": "#B22222", 
                                            "font-family": 'Bitter',
                                            "font-size": "50px", "font-weight": "normal",
                                            "line-height": "54px", "margin": "0 0 54px"})])
        recipes_meal_gen = RecipeSearch(default_information.DEFAULT_MEAL_PLANNER_URL, data)
        recipes_meal_gen.get_recipes()
        recipe_names = recipes_meal_gen.recipe_names()
        recipes_ids = recipes_meal_gen.recipe_ids()
        recipes_nutrition = recipes_meal_gen.nutrients_per_day()
        new_data = main_functions.data_from_recipe_ids(recipes_ids)
        amount_recipes = recipes_meal_gen.amount_of_recipes()
        recipe_advanced_data = RecipeData(new_data, recipe_names, amount_recipes)
        recipe_advanced_data.add_data(default_information.DEFAULT_MAIN_INFO)
        output = []
        output.append(html.H1("MAIN INFORMATION ABOUT THE FOUND RECIPES",
                              style={'textAlign': 'center', "color": "#B22222", "font-size": "50px",
                                     "font-family": 'Bitter', "font-weight": "normal"}))
        recipes = recipe_advanced_data.recipes()
        fig = go.Figure(data=[go.Table(
            header=dict(values=["Recipes's names", 'Healthiness', "Health score",
                                'Popularity', "Cheap to cook", "Cooking time",
                                "Amount of calories", "Cuisines", "Diets", "Types"],
                        line_color='#B22222',
                        fill_color="#E9967A",
                        align='left',),
            cells=dict(values=[[i for i in recipes],
                               [i for i in recipe_advanced_data.healthiness()],
                               [i for i in recipe_advanced_data.healthy_score()],
                               [i for i in recipe_advanced_data.is_popular()],
                               [i for i in recipe_advanced_data.cheap()],
                               [i for i in recipe_advanced_data.time_cooking()],
                               [i for i in recipe_advanced_data.calories()],
                               [i for i in recipe_advanced_data.search_cuisines()],
                               [i for i in recipe_advanced_data.search_diets()],
                               [i for i in recipe_advanced_data.search_types()]],
                       line_color='#B22222',
                       fill_color="white",
                       align='left',))
        ])
        output.append(dcc.Graph(id='main-info-graph', figure=fig))
        output.append(html.H1("NEEDED INGREDIENTS FOR ONE SERVING",
                              style={'textAlign': 'center', "color": "#B22222",
                                     "font-family": 'Bitter',
                                     "font-weight": "normal", "font-size": "50px"}))
        ingredients = recipe_advanced_data.ingredients()
        output.append(dcc.Graph(id='main-info-graph', figure=main_functions.ingredients_table(recipes, 
                                                                                              ingredients)))
        output.append(html.H1("ANALYSIS OF THE NUTRITION OF THE DISHES",
                              style={'textAlign': 'center', "color": "#B22222",
                                     "font-family": 'Bitter', "font-size": "50px",
                                     "font-weight": "normal",
                                     "line-height": "54px",
                                     "margin": "0 0 54px"}))
        output.append(dcc.Graph(id='main-info-graph',
                                figure=pie_chart_mealgenerator(recipes_nutrition)))
        for i in range(len(recipes)):
            main_substances_analysis = recipe_advanced_data.main_nutrients_percents(
                default_information.MAIN_NUTRIENTS, i)
            other_substances_analysis = recipe_advanced_data.other_nutrients_percents(
                default_information.MAIN_NUTRIENTS, i)
            output.append(html.H1(f"{recipes[i]} recipe nutrition",
                                  style={'textAlign': 'center', "color": "#8B0000"}))
            output.append(dcc.Graph(id='main-graph', figure=main_functions.
                                    plot_nutrition(main_substances_analysis,
                                                   "Main nutrients")))

            output.append(dcc.Graph(id='other-graph', figure=main_functions.
                                    plot_nutrition(other_substances_analysis,
                                                   "Vitamins, minerals, etc.")))
        res_urls = recipe_advanced_data.get_recipe_urls()
        output.extend([html.H1("HERE ARE RECIPE'S LINKS:",
                               style={"color": "#B22222", "font-family": 'Bitter',
                                      "font-weight": "normal"}),
                       dcc.Link(f"{recipes[0]}", href=res_urls[0]), html.Br(), html.Br(),
                       dcc.Link(f"{recipes[1]}", href=res_urls[1]), html.Br(), html.Br(),
                       dcc.Link(f"{recipes[2]}", href=res_urls[2])])
        return html.Div(children=output)
