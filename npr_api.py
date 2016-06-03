# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import load, dumps
from urllib import quote

import os
key = os.getenv('NPR_KEY') # Import API key from local bash

# Stories API XML and RSS podcast
url = 'http://api.npr.org/query?apiKey='
url += key
url += "&numResults=3&action=Or&requiredAssets=text&format=rss"

npr_id = raw_input("Enter comma-separated NPR IDs or leave blank.")

search_string = raw_input("Enter your search string or leave blank.")

feed_title = raw_input("What's your feed title?")

if npr_id or search_string:

    raw_input("Hit Enter to download your podcast.")

    if npr_id:
        url = url + "&id=" + npr_id

    if search_string:
        url = url + "&searchTerm=" + quote(search_string)

    if feed_title:
        url = url + "&title=" + feed_title

    response = urlopen(url)
    output = response.read()

    my_feed = open("my_feed.xml", "w") # Returns XML feed
    my_feed.write(output)
    my_feed.close()

else:
    print "You must enter an NPR ID, a search term, or both."


#############
# Transcript API
# JSON accessed to print paragraphs for story id 152248901
url = "http://api.npr.org/transcript"
url = url + "?apiKey=" + key + "&format=json" + "&id=152248901"
print url

response = urlopen(url)
j = load(response)
print j

for paragraph in j["paragraph"]:
    print paragraph["$text"] + "\n"

f = open("output.json", "w")
f.write(dumps(j, indent=4))
f.close()

################
# Local Stations API
## API out of date now..must find new way to do it
#
# def build_api_call(key):
#     zip_code = raw_input("Enter your zip code:")
#     url = "http://api.npr.org/stations" + "?apiKey=" + key + "&format=json" + "&zip=" + zip_code
#     return url
#
# def call_station_api(url):
#     response = urlopen(url)
#     j = load(response)
#     return j
#
# def parse_station_json(json_obj):
#     for station in json_obj['station']:
#         print station['callLetters']["$text"] + ": " + station["marketCity"]["$text"] + ", " + station["state"]["$text"]
#         print "Frequency: " + station["frequency"]["$text"] + station["band"]["$text"]
#
#         if 'url' in station:
#             print "MP3 Streams: "
#             for link in station['url']:
#                 if link['type'] == "Audio MP3 Stream":
#                     print "\t" + link['title'] + " - " + link["$text"]
#
# url = build_api_call(key)
# print "URL: " + url
#
# json_obj = call_station_api(url)
# print json_obj
#
# parse_station_json(json_obj)
