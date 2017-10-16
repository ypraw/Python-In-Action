#  tesml.py on  Python-In-Action Project
__author__ = " ypraw "
__date__ = "Jul 25, 2017  23:49 "

import RPi.GPIO as GPIO
import time
import os

'''
in this case, i added function to send email,
the purpose if there is movement then raspi will send the
pictures and give notification to the Owner.
and you can develop it, to your own goals


'''
# importing modul sendEmail, you can see in
# https://github.com/ypraw/Python-In-Action/tree/master/Python%20Email
import tesml

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  # input Pir Detector
GPIO.setup(3, GPIO.OUT)  # Output Alarm

try:
    pic = 0
    while True:
        i = GPIO.input(11)
        if i == 0:
            print "No Activity"
            GPIO.output(3, 0)
            time.sleep(10)
        elif i == 1:

            print "movement Detected"

            # Camera Action Here
            os.system("fswebcam -p yuyv -d /dev/video0 -r 640*480/home/pi/Pictures/%d.jpeg" % pic)

            # Sending email here
            SendMail('name of image', 'your email address', 'sending to',
                     'your password', 'subject of message', 'content of message')

            pic += 1
            GPIO.output(3, 1)
            time.sleep(10)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
