from gpiozero import Servo

def rotate_azimuth(angle):
    servo = Servo(25)
    return 0