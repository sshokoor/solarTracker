import pytest
from astropy.coordinates import Angle

# Import the trackSun function from your code file
from ..tester import sunExposure

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