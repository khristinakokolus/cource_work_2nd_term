"""Module that represents ADT for getting more information about recipes"""
from modules.arrays import Array, DynamicArray


class RecipeData:
    """Represents data container class for the recipe analysis"""
    def __init__(self, data, recipes, amount_of_recipes):
        """(RecipeData, str, array, int)

        Creates a new object of RecipeData class.
        """
        self.data = data
        self._recipes = recipes
        self._main_info = DynamicArray()
        self._nutrients = DynamicArray()
        self._ingredients = DynamicArray()
        self._arr_size = amount_of_recipes

    def add_data(self, main_information):
        """(RecipeData, list)

        Adds the all needed information about
        all the recipes.
        """
        for i in range(len(self.data)):
            ingredients = self.get_ingredients(i)
            nutrients = self.recipe_nutrition(i)
            main_info = self.recipes_main_information(main_information, i)
            self._nutrients.append(nutrients)
            self._main_info.append(main_info)
            self._ingredients.append(ingredients)

    def recipe_nutrition(self, index):
        """(RecipeData, int)

        Gets nutrition of the one recipe.
        """
        temp_array = DynamicArray()
        for nutrients in self.data[index]['nutrition']['nutrients']:
            title = nutrients['title']
            value = nutrients['amount']
            unit = nutrients['unit']
            daily_needs = nutrients["percentOfDailyNeeds"]
            nutrients_pair = (title, value, unit, daily_needs)
            temp_array.append(nutrients_pair)
        return temp_array

    def recipes_main_information(self, main_info, index):
        """(RecipeData, list, int)

        Gets the main needed information about one recipe.
        """
        temp_array = DynamicArray()
        for key, value in self.data[index].items():
            if key in main_info:
                val_pair = (key, value)
                temp_array.append(val_pair)
        return temp_array

    def get_ingredients(self, index):
        """(RecipeData, int)

        Gets the ingredients of recipes.
        """
        temp_array = DynamicArray()
        data = self.data[index]['nutrition']['ingredients']
        for item in data:
            name = item['name']
            amount = item['amount']
            unit = item['unit']
            ingr_pair = str(amount) + " " + str(unit) + " " + str(name)
            temp_array.append(ingr_pair)
        return temp_array

    def ingredients(self):
        """(RecipeData) -> DynamicArray

        Returns the array of arrays
        with the ingredients of all
        dishes.
        """
        return self._ingredients

    def recipes(self):
        """(RecipeData) -> DynamicArray

        Returns the array of the names
        of recipes.
        """
        return self._recipes

    def healthiness(self):
        """(RecipeData) -> Array

        Returns the array of values healthy or not healthy
        that correspond to the recipes.
        """
        healthy_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[0][1] is False:
                value = "not healthy"
            else:
                value = "healthy"
            healthy_array[k] = value
            k += 1
        return healthy_array

    def cheap(self):
        """(RecipeData) -> Array

        Returns the array of values cheap or not cheap
        of all recipes.
        """
        cheap_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[1][1] is False:
                value = "not cheap to cook"
            else:
                value = "cheap to cook"
            cheap_array[k] = value
            k += 1
        return cheap_array

    def is_popular(self):
        """(RecipeData) -> Array

        Returns the array of values popular or not popular
        of all recipes.
        """
        popularity_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[2][1] is False:
                value = "not popular"
            else:
                value = "popular"
            popularity_array[k] = value
            k += 1
        return popularity_array

    def healthy_score(self):
        """(RecipeData) -> Array

        Returns the array of values of health score
        of all recipes.
        """
        healthy_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            healthy_array[k] = item[3][1]
            k += 1
        return healthy_array

    def time_cooking(self):
        """(RecipeData) -> Array

        Returns the array of values of cooking time
        of all recipes.
        """
        time_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            value = str(item[4][1]) + " minutes"
            time_array[k] = value
            k += 1
        return time_array

    def get_recipe_urls(self):
        """(RecipeData) -> Array

        Returns the array of urls
        of all recipes.
        """
        urls_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            urls_array[k] = item[5][1]
            k += 1
        return urls_array

    def search_cuisines(self):
        """(RecipeData) -> Array

        Returns the array of cuisines
        of all recipes.
        """
        cuisines_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[6][1] == []:
                cuisines_array[k] = "no information"
            else:
                cuisines_array[k] = item[6][1]
            k += 1
        return cuisines_array

    def search_types(self):
        """(RecipeData) -> Array

        Returns the array of dish types
        of all recipes.
        """
        types_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[7][1] == []:
                types_array[k] = "no information"
            else:
                types_array[k] = item[7][1]
            k += 1
        return types_array

    def search_diets(self):
        """(RecipeData) -> Array

        Returns the array of diets
        of all recipes.
        """
        diets_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[8][1] == []:
                diets_array[k] = "no information"
            else:
                diets_array[k] = item[8][1]
            k += 1
        return diets_array

    def calories(self):
        """(RecipeData) -> Array

        Returns the array of the calories amount
        of all recipes.
        """
        calories_array = Array(self._arr_size)
        k = 0
        for item in self._nutrients:
            value = str(item[0][1]) + " cal"
            calories_array[k] = value
            k += 1
        return calories_array

    def count_main_substances(self, main_substances, index):
        """(RecipeData, list, int) -> int

        Returns the amount of main nutrients in the
        dish.
        """
        count = 0
        for nutrient in self._nutrients[index]:
            if nutrient[0] in main_substances:
                count += 1
        return count

    def main_nutrients_percents(self, main_substances, index):
        """(RecipeData, list, int) -> Array

        Returns the array of two arrays that consist
        of the names of main nutrients with amounts
        and the percents of daily needs.
        """
        information = Array(2)
        length = self.count_main_substances(main_substances, index)
        main_nutrients = Array(length)
        main_percents = Array(length)
        k = 0
        for i in range(len(self._nutrients[index])):
            if self._nutrients[index][i][0] in main_substances:
                name = self._nutrients[index][i][0]
                value = self._nutrients[index][i][1]
                unit = self._nutrients[index][i][2]
                percent = int(self._nutrients[index][i][3])
                new_subs = name + " " + str(value) + unit
                main_nutrients[k] = new_subs
                main_percents[k] = percent
                k += 1
            if k == length:
                break
        information[0] = main_nutrients
        information[1] = main_percents
        return information

    def other_nutrients_percents(self, main_substances, index):
        """(RecipeData, list, int) -> Array

        Returns the array of two arrays that consist
        of the names of vitamins, minerals, etc with amounts
        and the percents of daily needs.
        """
        information_other = Array(2)
        length = len(self._nutrients[index]) - 1 -\
                 self.count_main_substances(main_substances, index)
        other_nutrients = Array(length)
        other_percents = Array(length)
        k = 0
        for i in range(len(self._nutrients[index])):
            if self._nutrients[index][i][0] not in main_substances and\
                    i != 0:
                name = self._nutrients[index][i][0]
                value = self._nutrients[index][i][1]
                unit = self._nutrients[index][i][2]
                percent = int(self._nutrients[index][i][3])
                new_subs = name + " " + str(value) + unit
                other_nutrients[k] = new_subs
                other_percents[k] = percent
                k += 1
        information_other[0] = other_nutrients
        information_other[1] = other_percents
        return information_other
