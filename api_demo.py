#!/usr/bin/env python3.6
import urllib.request
import json
import decimal
import locale

locale.setlocale(locale.LC_ALL, 'en_IN')


def ViewsFormat(num):
	if num >= 1000 and num < 1000000:
        	div=int(num/1000)
        	#div=round(div,0)
        	print(str(div)+"K Views")
	elif num >= 1000000 and num < 1000000000:
        	div=num/float(1000000)
        	div=round(div,1)
        	print(str(div)+"M Views")
	elif num >=1000000000:
        	div=num/float(1000000000)
        	div=round(div,1)
        	print(str(div)+"B Views")
	else:
        	pass


#url = "https://gdata.youtube.com/feeds/api/videos?q=Python&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU&orderby=viewCount&max-results=50&v=2&alt=json"

#url = "https://www.googleapis.com/youtube/v3/activities?part=snippet&channelId=UC_x5XG1OV2P6uZZ5FSM9Ttw&key=AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU&maxResults=25"

##	chid = input("Enter the channel id ")
API_KEY = 'AIzaSyDkMyxlITYIZ7C_eGjfpF5RoeJsOoJsOFU'

##	url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails&id="+chid+"&key="+API_KEY+""

def pstar():
	for i in range(100):
		print("*", end='')
	print("")
'''
feed = urllib.request.urlopen(url)
feed = feed.read()
feed_json = json.loads(feed)
 

print("Channel Name: ",feed_json['items'][0]['snippet']['title'])
print("Description: ",feed_json['items'][0]['snippet']['description'])

'''


# FOR INDIA 

url1 = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=IN&maxResults=10&key="+API_KEY+""
trends = urllib.request.urlopen(url1)
trends = trends.read()
trends_json = json.loads(trends)

print("")
pstar()
print("YOUTUBE TRENDING VIDEOS IN INDIA")
pstar()
for i in range(10):
	print("")
	print(trends_json['items'][i]['snippet']['title'])
	Views=int(trends_json['items'][i]['statistics']['viewCount'])
	ViewsFormat(Views)
	#Views=locale.format("%d", Views , grouping=True)
	#print(Views+" Views")


'''

# FOR UK

ukurl="https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=GB&maxResults=10&key="+API_KEY+""
trendsUK = urllib.request.urlopen(ukurl)
trendsUK = trendsUK.read()
trends_json = json.loads(trendsUK)
print("")
pstar()
print("YOUTUBE TRENDING VIDEOS IN UK")
pstar()
for i in range(10):
        print("")
        print(trends_json['items'][i]['snippet']['title'])
        print(trends_json['items'][i]['statistics']['viewCount']+" Views" )


# FOR USA

usaurl="https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=US&maxResults=10&key="+API_KEY+""
trendsUSA = urllib.request.urlopen(usaurl)
trendsUSA = trendsUSA.read()
trends_USA_json = json.loads(trendsUSA)
print("")
pstar()
print("YOUTUBE TRENDING VIDEOS IN USA")
pstar()
for i in range(10):
	print("")
	print(trends_USA_json['items'][i]['snippet']['title'])
	print(trends_USA_json['items'][i]['statistics']['viewCount']+" Views" )


'''
