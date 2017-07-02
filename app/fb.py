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


ACCESS_TOKEN = "EAAOmOU5RCZAkBAI8rteUTNl2NTp2ZBCqb9pY8VKrxkpB68SsU5XDftzZAegzejZC8yso44mILljyXZAsJCH8MJ2dgGq0LA91gqZCjAZBWwrpU5t0HHGHSdECPd9TcjApzXo4d2bOCgstUmpFweabFz8TfBKUK3g80GS61oZAjyamBmtXl4n5IuTLZAtlEUBi8R5673E72zBwcEZAAoAoGcoK1m"

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