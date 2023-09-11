Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Project : Electric Vehicle Charging Scheduler

# Important Libraries need for this project
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def main():
    user_preferences = get_user_preferences()
    electricity_prices = get_electricity_price()
    battery_status = get_battery_status()
    next_trip_time = get_next_trip_time()

    print('User_preferences :', user_preferences)
    print('Electricity_prices :', electricity_prices)
    print('Battery_status :', battery_status)
    print('Next_trip_time :', next_trip_time)


    # Train a model to predict electricity prices
    model = train_price_prediction_model(electricity_prices)

    # Use the model to optimize charging times and costs
    Ideal_time_to_charge = optimize_charging_schedule(user_preferences, model, battery_status, next_trip_time)

    # Visualize outcomes
    visualize_electricity_prices(electricity_prices)
    visualize_battery_status(battery_status)
    visualize_charging_schedule(user_preferences, Ideal_time_to_charge)

    #print(f"Ideal time to start charging: {Ideal_time_to_charge} o'clock")

    print(f"Ideal time to start charging: {format_time(Ideal_time_to_charge)}")

# To represent time in a 24-hour format along with its respective AM/PM label,
def format_time(hour_24):
    """Converts 24-hour format time to 12-hour format with AM/PM label."""

    if 0 <= hour_24 < 12:
        am_pm = "AM"
        if hour_24 == 0:
            hour_24 = 12  # 0:00 in 24-hour is 12:00 AM in 12-hour format
    else:
        am_pm = "PM"
        if hour_24 > 12:
            hour_24 -= 12  # Convert 24-hour time to 12-hour time (for PM hours)

    return f"{hour_24:02}:00 {am_pm}"

#1: Data Generation and Retrieval#

# Retrieve user preferences for charging.
def get_user_preferences():
    start = random.randint(0, 23)
    end = random.randint(start, 23)
    return (start, end)

#Retrieve hourly electricity prices for the next 24 hours
def get_electricity_price():
    return [random.uniform(0.05, 0.25) for _ in range(24)]

#Retrieve the current battery status

def get_battery_status():
    return random.uniform(10, 90)

# Retrieve the time of the user's next trip.
def get_next_trip_time():
    return random.randint(0, 23)

#2: Predictive Model Training#

# Train a linear regression model to predict electricity prices.
def train_price_prediction_model(prices):
    hours = list(range(24))
    X = np.array(hours).reshape(-1, 1)
    y = prices
    model = LinearRegression().fit(X, y)
    return model

#3:Optimization of Charging Schedule

#Optimizing the charging schedule of an electric vehicle based on user preferences, electricity prices, and battery status

def optimize_charging_schedule(user_preferences, model, battery_status, next_trip_time):
    start, end = user_preferences
    hours_to_charge = (100 - battery_status) / 20  # Assuming 20% battery charge per hour

    # Predict prices for the next 24 hours
    predicted_prices = model.predict(np.array(list(range(24))).reshape(-1, 1))

    # Find the ideal time to start charging within user preferred time
    if start < end:
        ideal_time = start + predicted_prices[start:end].tolist().index(min(predicted_prices[start:end]))
    else:
        ideal_time = predicted_prices[start:].tolist().index(min(predicted_prices[start:])) + start
        if ideal_time >= 24:
            ideal_time -= 24

    # Ensure the car is charged by the next trip time
    if ideal_time + hours_to_charge > next_trip_time:
        ideal_time = next_trip_time - hours_to_charge
        if ideal_time < 0:
            ideal_time += 24

    return ideal_time

#4: Visualization


#Visualize the electricity prices.
def visualize_electricity_prices(prices):

    plt.plot(range(24), prices)
    plt.title("Hourly Electricity Prices")
    plt.xlabel("Hour")
    plt.ylabel("Price")
    plt.show()

#Visualize the battery status
def visualize_battery_status(status):

    plt.bar(["Battery Status"], [status], color=['blue'])
    plt.title("Battery Status")
    plt.ylabel("Charge (%)")
    plt.ylim(0, 100)
    plt.show()

#Visualize the changing schedule.
def visualize_charging_schedule(user_preferences, ideal_time):

    start, end = user_preferences
    plt.bar(range(24), [0] * 24, color='grey')
    plt.bar(range(start, end), [100] * (end - start), color='green', alpha=0.7)
    plt.axvline(x= ideal_time, color='red', linestyle='--', label="Ideal Time to Charge")
    plt.title("Charging Schedule")
    plt.xlabel("Hour")
    plt.ylabel("Charge (%)")
    plt.ylim(0, 110)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
