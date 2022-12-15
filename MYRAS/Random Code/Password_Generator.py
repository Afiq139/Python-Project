import random
#List with random words
random_strings=['nectar',
'expert',
'analyzer',
'teasing',
'glucose',
'stilt',
'circus',
'meet',
'scum',
'drill',]
#Password function
def password_generator():
    random_word= random.choice(random_strings)
    random_integer=random.randrange(1000,9999)
    password= random_word + str(random_integer)
    print(password)
#Loopx10
for x in range(3): #for x in range(x):
    password_generator()