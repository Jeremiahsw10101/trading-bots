import datetime as dt
from meteomatics.api import query_time_series

# Meteomatics API credentials
username = 'woldabezgi_woldabezgi_jeremiah'
password = 'bcX92Y1PhM'

# Coordinates for Central Park, New York
coordinates = [(40.7829, -73.9654)]

# Parameter for 2-meter temperature in Celsius
parameters = ['t_2m:C']

# Define the date for February 4, 2025
date = dt.datetime(2025, 2, 4)

# Fetch hourly temperature data for the specified date
startdate = date
enddate = date + dt.timedelta(days=1)
interval = dt.timedelta(hours=1)

# Query the Meteomatics API
df = query_time_series(coordinates, startdate, enddate, interval, parameters, username, password)

# Display the hourly temperatures
for timestamp, row in df.iterrows():
    temp_celsius = row['t_2m:C']
    temp_fahrenheit = temp_celsius * 9/5 + 32
    print(f"{timestamp}: {temp_celsius:.2f}°C / {temp_fahrenheit:.2f}°F")