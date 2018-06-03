#Jangwon Lee
#5.29
#Write funcion lastfirst() that takes one argument
def lastfirst(names):
    #make an empty list to append variables. 
    first = []
    last = []
    #divide name into first name and last name and append these to the empty list above.
    for name in names:
        first.append(name.split(', ')[1])
        last.append(name.split(', ')[0])
    return [first] + [last]

print(lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob']))

#5.39
#Write function exclamation() that takes as input a string
def exclamation(word):
    #To find every vowel
    for i in 'aeiouAEIOU':
        #make vowels be replaced by four consecutive copies of itself
        word = word.replace(i, i*4)
    return word + "!"

#When I print this, I got this.
##>>> exclamation('argh')
##'aaaargh!'
##>>> exclamation('hello')
##'heeeelloooo!'

#5.43
#Implement function evenrow() that takes a two-dimensional list of integers
def evenrow(num_list):
    for i in num_list:
        #find the sum of list is odd using sum(i) mod 2 is equal to 1.
        if sum(i) %2 ==1:
        # then return False.
            return False
        #Otherwise, the sum of numbers in the list is even, return True.
    return True

# The output of this problem is :
##>>> evenrow([[1,3],[2,4],[0,6]])
##True
##>>> evenrow([[1,3,2],[3,4,7],[0,6,2]])
##True
##>>> evenrow([[1,3,2],[3,4,7],[0,5,2]])
##False
