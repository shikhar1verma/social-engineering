#!/usr/bin/env python
'''
Program to pull and posts data from and to the  facebook respectively
How to use the graph api of facebook.
'''

import facebook         #facebook sdk for python
import json             #to tweak the json format
import urllib
import urllib2
import requests

page_id=raw_input('enter facebook page id: ')       #url of facebook
token=raw_input('enter fb token: ')                 #token or key given by facebook

def testFacebookPageFeedData(page_id,token):        #getting the profile information and posting the status
    graph = facebook.GraphAPI(token)                #validating the token
    profile = graph.get_object("me")                #once token information is valid we can get entities from facebook
    print profile
    posts = graph.get_connections(profile['id'], 'posts', limit = 1)    #posting the staus in json format
    print posts
    post_dict=json.dumps(posts)
    data = json.loads(post_dict)
    print data['data'][0]['message']

if __name__ == "__main__":
    testFacebookPageFeedData(page_id,token)         #function that calls feed
