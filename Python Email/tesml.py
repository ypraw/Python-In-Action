#  tesml.py on  Python-In-Action Project

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName, sendfrom, sendTo, passUser, subMsg, MsgContent):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = subMsg
    msg['From'] = sendfrom
    msg['To'] = sendTo

    text = MIMEText(MsgContent)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sendfrom, passUser)
    s.sendmail(sendfrom, sendTo, msg.as_string())
    s.quit()


if __name__ == '__main__':
    # NOTE
    """
    SendMail('name of image','your email address','sending to',
             'your password','subject of message','content of message'
    before you send of message, please activate less secure apps in your gmail,
    following this url https://myaccount.google.com/lesssecureapps
    """
