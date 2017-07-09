#!/usr/bin/env python
'''
in this script we webscraped the table from a wiki page
and stored in a dataframe of pandas then update that dtaframe as
table in mysql databse server
'''

import urllib2                      #helps in openning urls
from bs4 import BeautifulSoup       #helps in webscraping

wiki = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)
print 'string',soup.title.string    #here we print the title of the page
tables = soup.find('table',{"class" : 'wikitable sortable plainrowheaders'})    #here we found the table we want to scrape from wikipedia


A=[]            #empty list for different collumns
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in tables.findAll("tr"):                 #here we finding the data tag of row of the table
	cells = row.findAll('td')
        states=row.findAll('th')                 #To store second column data
        if len(cells)==6:
                                                 #Only extract table body not heading
		a=cells[0].find(text=True)
		A.append(a.encode(encoding='UTF-8'))        #we have to change the encoding to readable form
		b=states[0].find(text=True)
		B.append(b.encode(encoding='UTF-8'))
		c=cells[1].find(text=True)
		C.append(c.encode(encoding='UTF-8'))
		d=cells[2].find(text=True)
		D.append(d.encode(encoding='UTF-8'))
		e=cells[3].find(text=True)
		E.append(e.encode(encoding='UTF-8'))
		f=cells[4].find(text=True)
		F.append(f.encode(encoding='UTF-8'))
		g=cells[5].find(text=True)
		try:
                        G.append(g.encode(encoding='UTF-8'))
                except AttributeError:
                        G.append(None)


import pandas as pd                     #here we importing pandas library
from pandas.io import sql               #here we import pandas.io to directly convert the pandas dataframe to table of mysql database
df=pd.DataFrame(A,columns=['Number'])   #putting data to the collumns
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print df

#import MySQLdb as mdb                                              '''this is an old engine which pandas do not support now'''
#con = mdb.connect('127.0.0.1', 'testuser', 'test123', 'testdb');

from sqlalchemy import create_engine            #it provide the engine so we can send the dataframe to our mysql database

#df.to_sql(con='testdb', name='capitals',if_exists='replace',flavor='mysql',chunksize=1000)
pwd='password'                                                                  #here comes the password
engine = create_engine('mysql://root:'+pwd+'@127.0.0.1/testdb?charset=utf8')    #here comes the user then password then IP on which mysql server is configured and then the name of databse
df.to_sql('capitals',engine,if_exists='replace')                                #here the name of table then engine them the condition of existing the table
