Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import project

def test_get_user_preferences():
    start, end = project.get_user_preferences()
    assert 0 <= start < 24 and 0 <= end < 24, f"Expected hours to be between 0 and 23, but got {start} and {end}"


def test_get_electricity_price():
    prices = project.get_electricity_price()
    assert len(prices) == 24, f"Expected 24 hourly prices, but got {len(prices)}"


def test_get_battery_status():
    status = project.get_battery_status()
    assert 0 <= status <= 100, f"Expected battery status to be between 0% and 100%, but got {status}%"


def test_get_next_trip_time():
    trip_time = project.get_next_trip_time()
    assert 0 <= trip_time < 24, f"Expected trip time to be between 0 and 23, but got {trip_time}"


def test_train_price_prediction_model():
    prices = project.get_electricity_price()
    model = project.train_price_prediction_model(prices)
    assert model is not None, "Expected model to be trained"


def test_optimize_charging_schedule():
    user_preferences = project.get_user_preferences()
    electricity_prices = project.get_electricity_price()
    battery_status = project.get_battery_status()
    next_trip_time = project.get_next_trip_time()

    model = project.train_price_prediction_model(electricity_prices)
    ideal_time = project.optimize_charging_schedule(user_preferences, model, battery_status, next_trip_time)

    assert 0 <= ideal_time < 24, f"Expected best charging time to be between 0 and 23, but got {ideal_time}"


# Run the tests
if __name__ == "__main__":
    test_get_user_preferences()
    test_get_electricity_price()
    test_get_battery_status()
    test_get_next_trip_time()
    test_train_price_prediction_model()
    test_optimize_charging_schedule()
    print("All tests passed!")
