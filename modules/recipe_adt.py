"""
Module that represents the ADT for getting recipe data
from json and helping to select needed info
due to the certain search.
"""
from modules.arrays import DynamicArray

# Works with data from API with such requests as
# complexSearch, mealplans/generate


class Recipe:
    """Gets needed information about recipes"""
    def __init__(self, query, data):
        """(Recipe, str, str)

        Represents recipes info.
        """
        self.data = data
        self.query = query
        self._recipes = DynamicArray()

    def get_recipes(self):
        """(Recipe)
        Gets needed recipe info from json.
        """
        if self.data == []:
            self._recipes = None
        if self.query == 'mealplans/generate':
            for recipe in self.data['meals']:
                res_id = recipe['id']
                res_name = recipe['title']
                meals_info = (res_id, res_name)
                self._recipes.append(meals_info)
        elif self.query == 'complexSearch':
            for recipe in self.data['results']:
                res_id = recipe['id']
                res_title = recipe['title']
                meals_info = (res_id, res_title)
                self._recipes.append(meals_info)

    def recipes(self):
        """(Recipe)

        Returns the whole collected information.
        """
        return self._recipes

    def recipe_names(self):
        """(Recipe)

        Returns the list with the
        recipe names.
        """
        recipe_names = DynamicArray()
        for recipe in self._recipes:
            recipe_name = recipe[1]
            recipe_names.append(recipe_name)
        return recipe_names

    def recipe_ids(self):
        """(Recipe)

        Returns the list with the
        recipe id numbers.
        """
        recipe_ids = DynamicArray()
        for recipe in self._recipes:
            recipe_id = recipe[0]
            recipe_ids.append(recipe_id)
        return recipe_ids

    def nutrients_per_day(self):
        """(Recipe)

        Returns the amount of nutrients for the
        mealsplan search.
        """
        if self.query != 'mealplans/generate':
            return 'This information cannot be obtained from such a request'
        nutrients_per_day = DynamicArray()
        dct_nutrition = self.data['nutrients']
        for key, value in dct_nutrition.items():
            val_pair = (key, value)
            nutrients_per_day.append(val_pair)
        return nutrients_per_day

