import astropy.units as u
from astropy.coordinates import SkyCoord, ITRS, EarthLocation
from astropy.time import Time

c = SkyCoord(-117, 32, unit='deg', frame='icrs')
t = Time.now()
loc = EarthLocation.of_address('San Diego, CA')

c_ITRS = c.transform_to(ITRS(obstime=t))
# Calculate local apparent Hour Angle (HA), wrap at 0/24h
local_ha = loc.lon - c_ITRS.spherical.lon
local_ha.wrap_at(24*u.hourangle, inplace=True)
# Calculate local apparent Declination
local_dec = c_ITRS.spherical.lat
print("Local apparent HA, Dec={} {}".format(local_ha.to_string(unit=u.hourangle, sep=':'), local_dec.to_string(unit=u.deg, sep=':', alwayssign=True) ))