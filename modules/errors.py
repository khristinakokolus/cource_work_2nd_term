"""Module that contains of bad results from the API call"""

BAD_REQUEST = {
    "status": 404,
    "code": 0,
    "message": "We're so sorry, something went wrong. If this error persists, please contact us.",
    "link": "https://www.mashape.com/webknox/"
}

NO_RESULTS_MEALS = {
    "meals": [],
    "nutrients": {
        "calories": 0.0,
        "protein": 0.0,
        "fat": 0.0,
        "carbohydrates": 0.0
    }
}

NO_RESULTS_COMPLEX = {
    "results": [],
    "offset": 0,
    "number": 50,
    "totalResults": 0
}