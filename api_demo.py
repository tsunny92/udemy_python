#!/usr/bin/env python
import urllib
import json
 
#url = "https://gdata.youtube.com/feeds/api/videos?q=Python&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU&orderby=viewCount&max-results=50&v=2&alt=json"

#url = "https://www.googleapis.com/youtube/v3/activities?part=snippet&channelId=UC_x5XG1OV2P6uZZ5FSM9Ttw&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU&maxResults=25"

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

#for feed in feed_json['feed']['entry']:
#	Video_title = feed['title']['$t']
#    	print Video_title

url1 = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=IN&maxResults=10&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU"

trends = urllib.urlopen(url1)
trends = trends.read()
trends_json = json.loads(trends)


print("")
print("")
print("***************************************************************************************")
print("YOUTUBE TRENDING VIDEOS IN INDIA")
print("***************************************************************************************")

for i in range(10):
	print("")
	print(trends_json['items'][i]['snippet']['title'])
        print(trends_json['items'][i]['statistics']['viewCount']+" Views" )

#print(trends_json['items'][0]['snippet']['title'])
#print(trends_json['items'][1]['snippet']['title'])


ukurl="https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=GB&maxResults=10&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU"

trendsUK = urllib.urlopen(ukurl)
trendsUK = trendsUK.read()
trends_json = json.loads(trendsUK)


print("")
print("")
print("***************************************************************************************")
print("YOUTUBE TRENDING VIDEOS IN UK")
print("***************************************************************************************")

for i in range(10):
        print("")
        print(trends_json['items'][i]['snippet']['title'])
        print(trends_json['items'][i]['statistics']['viewCount']+" Views" )





#usaurl="https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails&chart=mostPopular&regionCode=US&maxResults=10&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU"

usaurl="https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=US&maxResults=10&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU"

trendsUSA = urllib.urlopen(usaurl)
trendsUSA = trendsUSA.read()
trends_USA_json = json.loads(trendsUSA)


print("")
print("")
print("***************************************************************************************")
print("YOUTUBE TRENDING VIDEOS IN USA")
print("***************************************************************************************")

for i in range(10):
        print("")
        print(trends_USA_json['items'][i]['snippet']['title'])
	print(trends_USA_json['items'][i]['statistics']['viewCount']+" Views" )


