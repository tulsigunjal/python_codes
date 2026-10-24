"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data


"""
import csv
from collections import defaultdict   # It automatically provides a default value when you access a key that does not exist.
import matplotlib.pyplot as plt

FILENAME = "weather_logs.csv"
def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)  #A dictionary that counts how often each weather condition appears.

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)  #reads the CSV file and treats the first row as column names.
        for row in reader:
            try:
                dates.append(row["Date"])
                temps.append(row["Temperature"])
                conditions[row["Condition"]] += 1
            except:
                continue  #if an error occurs inside the try block, continue skips the current iteration and moves to the next row.
    if not dates:
        print("NO data is available")
        return
    
    plt.figure(figsize=(10, 7))  #sets its width to 10 inches and height to 7 inches.
    plt.plot(dates, temps, marker='o')
    plt.title("Temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values(), color='skyblue')
    plt.xlabel("Condition")
    plt.ylabel("Days")
    plt.show()



visualize_weather()