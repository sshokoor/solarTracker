from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
from datetime import datetime, timezone

def getSunPosition(latitude, longitude, elevation, observedTime):
    # Define EarthLocation object
    # location = EarthLocation(lat=latitude, lon=longitude, height=elevation)
    sd_location = EarthLocation(lat=str(latitude) + ' deg', lon=str(longitude) + ' deg', height=elevation)

    #currentLocalTime = "2023-04-06 13:53:44.284268"
    currentUtcTime = datetime.fromisoformat(observedTime).astimezone(timezone.utc)

    # Get the current time
    now = Time(currentUtcTime)

    # Get the position of the Sun at the current time
    sun = get_sun(now)

    # Convert the Sun's position to altitude and azimuth coordinates
    alt_az = sun.transform_to(AltAz(obstime=now, location=sd_location))

    return(round(alt_az.az.to_value()), round(alt_az.alt.to_value()))
    
    #return (ha, solar_angle)

#getSunPosition(32.715736, -117.161087, 0, "2023-04-06 13:53:44.284268")
#print(getSunPosition(32, -117, 0, "2023-04-06 13:41:00")) 

"""
# Define San Diego coordinates
latitude = 32.7157
longitude = -117.1611
elevation = 0  # meters above sea level

# Define test cases
test_cases = [
    # Test case 1: Sunrise
    {"observedTime": "2023-03-31T13:30:00", "expectedHourAngle": Angle(-95.83, unit='degree'), "expectedZenithAngle": Angle(91, unit='degree')},
    
    # Test case 2: Solar Noon
    {"observedTime": "2023-03-31T19:00:00", "expectedHourAngle": Angle(0, unit='degree'), "expectedZenithAngle": Angle(184, unit='degree')},
    
    # Test case 3: Sunset
    {"observedTime": "2023-03-31T25:30:00", "expectedHourAngle": Angle(84.17, unit='degree'), "expectedZenithAngle": Angle(274, unit='degree')}
]

# Define the pytest function
@pytest.mark.parametrize("test_case", test_cases)
def test_getSunPosition(test_case):
    # Extract the input values from the test case dictionary
    observed_time = test_case["observedTime"]
    expected_ha = test_case["expectedHourAngle"]
    expected_za = test_case["expectedZenithAngle"]

    location = EarthLocation(lat=latitude, lon=longitude, height=elevation)

    expected_alt = 50.740
    expected_azimuth = 231.376
    
    # Call the getSunPosition function with the observed time
    ha, za = getSunPosition(latitude, longitude, elevation, observed_time)
    
    # Compare the output values to the expected values
    assert ha.to_value() == pytest.approx(expected_ha.to_value(), abs=1e-2)
    assert za == pytest.approx(expected_za.to_value(), abs=1e-2)

    assert abs(sun_altaz.alt.value - expected_alt) < 1e-4
    assert abs(sun_altaz.az.value - expected_azimuth) < 1e-4

    
   """ 

   