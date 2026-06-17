import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

spreadsheet_api = os.getenv("GOOGLE_SPREADSHEET")
drive_api = os.getenv("GOOGLE_DRIVE")

scope = [spreadsheet_api,drive_api]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open("Workout Tracker").sheet1


EXERCISES = {
    "running": 10,
    "walking": 4,
    "cycling": 8,
    "jumping rope": 12,
    "pushups": 7
}

exercise = input("What exercise did you do? ").lower()
duration = int(input("How many minutes? "))

if exercise not in EXERCISES:
    print("Exercise not found")
    exit()


calories = EXERCISES[exercise] * duration

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

sheet.append_row([
    date,
    time,
    exercise,
    f"{duration} min",
    calories
])

print("\nWorkout saved successfully!")
print(f"Exercise: {exercise}")
print(f"Duration: {duration} minutes")
print(f"Calories burned: {calories}")