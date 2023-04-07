from solarPanelController import rotate

def test_can_given_azimuth_at_sunrise():
    actual = rotate(1,0)
    assert actual

def test_can_given_azimuth_at_midnight():
    actual = rotate(1,300)
    assert actual == 270