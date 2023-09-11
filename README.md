# MuhammadShahab00-CS50-Introduction-to-Programming-with-Python-Problem-Sets-Final-Project
Project Title : **Electric Vehicle Charging Scheduler**
Video Demo: https://www.youtube.com/watch?v=O2hBcDCqVZQ&t=10s

**Introduction**

This project is designed to optimize the charging schedule of an electric vehicle (EV) based on a variety of inputs including user preferences, electricity pricing trends, and the current battery status of the vehicle. The central objective is to find the most cost-effective time to charge the vehicle within a preferred timeframe specified by the user while ensuring that the vehicle is sufficiently charged for the next trip.

**Objective**

The key objective is to leverage data and predictive modeling to:

1: Minimize the cost of charging the EV by identifying the hours with the lowest electricity prices.
2: Meet the user’s charging preferences and ensure the car is adequately charged for the next trip.
3: Provide visual insights into the electricity prices, battery status, and the recommended charging schedule through data visualization.

**Algorithm and Logic Explained**

The project leverages a simple machine learning model and predictive analytics to find the optimal charging schedule. Here is a step-by-step explanation of the algorithm and its underlying logic:

***Data Generation and Retrieval***

1: **User Preferences**: Retrieve the user's preferred start and end times for charging.
2: **Electricity Prices**: Generate a random set of hourly electricity prices for a 24-hour period.
3: **Battery Status**: Get the current battery status, represented as a random percentage between 10% and 90%.
4  **Next Trip Time**: Find out the time of the user's next trip, generated randomly within the next 24 hours.

***Predictive Model Training***

1: **Model Training**: A linear regression model is trained using the 24-hour electricity price data to predict the electricity prices for the upcoming hours.

***Optimization of Charging Schedule***

1: **Predicted Prices**: Using the trained model, the electricity prices for the next 24 hours are predicted.
2: **Hours to Charge**: Calculate the required hours to charge the battery to full based on the current battery status.
3: **Best Time to Charge**: Identify the best time to initiate the charging process within the user-preferred timeframe such that it ensures the lowest cost while meeting the charging needs before the next trip. This part of the algorithm handles different cases including crossing midnight and the next trip time to find a suitable charging start time.

# Explaination with Example for Better Understanding of the Optimization Algorithm

Assume that Shahab prefers his EV (Electric Vehicle) to be charged between 10:00 PM (22:00) to 6:00 AM (06:00) the next day. Currently, the battery is 40% charged, and Shahab has a trip scheduled for 8:00 AM.

Given this scenario, let's see how the optimize_charging_schedule function helps find the best time for Shahab to start charging his EV.

**Step 1: Calculate the Required Charging Duration**
To find out how long it will take to fully charge the battery from a 40% charge level, we use the formula:

hours_to_charge = (100 - battery_status) / 20
# Substituting the given battery_status of 40
hours_to_charge = (100 - 40) / 20
hours_to_charge = 3 hours

So, the car needs 3 hours to be fully charged.

**Step 2: Predict the Electricity Prices for the Next 24 Hours**
Using a predictive model, we forecast the electricity prices for each hour of the next day. This is done with the line:

predicted_prices = model.predict(np.array(list(range(24))).reshape(-1, 1))

**Step 3: Finding the Cheapest Time to Charge within the Preferred Time Frame**

In this step, the function checks the predicted prices between 10:00 PM and 6:00 AM to find the cheapest hour to start charging. The code segment:

if start < end:
    best_time = start + predicted_prices[start:end].tolist().index(min(predicted_prices[start:end]))
else:
    best_time = predicted_prices[start:].tolist().index(min(predicted_prices[start:])) + start
    if best_time >= 24:
        best_time -= 24

Deals with finding the optimal charging time in two scenarios:

1: ***The charging window doesn't cross midnight (start time is less than the end time)***: It finds the hour with the lowest predicted electricity price within this window, setting it as the best_time.

2: ***The charging window crosses midnight (start time is greater than or equal to the end time)***: It considers the period from the start time to midnight and from midnight to the end time to find the hour with the minimum predicted price, setting it as the best_time. If the best time is 24 or higher, it adjusts it to represent the correct hour in a 24-hour format.

In our scenario with Shahab, the window is from 10:00 PM to 6:00 AM, crossing midnight, so the second scenario applies. Let's say that the lowest price occurs at 3:00 AM. Initially, the function selects this as the best time to start charging.

**Step 4: Adjusting the Time to Ensure the Car is Fully Charged by Next Trip**

Now, we ensure that starting to charge at 3:00 AM allows the battery to be fully charged by 8:00 AM (next trip time). If we start charging at 3:00 AM, it will be fully charged by 6:00 AM, which is before the next trip time.

However, if the best time was later, such that the car wouldn't fully charge before the trip time, the function would adjust the start time to ensure the car is fully charged before the next trip.

if best_time + hours_to_charge > next_trip_time:
    best_time = next_trip_time - hours_to_charge
    if best_time < 0:
        best_time += 24

**Step 5: Getting the Result**

The function then returns this best_time (3:00 AM in this case), indicating the optimal time to start charging, considering both the electricity prices and the need to have the car fully charged by the next trip time.

Therefore, Shahab should start charging his EV at 3:00 AM to make the most of the lowest electricity rate while ensuring his car is fully charged for his trip at 8:00 AM


***Visualization***

1: **Electricity Prices**: Visualize the hourly electricity prices in a line plot to give a graphical representation of the price trend.
2: **Battery Status**: Display the current battery status in a bar chart.
3: **Charging Schedule**: Visualize the recommended charging schedule in a bar chart, highlighting the user-preferred timeframe and the optimized start time for charging.

Through this algorithm, the script provides a simple yet effective way to determine the most cost-effective charging schedule, aligning with user preferences and the vehicle's battery needs, while offering a visual representation of various data points to the user.




