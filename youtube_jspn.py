# Connect to Youtube website retrieves info on the most highly rated videos 
#1. Import Json
import json
#import only the urlopen functions from the standard urllib library 
from urllib.request import urlopen
#assign a youtube url to the variable url
url="https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json" 
#connect to the web server at the URL and request a particulate web service 
response = urlopen(url)
#Get the response data and assign to the cariable contents 
contents = response.read()
#decode contents tp a text string in JSON format, and assign to the variable text
text = contents.decode('utf8')
#convert text to data- phthon data structures about videos
data = json.loads(text)
#uses a two level python dictionary (data['fee']['entry']) and a slice ([0:6])
for video in data['feed']['entry'][0:6]:
	print(video['title'['$t']