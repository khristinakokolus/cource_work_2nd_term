"""Module that represents ADT for getting more information about recipes"""
from modules.arrays import Array, DynamicArray


class RecipeData:
    """Represents data container class for the recipe analysis"""
    def __init__(self, data, recipes, amount_of_recipes):
        """(RecipeAdvanced, str, array, int)

        Creates a new objects of RecipeAdvanced class.
        """
        self.data = data
        self._recipes = recipes
        self._main_info = DynamicArray()
        self._nutrients = DynamicArray()
        self._ingredients = DynamicArray()
        self._arr_size = amount_of_recipes

    def add_data(self, main_information):
        """(RecipeAdvanced, list)

        Adds the all needed information about all the recipes.
        """
        for i in range(len(self.data)):
            ingredients = self.get_ingredients(i)
            nutrients = self.recipe_nutrition(i)
            main_info = self.recipes_main_information(main_information, i)
            self._nutrients.append(nutrients)
            self._main_info.append(main_info)
            self._ingredients.append(ingredients)

    def recipe_nutrition(self, index):
        """(RecipeAdvanced, int)

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
        """(RecipeAdvanced, list, int)

        Gets the main needed info about recipes.
        """
        temp_array = DynamicArray()
        for key, value in self.data[index].items():
            if key in main_info:
                val_pair = (key, value)
                temp_array.append(val_pair)
        return temp_array

    def get_ingredients(self, index):
        """(RecipeAdvanced, int)

        Gets the ingredients of recipes.
        """
        temp_array = DynamicArray()
        data = self.data[index]['nutrition']['ingredients']
        for item in data:
            name = item['name']
            amount = item['amount']
            unit = item['unit']
            ingr_pair = (name, amount, unit)
            temp_array.append(ingr_pair)
        return temp_array

    def recipes(self):
        """
        Returns the array of recipes.
        """
        return self._recipes

    def healthiness(self):
        """
        Returns the list of boolean values
        of the healthiness of the recipes.
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
        cheap_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[0][1] is False:
                value = "not cheap to cook"
            else:
                value = "cheap to cook"
            cheap_array[k] = value
            k += 1
        return cheap_array

    def is_popular(self):
        popularity_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            if item[0][1] is False:
                value = "not popular"
            else:
                value = "popular"
            popularity_array[k] = value
            k += 1
        return popularity_array

    def healthy_score(self):
        healthy_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            healthy_array[k] = item[3][1]
            k += 1
        return healthy_array

    def time_cooking(self):
        time_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            time_array[k] = item[4][1]
            k += 1
        return time_array

    def get_recipe_urls(self):
        urls_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            urls_array[k] = item[5][1]
            k += 1
        return urls_array

    def search_cuisines(self):
        cuisines_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            cuisines_array[k] = item[6][1]
            k += 1
        return cuisines_array

    def search_types(self):
        types_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            types_array[k] = item[7][1]
            k += 1
        return types_array

    def search_diets(self):
        diets_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            diets_array[k] = item[8][1]
            k += 1
        return diets_array

    def calories(self):
        calories_array = Array(self._arr_size)
        k = 0
        for item in self._nutrients:
            calories_array[k] = item[0][1]
            k += 1
        return calories_array

    def count_main_substances(self, main_substances, index):
        count = 0
        for nutrient in self._nutrients[index]:
            if nutrient[0] in main_substances:
                count += 1
        return count

    def main_substances_nutrition_percents(self, main_substances, index):
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

    def other_substances_nutrition_percents(self, main_substances, index):
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
                new_subs = new_subs = name + " " + str(value) + unit
                other_nutrients[k] = new_subs
                other_percents[k] = percent
                k += 1
        information_other[0] = other_nutrients
        information_other[1] = other_percents
        return information_other

    def ingredients_data_per_recipe(self, index):
        ingredients_data = DynamicArray()
        for item in self._ingredients[index]:
            value = item[0] + str(item[1]) + item[2]
            ingredients_data.append(value)
        return ingredients_data
