"""Module that represents the example of using RecipeSearch ADT and RecipeData ADT """
from modules.recipe_search_adt import RecipeSearch
from modules.recipe_data_adt import RecipeData
from modules.main_functions import get_data_from_url, data_from_recipe_ids, check_data, plot_nutrition
import modules.default_information
import modules.errors

# this module uses constant variables
# exactly to show the work of RecipeSearch ADT and RecipeData ADT


def main():
    """
    Main function to show the work of RecipeSearch ADT and RecipeData ADT.
    """
    try:
        print("It is an example module of using RecipeSearch ADT and RecipeData ADT")
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
            number_or_recipes = 5
            print(f"The search is carried out according to such parameters: the main ingredient is {option},"
                  f" cuisine is {cuisine}, diet is {diet}, ingredient to include is {include},"
                  f"ingredient to exclude is {exclude} and the dish type is {dish_type} and"
                  f" the number of recipes is {number_or_recipes}.")
            more_options_complex = [option, cuisine, diet, include, exclude, dish_type, "100"]
            data = get_data_from_url(modules.main_functions.BASE_URL, add_url, option,
                                     more_options=more_options_complex)
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
            data = get_data_from_url(modules.main_functions.BASE_URL, add_url, option,
                                     more_options=more_options_meal_gen)
        else:
            raise ValueError

        if check_data(data) != "information OK":
            return "Such request is incorrect or there are not such recipes"
        else:
            if add_url == "complexSearch":
                recipes = show_recipe_adt_work(add_url, data, number_of_recipes=number_or_recipes)
            else:
                recipes = show_recipe_adt_work(add_url, data)
            res_ids = recipes.recipe_ids()
            res_names = recipes.recipe_names()
            res_amount = recipes.amount_of_recipes()
            new_data = data_from_recipe_ids(res_ids)
            show_recipe_advanced_adt_work(new_data, res_names, res_amount)
            return "Everything went well"

    except ValueError:
        print("The input is wrong!")
    except TypeError:
        print("There is no data for such search, try again!")


def show_recipe_adt_work(add_url, data, number_of_recipes=None):
    """
    (str, dict, int) -> RecipeSearch

    Shows the example of work of RecipeSearch ADT.
    """
    recipes = RecipeSearch(add_url, data)
    recipes.get_recipes()
    if add_url == "complexSearch":
        recipes.recipe_selector(number_of_recipes)
    print("There are such recipes for the query: ")
    recipes_names = recipes.recipe_names()
    for res in recipes_names:
        print(res)
    print()
    if add_url == "mealplans/generate":
        print("Information about the whole nutrition per day using meal generator")
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
    (dict, DynamicArray, int) -> None

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
        if cuisines == "no information":
            cuisines = "no one"
        diets = recipes.search_diets()[k]
        if diets == "no information":
            diets = "no one"
        types = recipes.search_types()[k]
        new_str = f"{recipe} recipe is {res_cheap[k]}, {res_popularity[k]}, {res_health[k]}."
        str_res = f"It contains of {res_calories[k]}, its health score is {res_health_score[k]}," \
                  f" cooking time is {res_time_cook[k]}."
        str_other_info = f"It belongs to such cuisines as {cuisines}, such diets as {diets} and" \
                         f" is sustainable for cooking as {types}."
        str_url = f"It's URL address is {res_urls[k]}"
        print(new_str)
        print(str_res)
        print(str_other_info)
        recipe_ingredients = recipes.ingredients()
        str_ingredients = "To cook this dish you need: " + ", ".join(recipe_ingredients[k]) + '.'
        print(str_ingredients)
        print(str_url)
        if k != len(all_recipes) - 1:
            print()
            print("Next about another dish...")
            print()
        k += 1

    print("Next example of plotting nutrition of the first recipe:")
    substances_res1 = recipes.main_nutrients_percents\
        (modules.default_information.MAIN_NUTRIENTS, 0)
    plot_nutrition(substances_res1, "Main nutrients").show()
    other_substances_res1 = recipes.other_nutrients_percents\
        (modules.default_information.MAIN_NUTRIENTS, 0)
    plot_nutrition(other_substances_res1, "Vitamins, minerals, etc").show()


print(main())
