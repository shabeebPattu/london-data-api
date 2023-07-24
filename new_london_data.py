import requests

def get_weather_data(api_key, date):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    city_name = "London"
    url = f"{base_url}?q={city_name}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

   
    forecast_data = next(item for item in data["list"] if item["dt_txt"].startswith(date))

    temperature = forecast_data["main"]["temp"]
    wind_speed = forecast_data["wind"]["speed"]
    pressure = forecast_data["main"]["pressure"]

    return temperature, wind_speed, pressure


api_key = "6e5a74718162d859ec78432283552b83"
date = input("Enter the date (YYYY-MM-DD): ")
while True:
    print("Press 1 to display the temperature of London")
    print("Press 2 to display the windspeed of London")
    print("Press 3 to display the pressure of London")
    print("Press 0 to Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        temperature, _, _ = get_weather_data(api_key, date)
        print(f"Temperature in London on {date}: {temperature} K")
    elif choice == "2":
        _, wind_speed, _ = get_weather_data(api_key, date)
        print(f"Wind Speed in London on {date}: {wind_speed} m/s")
    elif choice == "3":
        _, _, pressure = get_weather_data(api_key, date)
        print(f"Pressure in London on {date}: {pressure} hPa")
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
