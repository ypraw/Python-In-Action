#  tesml.py on  Python-In-Action Project
__author__ = " ypraw "
__date__ = "Jul 24, 2017  0:49 "

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# with open(textfile) as fp:
# Create a text/plain message
#    msg =  MIMEText(fp.read())
msg = "hello"
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % msg
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
