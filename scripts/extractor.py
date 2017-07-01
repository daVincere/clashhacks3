from textblob import TextBlob as tb
from stop_words import get_stop_words

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')


# from stop_words import safe_get_stop_words

# stop_words = safe_get_stop_words('unsupported language')

text = "this is my name and its good"

# we clean the irrelevant text out of the text
cleaned_text = []

# cleaned_text = text
# counting the number of words
# def count_words(x):
# 	count = 0
# 	words = x.lower().split(" ")

# 	for word in words:
# 		count +=1
# 	return count
# words = text.lower().split(" ")
def extract(text):
	words = text.lower().split(" ")
for word in text:
		if word not in stop_words:
			cleaned_text.append(word)
	
print (cleaned_text)
# # create a blob out of the cleaned text to get meaning out of it
# blob = tb(cleaned_text)

# # printing the result
# print blob.tags