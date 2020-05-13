"""Module that represents the example of using RecipeSearch ADT and RecipeData ADT """
import requests
import json
import plotly.express as px
import pandas as pd
from modules.recipe_search_adt import RecipeSearch
from modules.recipe_advanced_adt import RecipeData
import modules.default_information
import modules.errors

# this module uses constant variables
# exactly to show the work of RecipeSearch ADT and RecipeData ADT

BASE_URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "..."
    }


def main():
    try:
        print("Hello it is an example module of using RecipeSearch ADT and RecipeData ADT")
        print("You can choose ComplexSearch or Meal generating")
        input_value = input("Input please which search you want to test(1, 2): ")
        if input_value == "1":
            add_url = "complexSearch"
            option = 'pasta'
            cuisine = "italian"
            diet = "dairy free"
            include = "tomato"
            exclude = "olives"
            dish_type = "main course"
            print(f"The search is carried out according to such parameters: the main ingredient is {option},"
                  f" cuisine is {cuisine}, diet is {diet}, ingredient to include is {include},"
                  f"ingredient to exclude is {exclude} and the dish type is {dish_type}.")
            more_options_complex = [option, cuisine, diet, include, exclude, dish_type, "50"]
            data = get_data_from_url(BASE_URL, add_url, option, more_options=more_options_complex)
        elif input_value == "2":
            add_url = "mealplans/generate"
            option = None
            calories = "2000"
            diet = "dairy free"
            exclude = "apple"
            print(f"The search is carried out according to such parameters: "
                  f"the amount of calories is {calories},"
                  f" diet is {diet}, ingredient to exclude is {exclude}.")
            more_options_meal_gen = ["day", calories, diet, exclude]
            data = get_data_from_url(BASE_URL, add_url, option, more_options=more_options_meal_gen)
        else:
            raise ValueError

        if check_data(data) != "information OK":
            return "Such request is incorrect or there are not such recipes"
        else:
            recipes = show_recipe_adt_work(add_url, data)
            res_ids = recipes.recipe_ids()
            res_names = recipes.recipe_names()
            res_amount = recipes.amount_of_recipes()
            new_data = data_recipe(res_ids)
            show_recipe_advanced_adt_work(new_data, res_names, res_amount)
            return "Everything went well"

    except ValueError:
        print("The input is wrong!")
    except TypeError:
        print("There is no data for such search, try again!")


def show_recipe_adt_work(add_url, data):
    """
    Shows the example of work of RecipeADT.
    """
    recipes = RecipeSearch(add_url, data)
    recipes.get_recipes()
    recipes.delete_recipes()
    print("There are such recipes for your query: ")
    recipes_names = recipes.recipe_names()
    for res in recipes_names:
        print(res)
    if add_url == "mealplans/generate":
        print("Information about the whole nutrition per day using mel generator")
        nutrients = recipes.nutrients_per_day()
        str_plan = ""
        for item in nutrients:
            if item[0] == "calories":
                str_plan += "This meal plan contain " + \
                            str(item[1]) + " " + item[0].lower() + ", "
            else:
                str_plan += str(item[1]) + " " + "grams" + \
                            " " + item[0].lower() + ", "
        str_plan = str_plan[:-2]
        print(str_plan)
    return recipes


def show_recipe_advanced_adt_work(data, recipes, amount_of_recipes):
    """
    Function to show the work of RecipeAdvanced ADT.
    """
    recipes = RecipeData(data, recipes, amount_of_recipes)
    recipes.add_data(modules.default_information.DEFAULT_MAIN_INFO)
    res_health_score = recipes.healthy_score()
    res_time_cook = recipes.time_cooking()
    res_calories = recipes.calories()
    res_health = recipes.healthiness()
    res_cheap = recipes.cheap()
    res_popularity = recipes.is_popular()
    res_urls = recipes.get_recipe_urls()
    all_recipes = recipes.recipes()
    k = 0
    print("Here is main information about recipes: ")
    for recipe in all_recipes:
        cuisines = recipes.search_cuisines()[k]
        if cuisines == []:
            cuisines = "no one"
        else:
            cuisines = ", ".join(cuisines)
        diets = recipes.search_diets()[k]
        if diets == []:
            diets = "no one"
        else:
            diets = ", ".join(diets)
        types = recipes.search_types()[k]
        types = ", ".join(types)
        new_str = f"{recipe} recipe is {res_cheap[k]}, {res_popularity[k]}, {res_health[k]}."
        str_res = f"It contains of {res_calories[k]} calories, its health score is {res_health_score[k]}," \
                  f" cooking time is {res_time_cook[k]} minutes."
        str_other_info = f"It belongs to such cuisines as {cuisines}, such diets as {diets} and" \
                         f" is sustainable for cooking as {types}."
        str_url = f"It's URL address is {res_urls[k]}"
        print(new_str)
        print(str_res)
        print(str_other_info)
        recipe_ingredients = recipes.ingredients_data_per_recipe(k)
        str_ingredients = "To cook this dish you need: " + ", ".join(recipe_ingredients) + '.'
        print(str_ingredients)
        print(str_url)
        if k != len(all_recipes) - 1:
            print("Next about another dish...")
            print()
        k += 1

    print("Next example of plotting nutrition of the first recipe:")
    substances_res1 = recipes.main_substances_nutrition_percents\
        (modules.default_information.MAIN_SUBSTANCES, 0)
    plot_substances_info(substances_res1, "Main Substances").show()
    other_substances_res1 = recipes.other_substances_nutrition_percents\
        (modules.default_information.MAIN_SUBSTANCES, 0)
    plot_substances_info(other_substances_res1, "Other Substances").show()


def get_data_from_url(base_url, add_url, option, more_options=None):
    """
    Gets information using API.
    """
    if add_url == 'information':
        full_url = base_url + str(option) + f"/information?includeNutrition=true"
    elif add_url == 'complexSearch':
        default_values = modules.default_information.DEFAULT_DICT_COMPLEX
        querystring = {}
        for i in range(len(more_options)):
            key = default_values[i]
            value = more_options[i]
            if value != "None":
                querystring[key] = value.lower()
        full_url = base_url + "complexSearch"
    elif add_url == 'mealplans/generate':
        default_values = modules.default_information.DEFAULT_DICT_MEALS_VALUES
        querystring = {}
        for i in range(len(more_options)):
            key = default_values[i]
            value = more_options[i]
            if value != "None":
                querystring[key] = value
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
    Checks if the data is valid.
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


def data_recipe(recipes_data):
    """
    Function that gets needed id numbers
    for recipes data analysis.
    """
    recipes = []
    for id in recipes_data:
        data = get_data_from_url(BASE_URL, 'information', id)
        recipes.append(data)
    return recipes


def plot_substances_info(substances, value):
    """
    Example of plotting information.
    """
    data_to_pandas = {value: substances[0], "Percents of daily needs": substances[1]}
    data_to_plot = pd.DataFrame(data_to_pandas, columns=[value, "Percents of daily needs"])
    data_plot = px.bar(data_to_plot, x=value, y="Percents of daily needs", color=value)
    return data_plot


print(main())
