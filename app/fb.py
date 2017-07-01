import os
import json
import urllib
import pprint


def list_id_from_file():
	with open('id.txt') as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content] 
	for x in content:
		print x




# get Facebook access token from environment variable
#ACCESS_TOKEN = os.environ['ACCESS_TOKEN']


ACCESS_TOKEN = "EAACEdEose0cBAME4wMYoUy7aDuOzPlZCdA5fG0VZBgUqgcJZBECZAxa0FbsqasGZAFUlQMrAXkZC8ZACtNDtP0YiUBmeMlX6OKkcuVp2nXeUOdiH9HkSZAhittEpmwCicDSuUvpRa4wAgdM4oEwFLNCZCaANuMLCruuY0CTnOSJY5vr4apXBcIOfNqo4iiCrUCsdUDZAUE7IFgWwZDZD"

def scarpe_facebook():
# build the URL for the API endpoint
	host = "https://graph.facebook.com"
	path = "/1542318536060253/feed"
	params = urllib.urlencode({"access_token": ACCESS_TOKEN})

	url = "{host}{path}?{params}".format(host=host, path=path, params=params)

# open the URL and read the response
	resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype 
	me = json.loads(resp)
	pprint.pprint(me)
	return me
# display the result
#pprint.pprint(me)


scarpe_facebook()