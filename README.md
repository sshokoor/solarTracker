
# Solar Tracker

Program to control a servo to get the maximum sun exposure


## Authors


- [@sshokoor](https://www.github.com/sshokoor)
- [@skittleson](https://www.github.com/skittleson)


## Installation

To use this solar tracker you will need Python 3.7 or later. You will also need to install the astropy library with pip, as well as pytest to run the test code. 

```bash
  pip install astropy
  pip install -U pytest
```
    
## Usage
- To use Solar Tracker you will need two devices:
    - Raspberry PI and a Servo. 
- You will need to ssh into your Raspberry PI in order to control the servo
```bash
ssh <IP address>
```
- Then you will need to clone the repository onto your device 
```bash
git clone https://github.com/sshokoor/solarTracker.git
```

![Image](https://github.com/sshokoor/solarTracker/blob/main/servo.jpg)
## Resources
1. [Astropy](https://docs.astropy.org/en/stable/time/index.html) : astropy documentation for using date and time 
2. [Solar Calculator](https://gml.noaa.gov/grad/solcalc/azel.html) : solar calculator we used for reference to test our azimuth and altitude calculations
3. [Servo Documentation](https://www.waveshare.com/wiki/Servo_Driver_HAT) : documentation for the Servo Driver HAT

## Contact
If you have any questions or comments about solarTracker, please open an issue on this repository or contact me by [my email](sarahshokoor@gmail.com).
