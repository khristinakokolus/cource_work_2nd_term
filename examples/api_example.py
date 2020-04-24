"""This module represents the function that gets info from API"""
import json
import requests

# in the files meal_generate_example.json, 
# recipes_example.json, complex_example.json
# are the examples of function calls with different parameters
# to get more information about them and their use to call the function
# visit https://spoonacular.com/food-api/docs


BASE_URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
HEADERS = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "..."
}


def get_information_from_url(base_url, add_url, options, file_name):
    """
    (str, str, str, str) -> None

    Example of information retrieval about food using API.
    This function has four main parameters.
    Parameter base_url is the main site from where API comes from.
    Parameter add_url is an extension of the url address where you
    want to find information. Example: '/recipes/mealplans/generate'
    Parameter options is responsible for the data that will be searched.
    Example: {"timeFrame":"day","targetCalories":"2000","diet":"vegetarian",
    "exclude":"shellfish%2C olives"}
    Parameter file_name is for where you want to save the json data.
    """
    if isinstance(options, str):
        url = base_url + add_url + '/' + options
        response = requests.request("GET", url, headers=HEADERS,
                                    params=options)
    else:
        url = base_url + add_url
        response = requests.request("GET", url, headers=HEADERS,
                                    params=options)
    data = json.loads(response.text)
    with open(file_name, 'w+') as js_file:
        json.dump(data, js_file, indent=4)


if __name__ == '__main__':
    pass

