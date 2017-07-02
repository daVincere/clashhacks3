from textblob import TextBlob as tb
from stop_words import get_stop_words

# import app.views

import keywords

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')

text = raw_input("Please enter the text::")
text = text.lower()
print text
blob = tb(text)

# dictonary
dict = {
	"NN":["web",
		"android",
		"developer",
		"backend",
		"frontend",
		"full-stack",
		"website",
		"advertise",
		"market",
		"brand",
		"website",
		"app",
		],

	"VBD":[
		"want",
		"need",
		"needed",
		"required",
		"expansion",
		"requirement",
		]
	}

# # all the words
# print blob.words

# cleaned words
cleaned = []

# getting the cleaned words
for words in blob.words:
	if words not in stop_words:
		cleaned.append(words)
	
print cleaned

# if the words are in the dictionary
for words in cleaned:
	if words in dict["NN"] or words in dict["VBD"]:
		call = True
		break
	else:
		call = False

# if there is a call to be made and we're deciding between the places to call
if call == True:
	if words in cleaned and words == "web":
		dev_jobs()
	elif words in cleaned and words == "advertise":
		dev_market()
	else:
		print "Call no one"
else:
	print "out of order"

