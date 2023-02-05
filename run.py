import pandas as pd


def run():

    # Mapping column names to the input data.
    #  * Column 1 - time
    #  * Column 2 - humidity
    #  * Column 3 - salinity
    #  * Column 4 - air_temperature
    #  * Column 5 - water_temperature
    #  * Column 6 - wind_speed

    COLUMN_NAMES = [
        "time",
        "humidity",
        "salinity",
        "air_temperature",
        "water_temperature",
        "wind_speed",
    ]

    # Load data from CSV into dataframe
    df = pd.read_csv("data.csv", names=COLUMN_NAMES, parse_dates=["time"])

    # Return the means
    return {
        "humidity": df.humidity.mean(),
        "salinity": df.salinity.mean(),
        "air_temperature": df.air_temperature.mean(),
        "water_temperature": df.water_temperature.mean(),
        "wind_speed": df.wind_speed.mean(),
    }


if __name__ == '__main__':
    import sys
    import time
    import math

    start = time.perf_counter()
    averages = run()
    end = time.perf_counter()

    CORRECT_HUMIDITY = 80.8129
    CORRECT_SALINITY = 36.1433
    CORRECT_AIR_TEMPERATURE = 19.7976
    CORRECT_WIND_TEMPERATURE = 34.1683
    CORRECT_WIND_SPEED = 5.6777

    ANSWERS = {
        'humidity': CORRECT_HUMIDITY,
        'salinity': CORRECT_SALINITY,
        'air_temperature': CORRECT_AIR_TEMPERATURE,
        'water_temperature':CORRECT_WIND_TEMPERATURE,
        'wind_speed': CORRECT_WIND_SPEED,
    }

    for column, value in ANSWERS.items():
        assert math.isclose(
            averages[column],
            value,
            rel_tol=1e-5,
        ), f"{column} should be {value}, instead {averages[column]}"

    print("Succesfully validated the data using {} in {} seconds".format(__file__, end - start))

    sys.exit(0)
