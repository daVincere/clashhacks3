from textblob import TextBlob as tb
from stop_words import get_stop_words

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')


text = raw_input("Please enter the string")

# # create a blob out of the cleaned text to get meaning out of it
blob = tb(text)

# printing the result
print blob.tags