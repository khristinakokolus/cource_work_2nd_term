"""
Module that represents the ADT for getting recipe data
from json and helping to select needed info
due to the certain search.
"""
from modules.arrays import DynamicArray

# Works with data from API with such requests as
# findByIngredients, complexSearch, mealplans/generate


class Recipe:
    """Gets needed info and manipulates with it"""
    def __init__(self, query, data, amount_ingredients=None):
        """
        Represents recipes info.
        """
        self.data = data
        self.query = query
        self._recipes = DynamicArray()
        self._amount_ingredients = amount_ingredients

    def get_recipes(self):
        """
        Gets needed recipe info from json.
        """
        if self.data == []:
            self._recipes = None
        elif self.query == 'mealplans/generate':
            for recipe in self.data['meals']:
                res_id = recipe['id']
                res_name = recipe['title']
                meals_info = (res_id, res_name)
                self._recipes.append(meals_info)
        elif self.query == 'findByIngredients':
            for recipe in self.data:
                res_id = recipe['id']
                res_title = recipe['title']
                res_missed_ingredients = recipe["missedIngredientCount"]
                meals_info = (res_id, res_title, res_missed_ingredients)
                self._recipes.append(meals_info)
        elif self.query == 'complexSearch':
            for recipe in self.data['results']:
                res_id = recipe['id']
                res_title = recipe['title']
                meals_info = (res_id, res_title)
                self._recipes.append(meals_info)

    def recipe_names(self):
        """
        Returns the list with the
        recipe names.
        """
        recipe_names = DynamicArray()
        for recipe in self._recipes:
            recipe_name = recipe[1]
            recipe_names.append(recipe_name)
        return recipe_names

    def recipe_ids(self):
        """
        Returns the list with the
        recipe id numbers.
        """
        recipe_ids = DynamicArray()
        for recipe in self._recipes:
            recipe_id = recipe[0]
            recipe_ids.append(recipe_id)
        return recipe_ids

    def missed_ingredients_count(self):
        """
        Returns the amount of missed ingredients
        """
        if self.query != 'findByIngredients':
            return 'This information cannot be obtained from such a request'
        missed_ingr = DynamicArray()
        for recipe in self._recipes:
            missed = recipe[2]
            missed_ingr.append(missed)
        return missed_ingr

    def analyse_missed_ingredients_count(self):
        """
        Analyses missed ingredient count
        and reduces the number of recipes.
        """
        if self.query != 'findByIngredients':
            return 'This information cannot be obtained from such a request'
        if len(self._recipes) <= 5:
            return self._recipes
        recipes = DynamicArray()
        missed_ingredients_list = self.missed_ingredients_count()
        while len(recipes) != 5:
            missed_ingredient = min(missed_ingredients_list)
            for item in self._recipes:
                if len(recipes) == 5:
                    break
                if item[2] == missed_ingredient:
                    recipes.append(item)
            missed_ingredients_list.remove(missed_ingredient)
        self._recipes = recipes

    def nutrients_per_day(self):
        """
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

