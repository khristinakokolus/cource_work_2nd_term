"""Module that contains needed default variables"""

DEFAULT_INFO_URL = 'information'

DEFAULT_COMPLEX_URL = 'complexSearch'

DEFAULT_MEAL_PLANNER_URL = 'mealplans/generate'

DEFAULT_DICT_MEALS_VALUES = ["timeFrame", "targetCalories", "diet", "exclude"]

DEFAULT_DICT_COMPLEX = ["query", "cuisine", "diet", "includeIngredients", "excludeIngredients", "type", "number"]

CUISINES = ["African", "American", "British", "Cajun", "Carribean", "Chinese",
            "Eastern", "European", "French", "German", "Greek", "Indian", "Irish",
            "Italian", "Japanese", "Jewish", "Korean", "Latin American", "Mediterranean",
            "Mexican", "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"]

DISH_TYPE = ["main course", "side dish", "dessert", "appetizer", "salad", "bread",
             "breakfast", "soup", "beverage", "sauce", "marinade", "fingerfood", "snack", "drink"]

DIETS = ["gluten free", "ketogenic", "vegetarian", "lacto vegetarian", "ovo vegetarian",
         "vegan", "pescetarian", "paleo", "primal"]

DEFAULT_MAIN_INFO = ["veryHealthy", "cheap", "veryPopular", "healthScore", "readyInMinutes", "sourceUrl",
                     "cuisines", "dishTypes", "diets"]

MAIN_NUTRIENTS = ["Fat", "Saturated Fat", "Carbohydrates", "Net Carbohydrates",
                   "Sugar", "Sodium", "Protein", "Fiber"]
