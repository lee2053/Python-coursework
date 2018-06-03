#Jangwon Lee
#Practical 1 5/30/2017

#Section 1,2 - Loading the Data:
#-------------------------------------------------------------------------------------
from tools import *
#use while loop so that it keeps running until the user enters a stop.

while True:
    #make the user enters the state where they want to compute
    state = input("Which state's totals would you like to compute? (or STOP) ")
    #.upper makes input as the uppercased word.
    if state.upper() != "STOP":
    #loading a data
        text_file = open(state+".txt","r")
        file_contents = text_file.readlines()
        text_file.close()
    #if the user enters a "STOP", the look will be terminated.
    else:
        break
        
#create an empty dictionary
    dictionary = {}
#create an empty list
    clean_data =[]
    #find item in the file_contents.
    for item in file_contents:
        item = item.strip('\n') # use .strip to remove enter and '\n'
        item = item.split('\t') # divide words up in each line finding tab so that I make them a list
        # print(item) if we print item, it shows every single data from the text file.
        total = 0
        name = item[0]
        if name in dictionary: # put the first of the list(the name) into the dictionary
            dictionary[name] += int(item[1])
        else:
            dictionary[name] = int(item[1])
    print(dictionary) #this shows the dictionary that has been computed total votes for each candidates.
#------------------------------------------------------------------------------------------
#Section 3 - FInd the Winnder! :
    

    headers = ['Name','Votes']
    padding = 15

    data = dictionary.items()
    lines = []
 #   print(data)
#    table_print(headers, data, padding)
# When a table is printed here, it's not sorted. so we need to make it being sorted.   

    new_result = [] #we need to get data (.items()) position 1

    for pair in data: # pair is a tuple in the dictionary!
        new_result.append(pair[1]) # append the datas to a list
    new_result.sort(reverse=True) # it makes the table to be sorted. 
    #print(new_result) # check mark

    for item in new_result:
        for key in dictionary:
            if item == dictionary[key]:
                lines.append((key, item))
    table_print(headers, lines, padding)

#--------------------------------------------------------------------------------------------
#Section 4 - Show Percentages :

##    header =["Name", "Percentage"]
##
##    for percentage in new_result:
##        for i in dictionary:
##            if percentage == dictionary[i]:
##                dictionary[i] += dictionary[i]
##                dictionary[i][1] = sum(dictionary[i][1].values())
##                
##            print(dictionary[i])
##            lines.append((per, percentage))
##    table_print(header, lines, padding)
#-------------------------------------------------------------------------------------


