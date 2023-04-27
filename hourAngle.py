from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
from datetime import datetime, timezone

def getSunPosition(latitude, longitude, elevation, observedTime):
    """Returns the """
    # Define EarthLocation object
    sd_location = EarthLocation(lat=str(latitude) + ' deg', lon=str(longitude) + ' deg', height=elevation)

    observedTime = str(datetime.now())

    #currentLocalTime = "2023-04-06 13:53:44.284268"
    currentUtcTime = datetime.fromisoformat(observedTime).astimezone(timezone.utc)

    # Get the current time
    now = Time(currentUtcTime)

    # Get the position of the Sun at the current time
    sun = get_sun(now)

    # Convert the Sun's position to altitude and azimuth coordinates
    alt_az = sun.transform_to(AltAz(obstime=now, location=sd_location))

    print(round(alt_az.az.to_value()), round(alt_az.alt.to_value()))
    
if __name__ == '__main__':
    getSunPosition(32.715736, -117.161087, 0, "2023-03-31 14:49:44.284268")
#getSunPosition(32.715736, -117.161087, 0, "2023-04-06 13:53:44.284268")