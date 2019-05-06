import time
import datetime
import grovepi
from picamera import PiCamera


def start():
    # Connection sensors to digital port
    pir_sensor = 8
    loudness_sensor = 0
    led = 3

    date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.rotation = 180


    grovepi.pinMode(pir_sensor,"INPUT")

    while True:
        try:
            # Sense motion, usually human, within the target range
            if grovepi.digitalRead(pir_sensor) and grovepi.analogRead(loudness_sensor) > 30:
                grovepi.digitalWrite(led, 1)  # Send HIGH to switch on LED
                print ("LED ON!")
                # Video capture
                camera.start_recording("/home/pi/" + date + ".h264")
                camera.wait_recording(10)
                camera.stop_recording()
                time.sleep(1)
                grovepi.digitalWrite(led, 0)  # Send LOW to switch off LED

                # Image capture
                # camera.capture('/home/pi/Desktop/live2.jpg')
                # print("Image Shot")

            else:
                print '-'

            # if your hold time is less than this, you might not see as many detections
            time.sleep(1)

        except IOError as error:
            print("Error in Surveillance " + error)
