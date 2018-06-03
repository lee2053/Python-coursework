#Group4 Homework 1
#Chuck Kim, Jangwon Lee, Minsoo Kang
#4.29

#define a function to opening a file.
def stats(file_name):
    text_file =open("example.txt", "r") 
    contents = text_file.read()
    text_file.close()

#Count the number of lines, words, and characters.
    line_count = contents.count("\n")
    word_count = len(contents.split())
    char_count = 0

    for letter in contents:
        char_count += 1
    print("line count:", line_count)
    print("word count:", word_count)
    print("character count:", char_count)

#a result of this question:
#stats('example.txt')

#4.30
#define a function distribution of students' grade 
def distribution(file_name):
    file1=open(file_name,"r") # open a file and close
    file_contents =file1.read()
    file1.close()
#split what it's read
    num_grades= file_contents.split()

    A = num_grades.count("A")
    Am = num_grades.count("A-")
    Bp = num_grades.count("B+")
    B = num_grades.count("B")
    Bm = num_grades.count("B-")
    Cp = num_grades.count("C+")
    C = num_grades.count("C")
    Cm = num_grades.count("C-")
    F = num_grades.count("F")
#print
    print(A, "students got A")
    print(Am, "students got A-")
    print(Bp, "students got B+")
    print(B, "students got B")
    print(Bm, "students got B-")
    print(C, "students got C")
    print(Cm, "students got C-")
    print(F, "students got F")

#the rusult of this question
#distribution('grades.txt')


#4.31
#define a function duplicate
def duplicate(file_name):
    text_file = open(file_name,"r") #open a file and close it.
    contents = text_file.read()
    text_file.close()

#make a new_file as a varialbe.
    new_file = contents.split()
#for loop, if there is any duplicate word in a file then retrun True. Otherwise, return False.
    for word in new_file:
        if new_file.count(word)> 1:
            return True
    return False
    
#results of this question    
##>>> duplicate('Duplicates.txt')
##True
##>>> duplicate('noDuplicates.txt')
##False


#Chess Problem


#Step 1: ask user to open a file and read the file contents.

user_file = input("Please enter a game file to load:")

game_file = open(user_file, "r")
game_line = game_file.readlines()
#must close the file atter opening it.
game_file.close()

print ("Game moves so far: ")

##Step 2: Use the format method to display the contents of the file formatted.

count = 0

##display chess moves from text file
for line in range(len(game_line)):
    game_line[line] = game_line[line].strip()

for line in game_line:
    count += 1
    print(count, "White move", line[0], "to", line[1:3], "\t Black moves", line[4], "to", line[5:7])



##Step 3: Ask the user to enter moves for Player1 and Player2.

while True:
    player1 = input("Please enter Player 1's move: ")
    player2 = input("Please enter Player 2's move: ")

##Step 4:write out the entire game.
    new_move= open(user_file,"a")
    new_move.write(player1 + " " + player2)
    new_move.write("\n")
    new_move.close()
    another_turn = input("Would you like to enter another trun Y/N:")
    if another_turn.upper() == 'N':
        break


print("Thank you, your game has been saved.")    
