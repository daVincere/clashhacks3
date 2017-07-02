import os
import json
import urllib
import pprint
import requests

text = list()

groups = [
1557032894516446,
217478508419972,
1849134045317304,
217478508419972,
1192426724120440,
1410790809134759,
1533837663604401,
1542318536060253,
1438491639744224,
1124009880957693,
963046590478093,
232514253599135,
1673185433000576,
]

links = [
"https://www.facebook.com/photo.php?fbid=145167342723761&set=gm.1883679571892093&type=3",

"https://www.facebook.com/photo.php?fbid=148442795725776&set=gm.1883531878573529&type=3",

"https://www.facebook.com/photo.php?fbid=145166072723888&set=gm.1883678465225537&type=3",

"https://www.facebook.com/photo.php?fbid=846277408862450&set=gm.1883669018559815&type=3",

"https://www.facebook.com/photo.php?fbid=1435950169783975&set=gm.1882952331964817&type=3",

"https://www.facebook.com/photo.php?fbid=760120124173654&set=gm.1883612018565515&type=3",

"https://www.facebook.com/photo.php?fbid=760120124173654&set=gm.1883612018565515&type=3",

"https://www.facebook.com/photo.php?fbid=490729481263153&set=gm.1883348675258516&type=3",
"https://www.facebook.com/photo.php?fbid=490729481263153&set=gm.1883348675258516&type=3",
"https://www.facebook.com/photo.php?fbid=148442669059122&set=gm.1883531628573554&type=3"

]


def get_group_data():
	data_link = "https://graph.facebook.com/v2.9/1438491639744224/feed?fields=link,message&limit=10&access_token=EAAOmOU5RCZAkBAMTDSn6FfLuNsgzZClfRlszAHSZBz2AlUW5RUmw0WR70BZBreI2Pz3Fwcn90Pfzq18v1RsdmnGFtFYsfQFI2VrhAUbBP6L5GLv31qI7ImCxbyOtLKBvv7ZCnMlhagdk4ANJdsXtZCVfD5Yr4pwYG6jdZBqqAb5NxjRiUy91UJUFxidB044v6tlZCIa6PZAIGawZDZD"

	r = requests.get(data_link)
	parsed_data = r.json()
	for x in range(10):
		text.append(parsed_data['data'][x])
	return text
		




# def get_links():
#  	links_list = "https://graph.facebook.com/v2.9/1438491639744224/feed?fields=link&access_token=EAAOmOU5RCZAkBAAyFAQEdPtZBfKGzYJ56hOlIDDhuZAiMMCv6XimT6M9LLZAeZCY4KssZCgyIZALFhZAhrshZAqs090VceyNnQL67k3gVdenqN4nGNXnoeh8tTs742jX6JrexBPnZBxqWnPHtLkBEpNsAKos02QTpRwuoxiC0C9JyZAfANTmk7jkN1jcaDM6J0EWlQZD"
#  	r = requests.get(links_list)
# 	json_links = r.json()
# 	json_links = json_links['data']
# get_links()


def get_links():
	return links;

def list_id_from_file():
	with open('id.txt') as f:
	    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = [x.strip() for x in content] 
	for x in content:
		print (x)




# get Facebook access token from environment variable
#ACCESS_TOKEN = os.environ['ACCESS_TOKEN']


ACCESS_TOKEN = "EAAOmOU5RCZAkBAMx1oiIO9M58ZAycSqmDhAapkz56ZCfE1w8lVWW5MD7fnotzqE2THoaw9dUjj7M7D6LNE0AEOfFixu1xP1LfT3VG3r2LPhMPEUZCdafGN32iNMjZCFATBZCr3raxOBGKkbDZA9J5rCHZBD7exPGh2bU4tBsPDyuSoHs4WhAt5I3lbnW0V35nrb99snmlOUZCagZDZD"

def scarpe_facebook():
	for x in groups:
# build the URL for the API endpoint
		host = "https://graph.facebook.com"
		path = "/%s/feed" % x

		params = urllib.urlencode({"access_token": ACCESS_TOKEN})

		url = "{host}{path}?{params}".format(host=host, path=path, params=params)

	# open the URL and read the response
		resp = urllib.urlopen(url).read()

	# convert the returned JSON string to a Python datatype 
		me = json.loads(resp)
		#pprint.pprint((me))
		print me
		#print me['data'][0]['id']
		#print me['data'][0]['message']
		
	#return me
	# display the result
		#pprint.pprint(str(me.data))

