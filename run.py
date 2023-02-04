import csv


def run():

    # Mapping column names to the input data.
    #  * Column 1 - time
    #  * Column 2 - humidity
    #  * Column 3 - salinity
    #  * Column 4 - air_temperature
    #  * Column 5 - water_temperature
    #  * Column 6 - wind_speed

    # COLUMN_NAMES = [
    #     "time",
    #     "humidity",
    #     "salinity",
    #     "air_temperature",
    #     "water_temperature",
    #     "wind_speed"
    # ]

    # Load data from a local CSV file into a nested array
    data = []
    with open("data.csv") as csvdata:
        csv_reader = csv.reader(csvdata)
        for row in csv_reader:
            data.append(row)

    # Transpose the nested array
    transposed = list(map(list, zip(*data)))

    # Remove NaN values and cast to float
    for col_idx, col_data in enumerate(transposed):
        # Do not cast time column to float
        if col_idx == 0:
            continue
        transposed[col_idx] = [float(x) for x in col_data if not math.isnan(float(x))]

    def column_average(col_num):
        """Takes 1-indexed column number, returns the average of that column"""

        return sum(transposed[col_num - 1]) / len(transposed[col_num - 1])

    # Calculate the average of each column
    col_2_avg = column_average(2)
    col_3_avg = column_average(3)
    col_4_avg = column_average(4)
    col_5_avg = column_average(5)
    col_6_avg = column_average(6)

    # Return the averages of each column
    return {
        "humidity": col_2_avg,
        "salinity": col_3_avg,
        "air_temperature": col_4_avg,
        "water_temperature": col_5_avg,
        "wind_speed": col_6_avg,
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
