import smtplib
import os
s = smtplib.SMTP('smtp.gmail.com',587)
def sendmail(TEXT,email,SUBJECT):
    #print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login("golimeghana27@gmail.com", "Meghana@275")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("golimeghana27@gmail.com", email, message)
    s.quit()


