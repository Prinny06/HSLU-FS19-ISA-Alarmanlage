from picamera import PiCamera
#from subprocess import call
import datetime
import time


date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

camera = PiCamera()

camera.resolution = (640, 480)
camera.rotation = 180
camera.start_recording("/home/pi/" + date + ".h264")
# Videolaenge in Sekunden
camera.wait_recording(10)
camera.stop_recording()


