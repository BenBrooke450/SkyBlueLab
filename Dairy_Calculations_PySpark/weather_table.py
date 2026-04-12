def get_weather_data(country_name: str):
    import os
    import sys
    import pandas as pd
    import requests
    import plotly.express as px
    from pyjstat import pyjstat

    locations = {
        "Austria": {"lat": 48.21, "lon": 16.37},
        "Belgium": {"lat": 50.85, "lon": 4.35},
        "Bulgaria": {"lat": 42.69, "lon": 23.32},
        "Croatia": {"lat": 45.81, "lon": 15.97},
        "Cyprus": {"lat": 35.18, "lon": 33.38},
        "Czech Republic": {"lat": 50.07, "lon": 14.43},
        "Denmark": {"lat": 55.67, "lon": 12.56},
        "Estonia": {"lat": 59.43, "lon": 24.75},
        "Finland": {"lat": 60.16, "lon": 24.93},
        "France": {"lat": 48.85, "lon": 2.35},
        "Germany": {"lat": 52.52, "lon": 13.40},
        "Greece": {"lat": 37.98, "lon": 23.72},
        "Hungary": {"lat": 47.49, "lon": 19.04},
        "Ireland": {"lat": 53.34, "lon": -6.26},
        "Italy": {"lat": 41.90, "lon": 12.49},
        "Latvia": {"lat": 56.94, "lon": 24.10},
        "Lithuania": {"lat": 54.68, "lon": 25.27},
        "Luxembourg": {"lat": 49.61, "lon": 6.13},
        "Malta": {"lat": 35.89, "lon": 14.51},
        "Netherlands": {"lat": 52.36, "lon": 4.90},
        "Poland": {"lat": 52.22, "lon": 21.01},
        "Portugal": {"lat": 38.72, "lon": -9.13},
        "Romania": {"lat": 44.42, "lon": 26.10},
        "Slovakia": {"lat": 48.14, "lon": 17.10},
        "Slovenia": {"lat": 46.05, "lon": 14.50},
        "Spain": {"lat": 40.41, "lon": -3.70},
        "Sweden": {"lat": 59.32, "lon": 18.06}
    }

    all_weather_data = []

    for country, coords in locations.items():

        if country != country_name:
            continue

        api_url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&hourly=temperature_2m,relative_humidity_2m"

        try:
            response = requests.get(api_url, timeout=10)
            data = response.json()

            hourly = data.get("hourly", {})
            times = hourly.get("time", [])
            temps = hourly.get("temperature_2m", [])
            humidities = hourly.get("relative_humidity_2m", [])

            for i in range(len(times)):
                t = temps[i]
                rh = humidities[i]

                thi = (0.8 * t) + ((rh / 100) * (t - 14.4)) + 46.4

                all_weather_data.append(
                    {"Country": country, "Timestamp": times[i], "Temperature": t, "Humidity": rh, "THI": thi})


        except Exception as e:
            print(e)

    df = pd.DataFrame(all_weather_data)

    df = df[df["Country"] == country_name]

    return df

