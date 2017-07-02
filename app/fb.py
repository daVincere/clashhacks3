import os
import json
import urllib
import pprint


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
		#print me
		print me['data'][0]['id']
		print me['data'][0]['message']
		
	#return me
	# display the result
		#pprint.pprint(str(me.data))


scarpe_facebook()