from dotenv import load_dotenv
import os
import requests
import datetime

load_dotenv()
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
USER_GENDER = os.getenv("USER_GENDER")
USER_WEIGHT_KG = os.getenv("USER_WEIGHT_KG")
USER_HEIGHT_CM = os.getenv("USER_HEIGHT_CM")
USER_AGE = os.getenv("USER_AGE")
SHEETY_POST_ENDPOINT = os.getenv("SHEETY_POST_ENDPOINT")

# user_input = input("Please input what you did today:\n")
user_input = "ran 3 miles"

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

nutritionix_request_body = {
    "query": user_input,
    "gender": USER_GENDER,
    "weight_kg": float(USER_WEIGHT_KG),
    "height_cm": float(USER_HEIGHT_CM),
    "age": int(USER_AGE)
}

nutritionix_response = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, json=nutritionix_request_body, headers=nutritionix_headers)
nutritionix_response.raise_for_status()
nutritionix_result = nutritionix_response.json()

# example_response = {"exercises": [
#     {"tag_id": 317, "user_input": "ran", "duration_min": 30.02, "met": 9.8, "nf_calories": 355.49,
#      "photo": {"highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg",
#                "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg", "is_user_uploaded": false},
#      "compendium_code": 12050, "name": "running", "description": null, "benefits": null}]}

now = datetime.datetime.now()
current_date = now.strftime("%m/%d/%Y")
current_time = now.strftime("%H:%M:%S")

for exercise in nutritionix_result["exercises"]:
    sheety_body = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"]),
            "calories": round(exercise["nf_calories"]),
        }
    }

    sheety_response = requests.post(url=SHEETY_POST_ENDPOINT, json=sheety_body)
