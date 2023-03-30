from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
import astropy.units as u

def calculate_angles(observer_lat, observer_lon, observer_elev, target_ra, target_dec, obs_time_str):
    # Define the observer's location (latitude, longitude, elevation)
    observer_loc = EarthLocation(lat=observer_lat*u.deg, lon=observer_lon*u.deg, height=observer_elev*u.m)

    # Define the time of observation
    obs_time = Time(obs_time_str, format='isot', scale='utc')

    # Define the target's coordinates (right ascension, declination)
    target_coord = SkyCoord(ra=target_ra*u.deg, dec=target_dec*u.deg)

    # Calculate the Altitude/Azimuth coordinates of the target at the given time and location
    altaz_coord = target_coord.transform_to(AltAz(location=observer_loc, obstime=obs_time))

    # Calculate the hour angle (in hours)
    hour_angle = obs_time.sidereal_time('apparent', longitude=observer_loc.lon) - target_coord.ra
    hour_angle = hour_angle.wrap_at(180*u.deg).hourangle

    # Calculate the zenith angle (in degrees)
    zenith_angle = 90*u.deg - altaz_coord.alt

    return hour_angle, zenith_angle

def test_calculate_angles():
    # Define the test case: observer in San Diego, target at RA=10 deg, Dec=20 deg, and observation time at noon UTC on 2023-03-29
    observer_lat = 32.7157
    observer_lon = -117.1611
    observer_elev = 18.0
    target_ra = 10.0
    target_dec = 20.0
    obs_time_str = '2023-03-29T12:00:00'

    # Calculate the expected hour angle and zenith angle
    expected_hour_angle = -1.383 # hours
    expected_zenith_angle = 59.840 # degrees

    # Calculate the hour angle and zenith angle using the function
    hour_angle, zenith_angle = calculate_angles(observer_lat, observer_lon, observer_elev, target_ra, target_dec, obs_time_str)
    # Check that the calculated values match the expected values within a tolerance of 0.001 hours for the hour angle and 0.001 degrees for the zenith angle
    assert abs(hour_angle - expected_hour_angle) < 0.001
    assert abs(zenith_angle - expected_zenith_angle) < 0.001