#!/usr/bin/env python
'''
through this script we can browse a site
and get the source code of the site.
Through mechanize library we can automatically
fill form and many more things.
'''
import mechanize

def view_page(url):                             #to browse  a site and get the source code of the site
	try:
		browser=mechanize.Browser()
		page=browser.open(url)
		soure_code = page.read()
		print source_code
	except:
		print "Error in browsing....."

url = raw_input('Enter the URl: ')      #take user input of URL of site
view_page(url)                          #caling the function
