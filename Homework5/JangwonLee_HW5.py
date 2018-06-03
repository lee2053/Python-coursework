#Jangwon Lee HW 5

#6.20
#create a function named reverse() 
def reverse(phonebook) :
    
    reverse_pb= {}
    #use for loop to make repeat pairs in key.
    for key in phonebook:
        #put the value in the current key    
        newkey = phonebook[key]
        reverse_pb[newkey] = key
    #return the reverse phone book
    return reverse_pb
#the answer is
#>>> phonebook={'Smith,Jane':'123-45-67','Doe,John':'987-65-43','Baker,David':'567-89-011'}
#>>> reverse(phonebook)
#{'123-45-67': 'Smith,Jane', '987-65-43': 'Doe,John', '567-89-011': 'Baker,David'}

#6.22

#create a function
def mirror(string):
    #define letters that can bemirrored by alphabets
    reverse = {'b':'d','d':'b','o':'o','p':'q','q':'p','v':'v','w':'w','x':'x'}
    #if the string can be represented its mirror image by using reverse that we have defined with alphabets
    try:
        return "".join(reverse[key] for key in reversed(string))
   
    except KeyError:
        #return the message "INVALID"
        return "INVALID"

##>>> mirror('vow')
##'wov'
##>>> mirror('wood')
##'boow'
##>>> mirror('bed')
##'INVALID'

#6.24
#create names () function
def names():
    #create an empty dictionary
    name_list = {}
    #use while loop cuz we don't know how many times the user enters names
    while True:
        #ask the user to enter the number of a students
        names = input("Enter next name:")
        #when the user enters the emtpy stirng, loop stops
        if names == " ":
            break
        #otherwise, keep asking the user to enter names
        else:
            #check if the name user entered already exists in the dictionary
            if names in name_list:
                #the function will count by incrementing the repeated names
                name_list[names] +=1
            #when the input does not exists in the dictionary, put the name user entered into dictionary
            else:
                name_list[names] = 1
    #when there is only one person, print this
    message1 = "There is {} student names {}."
    #when there are more than two people.
    message2 = "There are {} student names {}."


    for name in name_list:
        #if there are more than one person who has the same name, print message2.
        if name_list[name] >1:
            print(message2.format(name_list[name],name))
        #if there is only one person who has single name, print message1.
        else:
            print(message1.format(name_list[name],name))
            
##>>> names()
##Enter next name:Valerie
##Enter next name:Bob
##Enter next name:Valerie
##Enter next name:Amelia
##Enter next name:Bob
##Enter next name: 
##There are 2 student names Valerie.
##There are 2 student names Bob.
##There is 1 student names Amelia.

#6.28
#create translate()function that takes dictionary mapping word as input
def translate(second):
    #make user to enter the word
    first_lang_word= input("Enter a word that you want to translate: ")
    #use while loop cuz we don't know how many word the user wants to translate
    while True:
        #check if the dictionary contains the word that user entered
        if first_lang_word in second:
            #give out the word in second language from the dictionary
            print(first_lang_word, "can be translated as", second[first_lang_word])
        #otherwise, print out underscores
        else:
            print(first_lang_word, "is not in your dictionary ", "___.")
        #continue to ask for user's input
        first_lang_word = input("Enter a wrod that you want to translate :")
        
#6.33
# import random to use random and randint
import random
#create a function named diceprob() that takes as input a possible result 'r'
def diceprob(r):
    total_rolls = 0
    count = 0
    # use while loop cuz we do not know how many times it would take
    #but we know that we only want to count the input number until 100 rolls.
    while count <100:
        #we want the roll pair of dice to be an integer between 2 and 12.
        #so use randint function from random to get random number.
        #we need the sum of two random number.
        roll = random.randint(1,7)+ random.randint(1,7)
        #as we roll the dice, we need to count how many we rolled the dice.
        #whenever we roll a dice, add 1 total rolls each time.
        total_rolls +=1
        #add 1 to the count if the roll equals to number user input at the first place
        if roll == r:
            count += 1
    #after getting done 100 rolls of r, print this message
    print("It took", total_rolls, "rolls to get 100 rolls of", r)

##the answer is            
##>>> diceprob(2)
##It took 3631 rolls to get 100 rolls of 2
##>>> diceprob(3)
##It took 2595 rolls to get 100 rolls of 3
##>>> diceprob(4)
##It took 1723 rolls to get 100 rolls of 4
##>>> diceprob(5)
##It took 1244 rolls to get 100 rolls of 5
##>>> diceprob(6)
##It took 978 rolls to get 100 rolls of 6
##>>> diceprob(7)
##It took 866 rolls to get 100 rolls of 7  
