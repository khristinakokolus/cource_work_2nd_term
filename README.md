## Project name: Recipe Selector and Analyzer

Welcome to Recipe Selector and Analyzer!

This web app is already hosted on pythonanywhere.com

Video presentation of the project: [Recipe Selector and Analyzer preview](https://www.youtube.com/watch?v=dhsA0brg_2o)

Check it now [Recipe Selector and Analyzer](http://recipeanalyser.pythonanywhere.com/)

## Description:

There are a lot of recipes but to find one that is really great is hard. Recipe Selector and Analyzer is created to solve this problem. It gives a great opportunity to find the dreamed recipe. There are a lot of recipes in the google but there is information only from what and how to cook the dish, but Recipe Selector and Analyzercan help to different recipes and to get the full information about them. To search the recipes you can use two oprions: Complex Search and Meal Generator. Complex search is a search that helps to find recipes based on the user's wishes. Meal Generator is used to generate recipes for the day. The information that user can get includes comparison characteristics of the recipes and nutrition composition.

## Table of contents:

* [Input/Output](#Input/Output)

* [Program Structure](#Structure)

* [Installation](#Installation)

* [Usage example](#Usage)

* [Contributing](#Contributing)

* [Credit](#Credit)

* [Licence](#Licence)

## Input/Output data

The input data for the Complex Search: main ingredient, ingredients to include and to exclude, cuisine, diet, dish type, the number of recipes to output. It is ESSENTIAL to input the main ingredient and number of recipes, but other input is optional.

The input data for the Meal Generator: number of calories, diet, ingredients to exclude. User сan not even enter anything and press the button to get the results. Using this option user can get only three recipes.


The output data of the Recipe Selector and Analyzer for Complex Search and Meal Generator are rather the same:
* table with comparative characteristics of selected recipes:
  * healthiness;
  * health score;
  * popularity;
  * cheap to cook or not;
  * cooking time;
  * number of calories;
  * cuisines they belong to;
  * diets they belong to;
  * dish types they belong to;
* table with the ingredients you need for a portion of the dishes separately;
* bar charts with all recipes' nutrition composition that provide their analysis;
* all recipes' links;

If user uses Meal Generator, there is also displayed the pie chart with the the comparison of fats, carbohydrates and protein in dishes per day.

## Program structure

Program consists of such modules as:
* arrays.py - contains needed data structures for the investigation. They are Array and Dynamic Array that are needed to for the ADT implementation.
* recipe_search_adt.py - contains needed RecipeSearch ADT. This ADT is used to get the information about recipes' names and ids.RecipeSearch ADT also helps to select the recies in a random way.
* recipe_data_adt.py - contains needed ADT SecipeData ADT. This ADT is used as a cintainer of the main information about selected recipes and used to obtain the information needed for analysis.
* default_information - consists of the needed default information for the investigation such as list of needed diets, dish types, cuisines, etc.
* errors.py - there are dictionaries what returns API if it is a bad request. This module is used to define whether there are results for different user inputs.
* main_functions.py - consists of the functions that are needed to get the information using API, there are functions to check the if user's input is valid and if the information from the Internet is not in errors.py. also, there are needed functions to plot the data for both Complex Search and Meal Generator.
* complex_dashboard - contains the main function to get the information for the Complex Search and also there is Dash layout that is responsible for the output results of the data analysis for Complex Search.
* meal_gen_dashboard - contains of the function to plot the needed data for the Meal Generator and also there is Dash layout that is responsible for the output results of the data analysis for Meal Genarator.
* flask_app.py - contains of hree functions to create three main pages of the app: home, Complex Search and Meal Generator.
* wsgi.py - is responsible for the transition between the flask pages and dash pages.

If you want to know more just have a look at the documentation page, that consistsof the all neede information about main classes and functions. 

## Installation:

### Prerequisities:

If you want to run the program locally you need firstly to install such libraries:

`pip install requests`

`pip install flask`

`pip install dash`

`pip install plotly`

`pip install pandas`

Also you need to get an API key on [Rapid API](https://rapidapi.com/spoonacular/api/recipe-food-nutrition)

Then you need only:

`git clone https://github.com/khristinakokolus/cource_work_2nd_term.git`

Then you shound run wsgi.py to see the work of the program.

## Usage

After following the link of the site you will see:

![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/home.png)

After that you can choose Complex Search or Meal Generator

If you chose Complex Search, you will see:

![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/complex.png)

Here is example of search query:

![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/complexsearch.png)

Example of output data:

![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res1.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res2.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res3.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res4.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res5.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res6.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res7.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/res8.png)


If you chose Meal Generator, you will see:

![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal_gen.png)

Here is example of search query:

![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/mealgenerator.png)


Example of output data:

![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal1.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal2.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal3.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal4.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal5.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal6.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal7.png)
![](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/screens/meal8.png)

## Contributing:

Please refer to project's style and contribution guidelines for submitting patches and additions. In general, the "fork-and-pull" Git workflow.

1.Fork the repo on GitHub

2.Clone the project to your own machine

3.Commit changes to your own branch

4.Push your work back up to your fork

5.Submit a Pull request so that we can review your changes

## Credit:
- Khrystyna Kokolus, Ukrainian Catholic University

## License:

[MIT LICENSE](https://github.com/khristinakokolus/cource_work_2nd_term/blob/master/LICENSE)
