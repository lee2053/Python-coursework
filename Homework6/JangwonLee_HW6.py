#Jangwon Lee
#HW 6

#8.20 Develop a class BankAccount that supports these methods:


class BankAccount(object): #develop a class BankAccount
    def __init__(self, balance = 0): #create method that intialized the bank account balance to the value of the input argument, or to () if no input argument is given
        self.accountBalance = balance

    def withdraw (self,amount): #create withdarw methhod that takes an amount as input
        self.accountBalance -= amount #and withdraws it form the balance

    def deposit(self,amount): #create deposit method that takes an amount as input 
        self.accountBalance += amount #add it to the balance

    def balance(self):  #create balance method
        return float(self.accountBalance) #returns the balance on the account and make it 2 decimals using float().

#main
x = BankAccount(700)
print (x.balance())

x.withdraw(70)
print (x.balance())

x.deposit(7)
print(x.balance())


#---------------------------------------------------------------------------------
#8.22

class Worker(object): #Implement class Worker

    def __init__(self, name, rate): #define initial values
        self.name = name # of name
        self.rate = rate # of rate

    def changeRate(self, newRate): #define changerate function
        self.rate = newRate #that takes the new pay rate as input of ate

    def pay(self,period): #define pay function
        return 'Not Implemented' #that prints not implemented

class HourlyWorker(Worker): #develop class HourlyWorker as subclass
    def pay(self, time): # overloads the inderited method pay()
        if time > 40: # when employees worked more than 40 hours
            return (self.rate * 40 ) + 2 * ((time - 40) * self.rate)
        else: # when employees worked less than or equal to 40 hours
            return self.rate * time

class SalariedWorker(Worker):#develop class SalaridWorker as subclass
    def pay(self, time = 40): #the salary of salaried workers is fixed. 
        return self.rate * 40 #although they worked more than 40 hours, they get paid for 40 hours.
    
        
##>>> w1=Worker('Joe',15)
##>>> w1.pay(35)
##'Not Implemented'
##>>> w2 = SalariedWorker('Sue',14.50)
##>>> w2.pay()
##580.0
##>>> w2.pay(60)
##580.0
##>>> w3 = HourlyWorker('Dana',20)
##>>> w3.pay(25)
##500
##>>> w3.changeRate(35)
##>>> w3.pay(25)
##875
#---------------------------------------------------------------------------------------------------------

#8.35 

class Stack(object): #create class stack

    data = [] #create an empty list variable

    def __len__(self): #create method __len__
        return len(self.data) # that returns length

    def push (self,item): # create function that takes item as input
        self.data.append(item) #append items at last position of stack
      
    def pop(self): #create method pop()
        return self.data.pop() #remove items and present at last position
    
    def isEmpty(self): #create function that tests whether the stack is empty.
        if len(self.data) == 0: # if it is empty
            return True #return true
        else: #otherwise,
            return False #return false

    def __str__(self): #create function that print stirngs out from the list.
        return str(self.data)
##    
#main
s= Stack()
s.push('plate 1')
s.push('plate 2')
s.push('plate 3')
print(s)
print(len(s))

print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())

#------------------------------------------------------------------------------
#8.40

class BankAccount(object): #develop a class BankAccount
    account = 0 
    def __init__(self, balance): #create method that intialized the bank account balance to the value of the input argument, or to () if no input argument is given
        if balance < 0:
            print("ValueError: Illegal Balance")
        BankAccount.account += 1
        self.accountNumber = str(BankAccount.account)
        self.accountBalance = balance

    def withdraw (self,amount): #create withdarw methhod that takes an amount as input
        if self.accountBalance - amount <0:
            self.accountBalance -= amount
            return ('Overdraft') #and withdraws it from the balance
        elif amount > self.accountBalance:
            self.accountBalance -= amount
            return ('Illegal Balance')
        else:
            self.accountBalance -= amount

    def deposit(self,amount): #create deposit method that takes an amount as input
        if amount < 0 :
            self.accountBalance += amount
            return ('Negative Deoposit')
        else:
            self.accountBalance += amount
    def balance(self):  #create balance method
        return float(self.accountBalance) #returns the balance on the account and make it 2 decimals using float().
    



