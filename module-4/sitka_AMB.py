# sitka_high_low_<AMB>.py
# Author: <Alexander Baldree>
# Assignment: Module-4 - Sitka Highs/Lows Menu Program
# Changes Made:
# 1. Added menu when program starts (Highs, Lows, Exit)
# 2. Low-temperature graph option added (blue)
# 3. Loop continues until user selects Exit
# 4. Exit message added
# 5. Reused code structure from sitka_highs.py

import csv
import sys
from datetime import datetime
import matplotlib as plt

# ---------------------------------------------------------
# Function to read CSV data and return date, highs, lows
# ---------------------------------------------------------
def load_weather_data():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = [], [], []

    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], "%Y-%m-%d")
                    high = int(row[5])
                    low = int(row[6])
                except ValueError:
                    # Missing data; skip row
                    continue
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)

    except FileNotFoundError:
        print("\n❌ CSV file not found. Make sure sitka_weather_2018_simple.csv is in the same directory.")
        sys.exit()

    return dates, highs, lows


# ---------------------------------------------------------
# Function to plot either Highs or Lows
# ---------------------------------------------------------
def show_graph(dates, values, title, ylabel):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, linewidth=1)
    plt.title(title, fontsize=18)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# MAIN PROGRAM LOOP
# ---------------------------------------------------------
dates, highs, lows = load_weather_data()

while True:
    print("\n--- Sitka Weather Menu ---")
    print("1. High Temperatures (red)")
    print("2. Low Temperatures (blue)")
    print("3. Exit\n")

    choice = input("Select an option (1, 2, or 3): ")

    if choice == "1":
        show_graph(dates, highs, "Daily High Temperatures - Sitka, Alaska", "Temperature (°F)")

    elif choice == "2":
        show_graph(dates, lows, "Daily Low Temperatures - Sitka, Alaska", "Temperature (°F)")

    elif choice == "3":
        print("\n✅ Exiting program. Have a great day!")
        sys.exit()

    else:
        print("\n⚠️ Invalid option. Please choose 1, 2, or 3.")
