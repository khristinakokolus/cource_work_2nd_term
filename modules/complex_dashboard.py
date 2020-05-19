"""Module that represents complex dashboard"""
import dash_html_components as html
from dash import Dash, exceptions
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import modules.default_information
import modules.main_functions
from modules.recipe_search_adt import RecipeSearch
from modules.recipe_data_adt import RecipeData


def recipes_complex_data(data, number):
    """
    (dict, int) -> RecipeData

    Function that gets needed information and
    returns one for the further analysis.
    """
    recipes_complex = RecipeSearch(modules.default_information.DEFAULT_COMPLEX_URL, data)
    recipes_complex.get_recipes()
    if len(recipes_complex.recipe_names()) > number:
        recipes_complex.recipe_selector(number)
    recipes_names = recipes_complex.recipe_names()
    recipes_ids = recipes_complex.recipe_ids()
    amount_recipes = recipes_complex.amount_of_recipes()
    new_data = modules.main_functions.data_from_recipe_ids(recipes_ids)
    recipe_advanced_data = RecipeData(new_data, recipes_names, amount_recipes)
    recipe_advanced_data.add_data(modules.default_information.DEFAULT_MAIN_INFO)
    return recipe_advanced_data


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'url(assets/reset.css)']

app = Dash(
    __name__,
    requests_pathname_prefix='/complex/'
)


app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1(children="COMPLEX RECIPE SEARCH WITH ANALYSIS",
                    style={'textAlign': 'center', "color": "white", "font-family": 'Bitter',
                           "font-size": "50px", "font-weight": "normal",
                           "line-height": "54px", "margin": "0 0 54px"}),
            ],),
        html.Div([
            html.Label("BE SURE to choose the main ingredient",
                       style={'color': 'white', "font-weight": "550"}),
        ], style={"color": "white", "width": "100%", "display": "flex",
                  "align-items": "center", "justify-content": "center", 'marginBottom': '1em'}
        ),
        html.Div([
            dcc.Input(id='ingr-id', placeholder='Main ingredient...', type='text', debounce=True,
                      style={"border": "2px solid #aaa", "border-radius": "4px",
                             "margin": "8px 0", "outline": "none", "padding": "8px",
                             "box-sizing": "border-box"}),
            html.H1(id='display-a-choice'),
        ], style={"width": "100%", "display": "flex", "align-items": "center",
                  "justify-content": "center",
                  'marginBottom': '1em'}
        ),

        html.Div([
            html.Label("If you want choose ingredients to include or to exclude USING COMMAS:",
                       style={'color': 'white', "font-weight": "550"}),
        ], style={"color": "white", "width": "100%", "display": "flex",
                  "align-items": "center", "justify-content": "center",
                  'marginBottom': '1em'}
        ),
        html.Div([
            dcc.Input(id='include-id', type='text', placeholder='Ingredients to include...',
                      debounce=True,
                      style={"border": "2px solid #aaa", "border-radius": "4px",
                             "margin": "8px 0", "outline": "none", "padding": "8px",
                             "box-sizing": "border-box"}),
            html.P(id='display-a-choice2'),
            dcc.Input(id='exclude-id', type='text', placeholder='Ingredients to exclude...',
                      debounce=True,
                      style={"border": "2px solid #aaa", "border-radius": "4px",
                             "margin": "8px 0", "outline": "none", "padding": "8px",
                             "box-sizing": "border-box"}),
            html.P(id='display-a-choice3'),
        ], style={"width": "100%", "display": "flex", "align-items": "center",
                  "justify-content": "center",
                  'marginBottom': '1em'}
        ),
        html.Div([
            html.Label("Choose if you want a cuisine, a diet or a dish type:",
                       style={'color': 'white', "font-weight": "550"}),
        ], style={"color": "white", "width": "100%", "display": "flex",
                  "align-items": "center",
                  "justify-content": "center", 'marginBottom': '1em'}
        ),
        html.Div([
            dcc.Dropdown(
                id="cuisine",
                options=[{"label": i, "value": i} for i in modules.default_information.CUISINES],
                placeholder="Select cuisine...",
                style={'width': '220px', 'font-size': '90%', 'height': '40px',
                       "align-items": "center",
                       "justify-content": "center"},
            ),
            dcc.Dropdown(
                id="diet",
                options=[{"label": i, "value": i} for i in modules.default_information.DIETS],
                placeholder="Select Diet...",
                style={'width': '220px', 'font-size': '90%', 'height': '40px'},
            ),
            dcc.Dropdown(
                id="dish type",
                options=[{"label": i, "value": i} for i in modules.default_information.DISH_TYPE],
                placeholder="Select Dish Type...",
                style={'width': '220px', 'font-size': '90%', 'height': '40px'},
            ),
        ], style={"width": "100%", "display": "flex", "align-items": "center",
                  "justify-content": "center", 'padding': "10", 'marginBottom': '1em'}
        ),
        html.Div([
            html.Label("BE SURE to select the number of recipes you want: ",
                       style={'color': 'white', "font-weight": "550"}),
            ], style={"color": "white", "width": "100%", "display": "flex",
                      "align-items": "center",
                      "justify-content": "center", 'marginBottom': '1em'}
                    ),
        html.Div([
            dcc.Dropdown(
                id="amount-res",
                options=[{"label": i, "value": i} for i in range(1, 11)],
                placeholder="Select number of recipes...",
                style={'width': '220px', 'font-size': '90%', 'height': '40px',
                       'marginBottom': '1em'},
            ),
            ], style={"width": "100%", "display": "flex", "align-items": "center",
                      "justify-content": "center", 'padding': "10", 'marginBottom': '1em'}
            ),
        html.Div([
            html.Label("BE SURE after the search DELETE NUMBER to PREVENT UPDATE"
                       " while choosing other "
                       "parameters ",
                       style={'color': 'white', "font-weight": "550"}),
            ], style={"color": "white", "width": "100%", "display": "flex",
                      "align-items": "center",
                      "justify-content": "center", 'marginBottom': '1em'}
                    ),

        html.Div([
            html.Button('Click here to see the results and wait a bit',
                        id='show-secret', n_clicks=0, className="btn"),
            html.Div(id='body-div'),
            ], className="button"),
        ], style={'background-image': 'linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),'
                                      ' url("assets/food_web_app.jpg")',
                  "background-size": "cover", "background-position": "center", 'bottom': '0',
                  'right': '0', 'left': '0',
           'top': '0'}),
        dcc.Tabs(id='tabs-example', value='tab-1', children=[
            dcc.Tab(value='tab-1'),
        ]),
    html.Div(id='tabs-example-content')
        ],

)


@app.callback(
    Output('tabs-example-content', 'children'),
    [Input('ingr-id', 'value'),
     Input("include-id", 'value'),
     Input("exclude-id", 'value'),
     Input('cuisine', 'value'),
     Input('diet', 'value'),
     Input("dish type", 'value'),
     Input("amount-res", 'value'),
     Input(component_id='show-secret',
           component_property='n_clicks'),
     Input('tabs-example', 'value')]

)
def update_state(ingredient, include, exclude, cuisine, diet, dish_type, amount, click, tab):
    if click is None or amount is None or ingredient is None:
        raise exceptions.PreventUpdate
    elif tab == 'tab-1':
        if click is not None and amount is not None and ingredient is not None:
            if ingredient is None:
                return html.H1("YOU DID NOT ENTER THE MAIN INGREDIENT",
                               style={'textAlign': 'center', "color": "#B22222",
                                                "font-family": 'Bitter',
                                                "font-size": "50px", "font-weight": "normal",
                                                "line-height": "54px", "margin": "0 0 54px"})
            option = ingredient
            if include is not None:
                include = include.replace(",", "")
            if exclude is not None:
                exclude = exclude.replace(",", "")
            more_options_complex = [ingredient, cuisine, diet, include, exclude, dish_type, "100"]
            data = modules.main_functions.get_data_from_url(modules.main_functions.BASE_URL,
                                                    modules.default_information.DEFAULT_COMPLEX_URL,
                                                    option, more_options_complex)
            if data == "The input is wrong!":
                return html.Div([html.H3("SOME OF YOUR INPUT VALUES ARE WRONG! TRY AGAIN!",
                                         style={'textAlign': 'center', "color": "#B22222",
                                                "font-family": 'Bitter',
                                                "font-size": "50px", "font-weight": "normal",
                                                "line-height": "54px", "margin": "0 0 54px"})])

            check = modules.main_functions.check_data(data)
            if check == "no data" or check == "no such results":
                return html.Div([html.H3("THERE ARE NO RESULTS FOR SUCH REQUEST",
                                         style={'textAlign': 'center', "color": "#B22222",
                                                "font-family": 'Bitter',
                                                "font-size": "50px", "font-weight": "normal",
                                                "line-height": "54px", "margin": "0 0 54px"})])
            elif check == "bad request":
                return html.Div([html.H3("SORRY SOMETHING WENT WRONG",
                                         style={'textAlign': 'center', "color": "#B22222",
                                                "font-family": 'Bitter',
                                                "font-size": "50px", "font-weight": "normal",
                                                "line-height": "54px", "margin": "0 0 54px"})])
            recipes_complex = recipes_complex_data(data, amount)
            diff_recipe = recipes_complex.recipes()
            output = [html.H1("COMPARATIVE CHARACTERISTICS OF FOUND RECIPES",
                              style={'textAlign': 'center', "color": "#B22222", "font-size": "50px",
                                     "font-family": 'Bitter', "font-weight": "normal"})]
            fig = go.Figure(data=[go.Table(
                header=dict(values=["Recipes's names", 'Healthiness', "Healthy Score", 'Popularity',
                                    "Cheap to cook", "Time cooking", "Calories", "Cuisines", "Diets",
                                    "Types"],
                            line_color='#B22222',
                            fill_color="#E9967A",
                            align='left'),
                cells=dict(values=[[i for i in diff_recipe],
                                   [i for i in recipes_complex.healthiness()],
                                   [i for i in recipes_complex.healthy_score()],
                                   [i for i in recipes_complex.is_popular()],
                                   [i for i in recipes_complex.cheap()],
                                   [i for i in recipes_complex.time_cooking()],
                                   [i for i in recipes_complex.calories()],
                                   [i for i in recipes_complex.search_cuisines()],
                                   [i for i in recipes_complex.search_diets()],
                                   [i for i in recipes_complex.search_types()]],
                           line_color='#B22222',
                           fill_color="white",
                           align='left'))
            ])
            output.append(dcc.Graph(id='main-info-graph', figure=fig))
            output.append(html.H1("NEEDED INGREDIENTS FOR ONE SERVING",
                              style={'textAlign': 'center', "color": "#B22222", "font-family": 'Bitter',
                                     "font-weight": "normal", "font-size": "50px"}))
            ingredients = recipes_complex.ingredients()
            output.append(dcc.Graph(id='main-info-graph', figure=modules.main_functions.
                                    ingredients_table(diff_recipe, ingredients)))
            output.append(html.H1("ANALYSIS OF THE NUTRITION OF THE DISHES",
                              style={'textAlign': 'center', "color": "#B22222",
                                     "font-family": 'Bitter', "font-size": "50px",
                                     "font-weight": "normal",
                                     "line-height": "54px",
                                     "margin": "0 0 54px"}))
            for i in range(len(diff_recipe)):
                main_substances_analysis = recipes_complex.main_nutrients_percents(
                    modules.default_information.MAIN_NUTRIENTS, i)
                other_substances_analysis = recipes_complex.other_nutrients_percents(
                    modules.default_information.MAIN_NUTRIENTS, i)
                output.append(html.H1(f"{diff_recipe[i]} nutrient composition for one serving",
                                  style={'textAlign': 'center', "color": "#8B0000"}))
                output.append(dcc.Graph(id='main-graph', figure=modules.main_functions.
                                        plot_nutrition(main_substances_analysis,
                                                       "Main nutrients")))

                output.append(dcc.Graph(id='other-graph',figure=modules.main_functions.
                                        plot_nutrition(other_substances_analysis,
                                                       "Vitamins, minerals, etc.")))
            res_url = recipes_complex.get_recipe_urls()
            output.append(html.H1("HERE ARE RECIPE'S LINKS:",
                               style={"color": "#B22222", "font-family": 'Bitter', 
                                      "font-weight": "normal"}))
            for i in range(len(diff_recipe)):
                output.extend([dcc.Link(f"{diff_recipe[i]}", href=res_url[i]), html.Br(), html.Br()])

            return html.Div(children=output)
