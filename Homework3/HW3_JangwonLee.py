#Jangwon Lee

#4.13 Write Python Boolean expressions that correspond to these propositions:
s = 'abcdefghijklmnopqrstuvwxyz'
#(a)The slice consisting of the second and third character of s is 'bc'.
>>> 'bc' == s [2:3]
False
>>> 

#(b)The slice consisting of the first 14 characters of s is 'abcdefghijklmn'.
>>> 'abcdefghijklmn' == s[:14]
True


#(c)The slice of s excluding the first 14 characters is 'opqrstuvwxyz'.
>>> 'opqrstuvwxyz' == s[-12:]
True


#(d)The slice of s exclusding the first and last characters is 'bcdefghijklmnopqrstuvw'.
>>> 'bcdefghijklmnopqrstuvw' == s[1:25]
False


#4.16 Implement a program that requests three words (strings) from the user. Your program
#shuold print Bollean value True if the words were entered in dictionary order; other wise nothing is printed.

first_word = input("Enter first word: ")
sec_word = input("Enter second word: ")
third_word = input("Enter third word: ")
#To check words in dictionary order, use <= (Boolean comparison operation which is Less than or Equal)
if first_word <= sec_word <= third_word:
    #'True' will be printed only when it is true.
    print('True')

#4.20
#Given string values for the sender, recipient, and subject of an email, write a string formant
#expression that uses variables sender, recipient, and subject and that prints as shown here:

# set sender, recipient, and subject as strings.
sender = 'tim@abc.com'
recipient = 'tom@xyz.org'
subject = 'Hello!'

#define frm, to, and Subject as strings
frm = "From: " + sender
to = "To: " + recipient
Subject = "Subject: " + subject

print(frm)
print(to)
print(Subject)

# 4.23
#Write a function average() that takes no input but requests that the user enter a sentence.
#Your function should return the average length of a word in the sentence.
#create average() function
def average():
    #return the average length of a word in the sentence.
    return average

#make user enter a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()

average = sum(len(word) for word in words)/len(words)
print (average)

#4.25 Write function voewlCount() that takes a string as input and counts and prints the number
#of occurences of vowels in the string.
vowels = 'aeiou'

def vowelCount(sentence):
    print('a,e,i,o, and u appear, respectively ', end="")
    for vowel in vowels:
        print(',', sentence.count(vowel), sep="", end="")
    print(' times')
    
