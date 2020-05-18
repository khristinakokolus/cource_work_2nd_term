"""
Module that represents the ADT for getting recipe data
from json and helping to select needed info
due to the certain search.
"""
import random
from modules.arrays import Array, DynamicArray

# Works with data from API with such requests as
# complexSearch, mealplans/generate


class RecipeSearch:
    """Gets needed information about recipes"""
    def __init__(self, query, data):
        """(RecipeSearch, str, str)

        Represents recipes info.
        """
        self.data = data
        self.query = query
        self._recipes = DynamicArray()

    def get_recipes(self):
        """(RecipeSearch)

        Gets needed recipe information from dictionary.
        """
        if self.query == 'mealplans/generate':
            data = self.data['meals']
        elif self.query == 'complexSearch':
            data = self.data['results']
        for recipe in data:
            res_id = recipe['id']
            res_name = recipe['title']
            meals_info = (res_id, res_name)
            self._recipes.append(meals_info)

    def amount_of_recipes(self):
        """(RecipeSearch) -> int

        Returns the amount of recipes.
        """
        return len(self._recipes)

    def recipe_names(self):
        """(RecipeSearch) -> DynamicArray

        Returns the array with the
        recipe names.
        """
        recipe_names = DynamicArray()
        for recipe in self._recipes:
            recipe_name = recipe[1]
            recipe_names.append(recipe_name)
        return recipe_names

    def recipe_ids(self):
        """(RecipeSearch) -> DynamicArray

        Returns the array with the
        recipe id numbers.
        """
        recipe_ids = DynamicArray()
        for recipe in self._recipes:
            recipe_id = recipe[0]
            recipe_ids.append(recipe_id)
        return recipe_ids

    def recipe_selector(self, number):
        """(RecipeSearch, int)

        Selects recipes in the random way.
        """
        new_recipes = DynamicArray()
        while len(new_recipes) != number:
            value = random.choice(self._recipes)
            if value not in new_recipes:
                new_recipes.append(value)
        self._recipes = new_recipes

    def nutrients_per_day(self):
        """(RecipeSearch) -> Array

        Returns the array with amount of nutrients for the
        mealplans search.
        """
        if self.query != 'mealplans/generate':
            return 'This information cannot be obtained from such a request'
        nutrients_per_day = Array(3)
        dct_nutrition = self.data['nutrients']
        i = 0
        for key, value in dct_nutrition.items():
            if key != "calories":
                val_pair = (key, value)
                nutrients_per_day[i] = val_pair
                i += 1
        return nutrients_per_day
