"""Module that represents ADT for recipes analysis"""
from modules.arrays import Array, DynamicArray
BASE_URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"


class RecipeAdvanced:
    """Represents data container class for the recipe analysis"""
    def __init__(self, data, recipes, amount_of_recipes):
        self.data = data
        self._recipes = recipes
        self._main_info = DynamicArray()
        self._nutritions = DynamicArray()
        self._main_nutritions = DynamicArray()
        self._ingredients = DynamicArray()
        self._arr_size = amount_of_recipes

    def add_data(self, main_information):
        for i in range(len(self.data)):
            ingredients = self.get_ingredients(i)
            nutrients = self.recipe_nutrition(i)
            main_info = self.recipes_main_information(main_information, i)
            self._nutritions.append(nutrients)
            self._main_info.append(main_info)
            self._ingredients.append(ingredients)

    def recipe_nutrition(self, index):
        """
        Gets recipe nutrition
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
        temp_array = DynamicArray()
        for key, value in self.data[index].items():
            if key in main_info:
                val_pair = (key, value)
                temp_array.append(val_pair)
        return temp_array

    def get_ingredients(self, index):
        temp_array = DynamicArray()
        data = self.data[index]['nutrition']['ingredients']
        for item in data:
            name = item['name']
            amount = item['amount']
            unit = item['unit']
            ingr_pair = (name, amount, unit)
            temp_array.append(ingr_pair)
        return temp_array

    def is_healthy(self):
        healthy_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            healthy_array[k] = item[0][1]
            k += 1
        return healthy_array

    def cheap(self):
        cheap_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            cheap_array[k] = item[1][1]
            k += 1
        return cheap_array

    def is_popular(self):
        popularity_array = Array(self._arr_size)
        k = 0
        for item in self._main_info:
            popularity_array[k] = item[2][1]
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
        for item in self._nutritions:
            calories_array[k] = item[0][1]
            k += 1
        return calories_array

    def names_of_main_substances(self, main_substances, index):
        main_nutritions = DynamicArray()
        for i in range(len(self._nutritions[index])):
            if self._nutritions[index][i][0] in main_substances:
                new_subs = self._nutritions[index][i][0]
                main_nutritions.append(new_subs)
        return main_nutritions

    def names_of_all_substances(self, index):
        array_len = self._nutritions[index]
        all_nutritions = Array(array_len)
        for i in range(array_len):
            new_subs = self._nutritions[index][i][0]
            all_nutritions[i] = new_subs
        return all_nutritions

    def percents_of_daily_needs(self, index):
        array_len = self._nutritions[index]
        percents = Array(array_len)
        for i in range(array_len):
            new_subs = self._nutritions[index][i][3]
            percents[i] = new_subs
        return percents

    def biggest_percent_of_daily_needs(self):
        pass

    def smallest_percent_of_daily_needs(self):
        pass

    def nutrient_with_biggest_amount(self):

        pass

    def nutrient_with_smallest_amount(self):
        pass

    def main_substances_nutrition(self, main_substances, index):
        array_len = len(self.names_of_main_substances(main_substances, index))
        main_subs = Array(array_len)
        main_subs_names = self.names_of_main_substances(main_substances, index)
        j = 0
        for i in range(len(self._nutritions[index])):
            if self._nutritions[index][i][0] in main_subs_names:
                print(self._nutritions[index][i][0])
                new_value = self._nutritions[index][i][1]
                if self._nutritions[index][i][2] == "mg":
                    new_value = new_value / 1000
                main_subs[j] = new_value
                j += 1
            if j == array_len:
                break
        return main_subs

    def other_substances_nutrition(self, main_substances, index):
        array_len = len(self._nutritions[index]) - \
                    len(self.names_of_main_substances(main_substances, index)) - 1
        main_subs = Array(array_len)
        main_names_of_subs = Array(array_len)
        main_array = Array(2)
        j = 0
        for i in range(len(self._nutritions[index])):
            if self._nutritions[index][i][0] not in main_substances \
                    and i != 0:
                new_value = self._nutritions[index][i][1]
                subs_name = self._nutritions[index][i][0]
                if self._nutritions[index][i][2] == "µg":
                    new_value = new_value / 1000000
                elif self._nutritions[index][i][2] == "mg":
                    new_value = new_value / 1000
                elif self._nutritions[index][i][2] == "IU":
                    new_value = new_value * 0.67 / 1000
                main_subs[j] = new_value
                main_names_of_subs[j] = subs_name
                j += 1
        main_array[0] = main_names_of_subs
        main_array[1] = main_subs
        return main_array

