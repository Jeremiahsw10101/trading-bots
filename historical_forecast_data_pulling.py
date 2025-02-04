import datetime as dt
from meteomatics.api import query_time_series

# Meteomatics API credentials
username = 'woldabezgi_woldabezgi_jeremiah'
password = 'bcX92Y1PhM'

# Coordinates for Central Park, New York
coordinates = [(40.7829, -73.9654)]

# Parameter for 2-meter temperature in Celsius
parameters = ['t_2m:C']

# Define the forecast issue date (two days ago)
forecast_issue_date = dt.datetime.now() - dt.timedelta(days=2)

# Define the forecast target date (yesterday)
forecast_target_date = forecast_issue_date + dt.timedelta(days=1)

# Fetch hourly temperature data for the target date as forecasted on the issue date
startdate = forecast_target_date
enddate = forecast_target_date + dt.timedelta(days=1)
interval = dt.timedelta(hours=1)

# Query the Meteomatics API
df = query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model='mix')

# Display the forecasted hourly temperatures
for timestamp, row in df.iterrows():
    temp_celsius = row['t_2m:C']
    temp_fahrenheit = temp_celsius * 9/5 + 32
    print(f"{timestamp}: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F")