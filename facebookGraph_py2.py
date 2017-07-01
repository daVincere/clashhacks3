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


ACCESS_TOKEN = "EAAOmOU5RCZAkBALHAcPV0ywWh5rzh8czlUGyzn437s7M4376SQULZBoaaD0RzikbFtPIrvB25VTrphGLmmEcWk2pe41w9EB23Mu3tSWRpwi3zu1qKLHejsMJyar5IoEj1FxhLmyGHlkGxs4PJTDesZCM0PtbUoYCisKARzeMAAbpXH0GKMk5CUDPng8JI0ZD"

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/1849134045317304/feed"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{params}".format(host=host, path=path, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype 
me = json.loads(resp)

# display the result
pprint.pprint(me)