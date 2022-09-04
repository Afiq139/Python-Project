# Title Encoder


# You are given a file named "books.txt" with book titles, each on a separate line.
# To encode the book titles you need to take the first letters of each word in the title and combine them.
# For example, for the book title "Game of Thrones" the encoded version should be "GoT".

# Complete the program to read the book title from the file and output the encoded versions, each on a new line.
# You can use the .split() method to get a list of words in a string.

file = open("/usercode/files/books.txt", "r")

#your code goes here

cont = file.readlines()
for line in cont: 
    words = line.split()
    for word in words: 
      print(word[0],end="")
    print() 

file.close()
