import requests
import os
from dotenv import find_dotenv, load_dotenv
from datetime import datetime


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

#params For Exercise
GENDER = "male"
WEIGHT_KG = 93.2
HEIGHT_CM = 170.1
AGE = 35


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Which exercises did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id": "0"
}

params_exercise={
     "query":exercise_text,
     "gender":GENDER,
     "weight_kg":WEIGHT_KG,
     "height_cm":HEIGHT_CM,
     "age":AGE
}


response_exer = requests.post(exercise_endpoint, json=params_exercise, headers=headers)
data_exer=response_exer.json()
print(data_exer)

now_date= datetime.now().strftime('%d/%m/%Y')
now_time= datetime.now().strftime('%H:%M:%S')



#for params Sheety
EXERCISE = data_exer['exercises'][0]['name']
DURATION = data_exer['exercises'][0]['duration_min']
CALORIES = data_exer['exercises'][0]['nf_calories']
DATE = now_date
TIME = now_time




params_sheety = {
    "workout":{
        "date" : DATE,
        "time" : TIME,
        "exercise" : EXERCISE,
        "duration" : DURATION,
        "calories" : CALORIES,
    }
}

sheety_bearer = os.getenv("sheety_bearer")
sheety_headers = { "Authorization" : sheety_bearer }

sheety_endpoint = os.getenv("sheety_endpoint")

sheety_response = requests.post(sheety_endpoint, json=params_sheety, headers=sheety_headers)


