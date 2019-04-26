import time
import grovepi
from picamera import PiCamera

def start():
    # Connect the Grove PIR Motion Sensor to digital port D8
    # SIG,NC,VCC,GND
    pir_sensor = 8
    loudness_sensor = 0
    led = 3
    camera = PiCamera()
    camera.resolution = (1024, 768)

    grovepi.pinMode(pir_sensor,"INPUT")

    while True:
        try:
            # Sense motion, usually human, within the target range
            if grovepi.digitalRead(pir_sensor) and grovepi.analogRead(loudness_sensor) > 30:
                grovepi.digitalWrite(led, 1)  # Send HIGH to switch on LED
                print ("LED ON!")
                camera.capture('/home/pi/Desktop/live2.jpg')
                print("Image Shot")
                time.sleep(0.5)
                grovepi.digitalWrite(led, 0)  # Send LOW to switch off LED

            else:
                print '-'

            # if your hold time is less than this, you might not see as many detections
            time.sleep(0.5)

        except IOError as error:
            print("Error in Surveillance " + error)
