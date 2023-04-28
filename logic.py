import PCA9685
import time
import hourAngle
import datetime


def setServoPulse(channel0Pulse: int, channel1Pulse: int) -> None:
    """Set servos to pulse range"""

    pwm = PCA9685(0x40, debug=False)
    pwm.setPWMFreq(50)
    pwm.setServoPulse(0, channel0Pulse)
    pwm.setServoPulse(1, channel1Pulse)
    time.sleep(2)

    # Kill the servos
    pwm.setPWM(0, 0, 0)
    pwm.setPWM(1, 0, 0)


def init() -> None:
    azPulse, altPulse = hourAngle.calculatePulsesOnSunPosition(datetime.datetime.now())
    setServoPulse(azPulse, altPulse)


if __name__ == '__main__':
    init()
