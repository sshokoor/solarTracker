from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
from datetime import datetime, timezone


def getSunPosition(latitude: float, longitude: float, elevation: float, observedTime: str):
    """Returns the azimuth and altitude"""

    # Define EarthLocation object
    sd_location = EarthLocation(
        lat=str(latitude) + ' deg', lon=str(longitude) + ' deg', height=elevation)

    # currentLocalTime = "2023-04-06 13:53:44.284268"
    currentUtcTime = datetime.fromisoformat(
        observedTime).astimezone(timezone.utc)

    # Get the current time
    now = Time(currentUtcTime)

    # Get the position of the Sun at the current time
    sun = get_sun(now)

    # Convert the Sun's position to altitude and azimuth coordinates
    alt_az = sun.transform_to(AltAz(obstime=now, location=sd_location))
    return (round(alt_az.az.to_value()), round(alt_az.alt.to_value()))


def calculatePulsesOnSunPosition(current: datetime):

    # get the current position of the sun relative to me
    date_iso = current.isoformat()
    az, alt = getSunPosition(32.715736, -117.161087, 0, date_iso)

    # map values to pulse
    azPulse = round(mapValue(az, 0, 270, 500, 2500), 0)
    altPulse = round(mapValue(alt, 0, 90, 500, 2500), 0)
    return (azPulse, altPulse)


def mapValue(num, in_min, in_max, out_min, out_max):
    """Helper method to map an input value (v_in)
       between alternative max/min ranges."""
    num = (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if num < out_min:
        num = out_min
    elif num > out_max:
        num = out_max
    return num
