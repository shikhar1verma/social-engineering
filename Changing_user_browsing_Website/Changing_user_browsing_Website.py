#!/usr/bin/env python
'''
through this script we can change the user agent
,we can change the platform through wich the packet
is coming from.
'''
import mechanize

def change_user_agent(url, user_agent):             #changing he user agent
	try:
		browser=mechanize.Browser()
		browser.set_handle_robots(False)    #we are not asking the robot.txt file
		browser.addheaders = user_agent	    #we are addin g the user agent in the header
		page=browser.open(url)
		source_code = page.read()
		print source_code                   #printing the source code
	except:
		print "Error in browsing....."

url = raw_input('Enter the URL: ')              #getting the URL from the user input
user_agent=[('User-agent','Mozilla/5.0 (X11;U;Linux 2.4.2.-2 i586; en-us;m18) Gecko/200010131 Netscape6/6.01')]     #giving the user agent mozilla
change_user_agent(url,user_agent)               #calling the function
