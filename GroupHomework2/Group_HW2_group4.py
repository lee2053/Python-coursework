
#INFO-I 210 Group HW 2
#Group 4
#Chuck Kim, Jangwon Lee, Minsoo Kang

#9.17
from tkinter import *
#Develop a GUI application whose purpose is to compute the monthly mortgage payment given
# loan amount(in $)
# interest rate(in %)
# loan term

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    #create 3 labels and entry boxes for users to enter loan amount, interest rate, and loan term
    def create_widgets(self):

        #loan amount
        self.amount_lbl = Label(self, text = "Loan Amount: ").grid(row = 0, column = 0, sticky = W )

        self.amount_ent = Entry(self,width =40)
        self.amount_ent.grid(row = 0, column = 1)

        #interest rate
        self.rate_lbl = Label(self,text ="Interest Rate: ")
        self.rate_lbl.grid(row = 1, column=0, sticky = W)

        self.rate_ent = Entry(self, width =40)
        self.rate_ent.grid(row = 1, column = 1)

        #loan term

        self.term_lbl = Label(self, text="Loan Term: ")
        self.term_lbl.grid(row = 2, column = 0 , sticky = W)

        self.term_ent = Entry(self, width =40)
        self.term_ent.grid(row = 2, column = 1)

        #create a button that computes the monthly mortgage payment when clicked
        self.compute_bttn = Button(self, text = "Compute Mortgage")
        self.compute_bttn["command"] = self.compute
        self.compute_bttn.grid(row = 4, column = 0, columnspan = 2)

        #compute and display the monthly mortgage payment in a text box
        self.m_txt = Text(self, width = 40, height = 10, wrap = WORD)
        self.m_txt.grid( row = 5, column = 0, columnspan = 3)

    def compute(self):

        c = float(self.rate_ent.get())/1200

        a_c = float(self.amount_ent.get()) * c

        #(1 + c)^t

        onect = (1 + c) **float(self.term_ent.get())

        # numerator = a * c * (1 + c)^ t
        
        num = a_c * onect

        # denomerator = (1 + c) ^ t - 1
        denom = (1 + c)**float(self.term_ent.get()) -1

        #Contents = implement num and denom

        contents = num/denom

        #delete any existing text and insert the monthly mortgage payment

        self.m_txt.delete(0.0, END)
        self.m_txt.insert(0.0, contents)
        

#main
root = Tk()
root.title("Monthly Mortgage Payment")
root.geometry("330x260")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()


#-------------------------------------------------------------------------
#9.24
from tkinter import *
from time import *   # To use the time fucntions, import time

class Application(Frame): #Develop an application


    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self): #Make label the GUI
        self.lbl1 = Label(self, text="Type: ")
        self.lbl1.grid()
        
        #make the text box that you can type.
        self.txt = Text(self, width = 60, height = 10, wrap = WORD)
        self.txt.grid()    
         #bind an event to it for a generic key press      
        self.txt.bind('<KeyPress>', self.time)
        self.txt.focus_set()

        self.status = True   #set True as status variable to use it throughout
        self.time_start = "" 
        self.time_end = ""   
        self.time_taken = 0  
        self.word_count = 0  

        self.time_lst = [] # Create variables to use calcuate average time.
        self.time_total = 0
        self.word_average = 0        

        #Create label to show how much time takes 
        self.lbl2 = Label(self, text = "It took " +str(self.time_taken) + " seconds.")
        self.lbl2.grid()
        #Create label to show average words / minute
        self.lbl3 = Label(self, text =  str(self.word_average) + "  words  /  minute.")
        self.lbl3.grid()                   

    def average_min(self): #Make the function to calculate the average words / minute
        #add all the time_taken 
        self.time_total = sum(self.time_lst)    
        if self.time_total > 0:     
            if self.time_lst == []:     
                self.word_average = 0   
            else:  
                self.word_average = round(60/(self.time_total/len(self.time_lst)), 2)
          
            self.lbl3["text"] =  str(self.word_average) + "  words  /  minute."
    def time(self, event):  #make the function that takes self and events.
        
        if self.status == True:    #if status is true, take the time in time_start
            self.time_start = time()
            self.status = False           #end it 

        if event.keysym ==  "space": #when users type empty character.            
            self.time_end = time()
            self.status = True
            self.word_count += 1    #add 1 to the variable.
            self.average_min()     #use average_min function to get average per minute.
            self.time_taken = round(self.time_end - self.time_start, 2) 

        if self.time_taken > 0: 
            if event.keysym == "space":  #When users type nothing               
                self.time_lst.append(self.time_taken)              
                self.lbl2["text"] = "It took " + str(self.time_taken) + " seconds to write the word."
            else: 
                self.lbl2["text"] = "It took " + str(0) + " seconds to write the word."



# main
root = Tk()
root.title("Measures how fast you type")
root.geometry("450x255")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()


#-----------------------------------------------------------------------
#9.28 ~ 29

from tkinter import* 
from calendar import monthrange #importing calendar 
from tkinter.messagebox import*
from tkinter.simpledialog import*

class Calendar(Frame):
    events = {} #dictionary for an event on calendar

    def __init__(self, master, year, month=1):
        
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets(year,month) # this makes that we can have a visual elements.
        self.master = master
        
    def create_widgets(self,year,month):
        
        self.year = year
        self.month = month

        lable_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] # labels of the calendar

        for i in range(7): 
            
            self.title = Label(self,text = lable_days[i])
            self.title.grid(row = 0, column = i)
            
        week_day, num_days = monthrange(self.year, self.month) #gets days of weeks and number of days
        
        week = 1

        for i in range(1, num_days + 1): # using for loop to make buttons for calendar; for each number in calendar button is made
            button = Button(self, text = str(i)) 
            button.configure (command = lambda b = button: self.event(b)) #recieved help in office hours
            button.grid(row = week, column = week_day)   # format row for week and column for week days
            
            week_day += 1
            if week_day > 6: # a week is not more than 7 days
                week += 1
                week_day = 0 
 
        self.previous = Button(self, text = "Previous", command = self.previousMonth) # create button for "previous" and "next"
        self.previous.grid(row = 6, column = 0, columnspan = 3)
        self.next = Button(self, text = "Next", command = self.nextMonth)
        self.next.grid(row = 6, column = 3, columnspan = 3) 
        
    def previousMonth(self): # show privous month of calendar
        
        Frame.destroy(self)
        if self.month > 1:
            self.__init__(self.master, self.year, self.month - 1)
            self.__init__(self.master,self.year - 1, month = 6)
            
    def nextMonth(self): # show next month of calendar
        
        Frame.destroy(self)
        if self.month < 12:
            self.__init__(self.master, self.year, self.month + 1)
            self.__init__(self.master, self.year + 1, month = 6)
            
    def event(self,button): # we can mark an even on the calendar
        
        day = button["text"] #when we have an event in the calendar print the event

        if day in self.events:
            message = self.events[day]

        else:
            message = ""
        note = simpledialog.askstring('example', 'Enter text', initialvalue = message)
        if note:
            self.events[day] = note

#main
root = Tk()
root.title("Calendar")
root.geometry("500x500")
app= Calendar(root,2012,2)
root.mainloop()
