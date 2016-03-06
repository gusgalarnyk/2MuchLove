import SendEmail
import datetime
import time

me = ""
key = ""
who = input("Whose birthday is coming up tomorrow?")
you = input("And what is their email?")
freq = input("How many emails should they get an hour? (0.0417-60)")
print("Ha. Wonderful, this should be good.")
waitsec = (3600/float(freq))
today = datetime.date.today()

Bday = True
while Bday == True:
    msg = "Hey there " + who + ", \r\n It's your birthday and I am so happy to tell you that I have signed you up" \
                               "to my personal love bot. Well I mean to say I made a bot in Python to show you just" \
                               "how much I love you. \r\n Expect to get a few emails from me today.  "
    sub = "Happy Birthday my friend with a good sense of humor."
    SendEmail.SendIt(me, key, you, sub, msg)
    time.sleep(waitsec)
    if today != datetime.date.today():
        Bday = False
    else:
        continue

print("Looks like they got the message. You love them too much. Nice job, let's see how fast your friends learn"
      "to filter your emails.")