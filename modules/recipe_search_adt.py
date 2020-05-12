"""
Module that represents the ADT for getting recipe data
from json and helping to select needed info
due to the certain search.
"""
from modules.arrays import Array, DynamicArray


# Works with data from API with such requests as
# complexSearch, mealplans/generate


class RecipeSearch:
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

    def amount_of_recipes(self):
        """(Recipe)

        Returns the amount of recipes.
        """
        return len(self._recipes)

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

    def recipe_selector(self):
        """
        Selects recipes.
        """
        recipes = DynamicArray()
        res_names = self.recipe_names()
        k = 0
        for recipe in res_names:
            if recipe not in recipes:
                recipes.append(recipe)
                k += 1
            if k == 5:
                break
        return recipes

    def delete_recipes(self):
        """
        Deletes recipes.
        """
        if len(self._recipes) > 5:
            new_recipes = Array(5)
            recipes = self.recipe_selector()
            k = 0
            for item in self._recipes:
                if item[1] in recipes:
                    new_recipes[k] = item
                    recipes.remove(item[1])
                    k += 1
                if len(recipes) == 0:
                    break
                self._recipes = new_recipes

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
