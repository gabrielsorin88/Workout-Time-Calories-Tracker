# Workout-Time-Calories-Tracker
The app converts a natural language input from the user into workout data which it saves in a Google Sheets Spreadsheet.
The user can specify the exercise and the duration, or the distance,using natural language, and the app will convert the 
input into workout data, estimating the calories (if not specified), duration (if not specified), giving the formal name 
for the exercise, and getting today's date and time, which then posts into a Google spreadsheet.

To convert natural language to workout data, I've used the Nutritionix API with a post request, which requires an app ID 
and an app key for authentication (hiden using.env) and the user's input about his training as well as his weight, height,
age, and gender to provide an accurate estimation of the calories burned during the exercises.

From the JSON-converted file that the post request provided, the specific data needed for the Google sheet is extracted,
saved as a variable, and passed to the Sheety API (hidden using.env). The POST request saves the data to the specified 
spreadsheet.
![Image 30 11 2023 at 08 17](https://github.com/gabrielsorin88/Workout-Time-Calories-Tracker/assets/126314730/b37e27eb-d9c3-4d93-b58f-f4b9c6902b31)
![Image 30 11 2023 at 08 20](https://github.com/gabrielsorin88/Workout-Time-Calories-Tracker/assets/126314730/270d5dd6-68a7-42d9-b70d-0e911007485e)
![Image 30 11 2023 at 08 20](https://github.com/gabrielsorin88/Workout-Time-Calories-Tracker/assets/126314730/dc56c7e0-31d2-44ed-ae4e-9ab83b67cea1)

