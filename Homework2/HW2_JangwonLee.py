#Jangwon Lee

#3.20 Write a for loop that iterates over a list of strings 1st and prints the first three characters of every word.
lst = ['January', 'Febrarury', 'March']
for i in range (0,len(lst)):
    print(lst[i][0:3])
# [0:3] makes us to get the first three characters. if it is [0:2] instead of [0,3], we get the first character and the second character of the word.

#3.25

names = eval(input("Enter list:"))
first_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
for name in names:
    if name[0] in first_letters:
        print(name)

#3.41

FirstName = input("Please enter a first name: ")
LastName = input("Pleaes enter a last name: ")

def lastF(FirstName,LastName):
    new_lastF = LastName +","+ FirstName[0] +"."
    return new_lastF

print(lastF(FirstName,LastName))

#3.44

time = eval(input("Enter the time elapsed (in seconds): "))

def distance():
    if not time in km:
        return time
    
sound_speed = 340.29 * time
convert = sound_speed/1000

print(convert)

#Random Cinema

import random
def movies (playing_mov):

    num_movies = eval(input("Please enter a number of movies you'd like to generate: "))
    print("Welcome to Randoplex! Currently playing movies are: ")

    for i in range(0,num_movies):
        print(random.choice(playing_mov),random.choice(playing_mov),random.choice(playing_mov))
        # the reason why I put comma is that comma put a space between words automatically, so I don't need to use " " to make a space between words.
movies(eval(input("Please enter a list of words: ")))


