from solarTracker.hourAngle import getSunPosition

def test_azimuth():
    az, alt = getSunPosition(32.715736, -117.161087, 0, "2023-04-06 14:51:00")
    assert az == 233
    assert alt == 52
    #assert getSunPosition(32, -117, 0, "2023-03-31 14:51:00").ha == 50.59

def test_sunrise():
    az, alt = getSunPosition(32.715736, -117.161087, 0, "2023-04-06 06:40:00")
    assert az == 83 #83.05
    assert alt == 1 #1.53

def test_solarNoon():
    az, alt = getSunPosition(32.715736, -117.161087, 0, "2023-04-06 12:00:00")
    assert az == 153 #152.83
    assert alt == 61 #61.3

def test_sunset():
    az, alt = getSunPosition(32.715736, -117.161087, 0, "2023-04-06 19:12:00")
    assert az == 278 #278.46
    assert alt == -1 #-.37



