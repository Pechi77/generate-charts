def weather_by_city(city):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(city)
    condition = location.condition
    current_condition=condition.text
    current_temp=location.print_obj["item"]["condition"]["temp"]
    forecasts = location.forecast
    weather_df=pd.DataFrame(columns=["Status","Date","High","Low"])
    for forecast in forecasts:
        weather_df=weather_df.append({"Status":forecast.text,"Date":forecast.date,"High":forecast.high,"Low":forecast.low},ignore_index=True)
    status_json=weather_df.to_json()
    return current_condition,current_temp,status_json
