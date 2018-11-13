#!/usr/bin/env python
import urllib
import json
 
#url = "https://gdata.youtube.com/feeds/api/videos?q=Python&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU&orderby=viewCount&max-results=50&v=2&alt=json"

#url = "https://www.googleapis.com/youtube/v3/activities?part=snippet&channelId=UC_x5XG1OV2P6uZZ5FSM9Ttw&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU&maxResults=25"

'''
chid = raw_input("Enter the channel id ")
url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails&id="+chid+"&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU"
feed = urllib.urlopen(url)
feed = feed.read()
feed_json = json.loads(feed)
 
#print(feed_json)
#  print(feed_json['kind'])
#print(feed_json['items'])
print(feed_json['items'][0]['snippet']['title'])
print(feed_json['items'][0]['snippet']['description'])
'''


def Viewformat(num):
	if num >= 1000 and num < 1000000:
		div= num / 1000
		print(str(div)+"K Views")
	elif num >= 1000000 and num < 1000000000:
		div = num / float(1000000)
		div = round(div,1)
		print(str(div)+"M Views")
	elif num >= 1000000000:
		div = num / float(1000000000)
                div = round(div,1)
                print(str(div)+"B Views")
	else:
		pass


countrycode={
                'India': 'IN',
                'Great Britain UK':'GB',
                'America': 'US',
                'China': 'CN',
                'France':'FR',
                'Germany':'DE',
                'Pakistan':'PK'
             }
for key in countrycode.keys():
	print(key)
code=raw_input("Select the country from above ")
regioncode=countrycode.get(code,"Invalid Country")

API_KEY='AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU'

url1 = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode="+regioncode+"&maxResults=20&key="+API_KEY+""

trends = urllib.urlopen(url1)
trends = trends.read()
trends_json = json.loads(trends)


print("")
print("")
print("***************************************************************************************")
print("Youtube Trending videos in "+code+"")
print("***************************************************************************************")

for i in range(5):
	print("")
	print(trends_json['items'][i]['snippet']['title'])
	views= int(trends_json['items'][i]['statistics']['viewCount'])
	Viewformat(views)
	print("https://www.youtube.com/watch?v="+trends_json['items'][i]['id'])

