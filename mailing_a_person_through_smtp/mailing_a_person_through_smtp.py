#!/usr/bin/env python

'''
program for send a mail using smtp library
sender gmail id password is required
Allow less Secure apps: on (gmail sign-in & security settings)
you can take sender mailid, password, receiver mailid, subject.
In your google account setting you have enable the handling from
the low level apps.
'''
import smtplib                          #it will open the link you desired
from email.mime.text import MIMEText    #it will send the subject user to in a particular text format

def sendMail(user,pwd,to,subject,text):                                         #it will connect to socket and send the message securely
	msg=MIMEText(text)                                                      #in a particular text format
	msg['From']=user
	msg['To']=to
	msg['Subject']=subject
	#msg = "\n".join(["From: "+user,"To: "+to,"Subject: "+subject,"",text]) #this line can also be used instead of upper 4 lines
	try:
		smtpServer=smtplib.SMTP('smtp.gmail.com',587)
		print "[+] Connecting to Mail Server"
		smtpServer.ehlo()
		print "[+] Starting encrypted session."
		smtpServer.starttls()
		print "[+] Logging into Mail Server."
		smtpServer.login(user,pwd)
		print"[+] Sending Mail."
		smtpServer.sendmail(user,to,msg.as_string())
		smtpServer.close()
		print "[+] Mail Sent Sucessfully"
	except:
		print "[-] Sending Mail Failed."
user='xyz@gmail.com'                                        #user email id
pwd='password'                                              #user password

receiver_id = 'zyx@gmail.com'                               #receiver's email id
subject = 'this is a testing mail'                          #subject of mail
text_msg = 'this mail is sent u by a simple python script'  #your message
sendMail(user,pwd,receiver_id,subject,text_msg)             #calling function
