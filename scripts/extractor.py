from textblob import TextBlob as tb
from stop_words import get_stop_words

# import app.views

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')

try:
	text = "Hi, Any freelancer who can build a very simple app to swipe left and right (just like tinder, but definately not for dating). I need a quote and timeframe to build it. I'll only contact you if you give me quote and timelines first."
	link = "https://www.facebook.com/groups/delhistartupnetwork/permalink/728027040733150/"
except:
	pass


text = text.lower()
print text
blob = tb(text)

realiblity = blob.sentiment.polarity

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
		dev_jobs(text, link, realiblity)
	elif words in cleaned and words == "advertise":
		dev_market(text, link, realiblity)
	else:
		print "Call no one"
else:
	print "out of order"

