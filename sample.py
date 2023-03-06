from pvlib import solarposition, location, pvsystem
import pandas as pd

# Define location
latitude = 40.7
longitude = -74.0
tz = 'US/Eastern'

# Define location object
location = location.Location(latitude, longitude, tz)

# Get solar position data
start_date = pd.Timestamp('2023-03-06 12:00:00', tz=tz)
end_date = start_date + pd.Timedelta(hours=1)

# Get solar position data
times = pd.date_range(start_date, end_date, freq='1s', tz=tz)
solar_position = solarposition.get_solarposition(times, latitude, longitude)

# Define PV system parameters
system = pvsystem.PVSystem(surface_tilt=20, surface_azimuth=180, module_parameters=None, inverter_parameters=None)

# Get PV system performance data
irradiance = solar_position['dni']
temp_air = 20
wind_speed = 0
system_data = pvsystem.get_pvwatts_tmy(location, surface_tilt=20, surface_azimuth=180)

# Calculate DC and AC power output
dc = pvsystem.pvwatts_dc(irradiance, temp_air)
ac = pvsystem.pvwatts_ac(dc['p_dc'], temp_air, **system_data)

# Print AC power output
print(ac.sum())
