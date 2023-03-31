from astropy.time import Time
import pytest
from astropy.coordinates import EarthLocation, AltAz, ICRS, Angle, get_sun

# Define San Diego coordinates
latitude = 32.7157
longitude = -117.1611
elevation = 18  # meters above sea level

def trackSun():
    # Define EarthLocation object
    san_diego = EarthLocation(lat=latitude, lon=longitude, height=elevation)

    # Get current time in UTC
    time_utc = Time.now()

    # Calculate Local Sidereal Time (LST) at San Diego
    lst = time_utc.sidereal_time('mean', longitude=san_diego.lon)

    # Calculate Hour Angle (HA) at San Diego
    ha = lst - Angle(san_diego.lon)

    # Print the Hour Angle
    print(f"Current Hour Angle in San Diego: {ha.to_string(unit='deg')}")  # prints in hours

    # Calculate the altitude and azimuth of the sun
    altaz = AltAz(location=san_diego, obstime=time_utc)
    sun_altaz = get_sun(time_utc).transform_to(altaz)

    # Calculate the solar angle
    solar_angle = 90 - sun_altaz.alt.to_value()

    # Print the solar angle
    print(f"Solar Angle in San Diego: {solar_angle:.2f} degrees")

trackSun()
