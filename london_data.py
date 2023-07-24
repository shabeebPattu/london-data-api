import requests

def get_weather(date,number):
    api_key='7a2977324f734c69a9c171319232407'
    city = 'London'

    if not city or not date:
        return {'error': 'Please provide a date.'}

    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=1&aqi=no&alerts=no'
    response = requests.get(url)
    data = response.json()

    try:
        forecast_data = next(item for item in data['forecast']['forecastday'] if item['date'] == date)
        temperature_c = forecast_data['day']['avgtemp_c']
        windspeed_kph = forecast_data['day']['maxwind_kph']
        pressure_mb = forecast_data['day']['totalprecip_mm']
        
        if number == 1:
            return temperature_c
        elif number == 2 :
            return windspeed_kph
        elif number == 3:
            return pressure_mb
        else:
            return "you have successfully exited "

    except StopIteration:
        return {'error': 'No data available for the given date'}

if __name__ == "__main__":
    date = input("Enter a date (YYYY-MM-DD): ")
    number=5
    while number != 0:
        number = int(input("""Enter the number from the list [1,2,3,0]
                    press 1 to display the temperature of London
                    press 2 to display the windspeed of London
                    press 3 to display the pressure of London
                    press 0 to Exit
                    """))

        if number == 0:
            print("Exiting from the game...")
            break

        result = get_weather(date, number)
        
        
        if number == 1:
            print(f"Temperature in London on {date}: {float(result)}°C")
        elif number == 2:
            print(f"Windspeed in London on {date}: {float(result)} kph")
        elif number == 3:
            print(f"Pressure in London on {date}: {float(result)} mb")
        else:
            print("Invalid number. Please try again.")
