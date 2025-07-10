import pandas as pd

def london_bikes():
    # extract data and get info on bikes data
    bikes = pd.read_csv("data/london_merged.csv")
    bikes.info()

    # Get dimensions of the data
    print("\nData Dimensions: " + str(bikes.shape))

    # Get the number of unique values in the weather_code column
    print("\nNumber of unique values in the weather_code column:")
    print(bikes.weather_code.value_counts())

    # Get the number of unique values in the season column
    print("\nNumber of unique values in the season column:")
    print(bikes.season.value_counts())

    # Specify columns to use:
    new_cols_dict = {
        "timestamp":"time",
        "cnt":"count",
        "t1":"temp_real_C",
        "t2":"temp_feels_C",
        "hum":"humidity_percent",
        "wind_speed":"wind_speed_kph",
        "weather_code":"weather",
        "is_holiday":"is_holiday",
        "is_weekend":"is_weekend",
        "season":"season"
    }

    # Rename the columns (without creaing a new DataFrame)
    bikes.rename(new_cols_dict, axis=1, inplace=True)

    # Change the humidity values to an actual percentage (e.g. a value between 0 and 1)
    bikes.humidity_percent = bikes.humidity_percent / 100

    # create a season dictionary so that we can map the integers 0-3 to actual written values
    season_dict = {
        "0.0":"Spring",
        "1.0":"Summer",
        "2.0":"Autumn",
        "3.0":"Winter"
    }

    # Create a weather dictionary so we can map the integers to actual written values
    weather_dict = {
        "1.0":"Clear",
        "2.0":"Scattered Clouds",
        "3.0":"Broken Clouds",
        "4.0":"Cloudy",
        "7.0":"Rain",
        "10.0":"Rain With Thunderstorm",
        "26.0":"Snowfall"
    }

    # Change the seasons column data type to String
    bikes.season = bikes.season.astype("str")

    # Mapping the values 0-3 to the actual written seasons
    bikes.season = bikes.season.map(season_dict)

    # Change the weather column data type to String
    bikes.weather = bikes.weather.astype("str")

    # Mapping the weather numbers to the actual written weathers
    bikes.weather = bikes.weather.map(weather_dict)

    # Check DataFrame mapping correctness
    print("\nModified DataFrame: ")
    print(bikes.head())

    # Convert the DataFrame into an Excel file
    bikes.to_excel("london_bikes_final.xlsx", sheet_name="Data")

if __name__ == "__main__":
    london_bikes()