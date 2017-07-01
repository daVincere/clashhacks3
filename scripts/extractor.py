from textblob import TextBlob as tb
from stop_words import get_stop_words

import keywords

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')

text = "I want a computer engineer to do web stuff"
blob = tb(text)

# dictonary
dict = {
	"NN":["web",
		"android",
		"developer",
		"backend",
		"frontend",
		"full-stack",
		"website"
		],

	"VBD":[
		"want",
		"need",
		"needed",
		"required"
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

for words in cleaned:
	if words in dict["NN"] or words in dict["VBD"]:
		call = True
		break
	else:
		call = False


if call == True:
	print "Call the computer company"
else:
	print "Call no one"