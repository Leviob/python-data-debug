import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

COLUMN_NAMES = [
    "time",
    "humidity",
    "salinity",
    "air_temperature",
    "water_temperature",
    "wind_speed",
]


def get_averages():
    """
    Returns dictionary of averages of CSV file

    The input data must have the following format:
    Column 1 - time
    Column 2 - humidity
    Column 3 - salinity
    Column 4 - air_temperature
    Column 5 - water_temperature
    Column 6 - wind_speed
    """

    # Organize data into a dataframe
    df = pd.read_csv("data.csv", names=COLUMN_NAMES, parse_dates=["time"])

    df["water_temp_diff"] = abs(df.water_temperature.diff())
    # print(df.water_temp_diff[abs(df.water_temp_diff) >= 2].count())

    # # Plot histogram of change in water temperature between readings, ignoring large differences
    # df.loc[abs(df.water_temp_diff) > 10, 'water_temp_diff'] = np.nan
    # plt.hist(df.water_temp_diff, bins=100)
    # plt.yscale('log')
    # plt.show()

    df["water_temp_no_outliers"] = df.water_temperature[
        (abs(df.water_temp_diff) < 2)
        & (df.water_temperature > 0)
        & (df.water_temperature < 100)
    ]

    # Plot water temperature over time
    fig, axs = plt.subplots(2, sharex=True)
    fig.subplots_adjust(hspace=0.5)
    fig.suptitle("Water Temperature")
    axs[0].scatter(df.time, df.water_temperature, marker=".")
    axs[0].set_title("Original Data")
    axs[1].scatter(df.time, df.water_temp_no_outliers, marker=".")
    axs[1].set_title("Outliers Removed")
    plt.show()

    # Return the averages of each column
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
    averages = get_averages()
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
