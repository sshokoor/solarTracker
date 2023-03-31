import pytest
from astropy.coordinates import Angle

# Import the trackSun function from your code file
from ..tester import trackSun

# Define San Diego coordinates
latitude = 32.7157
longitude = -117.1611
elevation = 18  # meters above sea level

# Define test cases
test_cases = [
    # Test case 1: Sunrise
    {"observedTime": "2023-03-30 06:30:00", "expectedHourAngle": Angle(0, unit='hourangle'), "expectedZenithAngle": Angle(90, unit='degree')},
    
    # Test case 2: Solar Noon
    {"observedTime": "2023-03-30 12:00:00", "expectedHourAngle": Angle(0, unit='hourangle'), "expectedZenithAngle": Angle(37.246, unit='degree')},
    
    # Test case 3: Sunset
    {"observedTime": "2023-03-30 18:00:00", "expectedHourAngle": Angle(0, unit='hourangle'), "expectedZenithAngle": Angle(90, unit='degree')}
]

# Define the pytest function
@pytest.mark.parametrize("test_case", test_cases)
def test_trackSun(test_case):
    # Extract the input values from the test case dictionary
    observed_time = test_case["observedTime"]
    expected_ha = test_case["expectedHourAngle"]
    expected_za = test_case["expectedZenithAngle"]
    
    # Call the trackSun function with the observed time
    ha, za = trackSun(latitude, longitude, elevation, observed_time)
    
    # Compare the output values to the expected values
    assert ha == pytest.approx(expected_ha, abs=1e-2)
    assert za == pytest.approx(expected_za, abs=1e-2)
