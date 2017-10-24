from gpiozero import DigitalInputDevice
import datetime
from picamera import PiCamera
from signal import pause

radar = DigitalInputDevice(17, pull_up=False, bounce_time=2.0)
camera = PiCamera()
camera.resolution = (1024, 768)

def detector():
    timestamp = str((datetime.datetime.now()))
    timestamp = timestamp[0:19]
    print("Image captured at",timestamp)
    camera.capture(timestamp+".jpg")
    
radar.when_activated = detector
pause()
    
