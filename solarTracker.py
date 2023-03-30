import astropy.coordinates as coord
from astropy.time import Time
import astropy.units as u


from astropy.coordinates import get_sun, AltAz, EarthLocation
from astropy.time import Time

## sun_time = Time('2023-12-6 17:00') #UTC time
now = Time.now()
loc = EarthLocation.of_address('San Diego, CA')  # anything the google geocoding API resolves
altaz = AltAz(obstime=now, location=loc)

print(now)

zen_ang = get_sun(now).transform_to(altaz)
print(zen_ang.zen.degree)