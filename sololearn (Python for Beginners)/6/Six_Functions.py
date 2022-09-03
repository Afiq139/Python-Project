# Search Engine


# You’re working on a search engine. Watch your back Google!

# The given code takes a text and a word as input and passes them to a function called search().

# The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

# Sample Input
# "This is awesome"
# "awesome"

# Sample Output
# Word found
# Define the search() function, so that the given code works as expected.

text = input()
word = input()

def search(text,word):
    if word in text:
      return print("Word found")
    else:
      return print("Word not found")
    
  
search(text, word)