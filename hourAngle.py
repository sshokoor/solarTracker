from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, SkyCoord, Angle, get_sun
from astropy import units as u
import pytest

def sunExposure(latitude, longitude, elevation, targetRA, targetDec, observedTimeStr):
    # Define EarthLocation object   
    sanDiego = EarthLocation(lat=latitude*u.deg, lon=longitude*u.deg, height=elevation*u.m)

    observedTime = Time(observedTimeStr, format='isot', scale='utc')

    targetCoord = SkyCoord(ra=targetRA*u.deg, dec=targetDec*u.deg)

    altazCoord = targetCoord.transform_to(AltAz(location=sanDiego, obstime=observedTime))

    hourAngle = observedTime.sidereal_time('apparent', longitude=sanDiego.lon) - targetCoord.ra
    hourAngle = hourAngle.wrap_at(180*u.deg).degree

    zenithAngle = 90*u.deg - altazCoord.alt

    return hourAngle, zenithAngle

def test_hourAngle():
    latitude = 32.7157
    longitude = -117.1611
    elevation = 19 

    targetRA = 83.8221
    targetDec = -5.3911

    observedTimeStr = [
        '2023-03-29T20:00:00',
        '2023-03-29T22:00:00',
        '2023-03-30T00:00:00',
    ]

    expectedHourAngles = [
        41.7466,
        295.5221,
        189.0636,
    ]
    expectedZenithAngles = [
        44.2624*u.deg,
        63.7985*u.deg,
        77.9148*u.deg,
    ]

    for observedTimeStr, expectedHourAngle, expectedZenithAngle in zip(observedTimeStr, expectedHourAngles, expectedZenithAngles):
        actualHourAngle, actualZenithAngle = sunExposure(latitude, longitude, elevation, targetRA, targetDec, observedTimeStr)

        assert actualHourAngle == pytest.approx(expectedHourAngle, abs=1e-4)
        assert actualZenithAngle == pytest.approx(expectedZenithAngle, abs=1e-4*u.deg)