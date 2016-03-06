#http://naelshiab.com/tutorial-send-email-python/

import smtplib


def SendIt(user, key, target, sub, msg):

    emailUsername = user
    emailPassword = key
    emailRecipient = target
    emailSubject = sub
    Message = msg

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(emailUsername, emailPassword)

    msg = "\r\n".join([
        "From: " + emailUsername,
        "To: " + emailRecipient,
     "Subject: " + emailSubject,
     "",
     Message
    ])

    server.sendmail(emailUsername, emailRecipient, msg)
    server.close()
    print("Email sent!")