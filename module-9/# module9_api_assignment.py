# module9_api_assignment.py
# Author: Alexander Baldree
# Assignment: Module 9 - API Tutorial

import requests
import json

# ----------------------------------------------------
# 1. TEST CONNECTION USING URL FROM THE READING LIST
#    (Usually: http://api.open-notify.org/astros.json)
# ----------------------------------------------------
test_url = "http://api.open-notify.org/astros.json"

print("=== TESTING CONNECTION TO OPEN-NOTIFY API ===")
test_response = requests.get(test_url)
print("Status Code:", test_response.status_code)
print()

# ----------------------------------------------------
# 2. RETRIEVE CURRENT ASTRONAUTS + FORMAT OUTPUT
# ----------------------------------------------------
if test_response.status_code == 200:
    data = test_response.json()

    print("=== CURRENT ASTRONAUTS (RAW JSON) ===")
    print(data)
    print()

    print("=== CURRENT ASTRONAUTS (FORMATTED OUTPUT) ===")
    print(f"Number of astronauts in space: {data['number']}")
    print("Names of astronauts currently in space:")
    for person in data['people']:
        print(f" - {person['name']} ({person['craft']})")
else:
    print("Error retrieving astronaut data.")

print("\n-----------------------------------------------\n")

# ----------------------------------------------------
# 3. SECOND API (your choice)
#    Example: Dog CEO Random Dog Picture API
# ----------------------------------------------------
api_url = "https://dog.ceo/api/breeds/image/random"

print("=== TESTING CONNECTION TO SECOND API ===")
api_response = requests.get(api_url)
print("Status Code:", api_response.status_code)
print()

# Print raw response
print("=== RAW API RESPONSE (NO FORMATTING) ===")
print(api_response.text)
print()

# Print formatted JSON
print("=== FORMATTED API RESPONSE ===")
try:
    formatted = api_response.json()
    print(json.dumps(formatted, indent=4))
except:
    print("Could not parse JSON response.")

print("\n=== END OF PROGRAM ===")
