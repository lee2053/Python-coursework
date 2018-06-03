from tkinter import*
import random

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.title = Label(self,text="Spiral Drawing Canvas")
        self.title.grid(row = 0, column = 0 ,columnspan =3)

        self.canvas = Canvas (self,height = 360, width = 360)
        self.canvas.grid (row =1, column = 0, columnspan = 2, rowspan = 5)

        self.txt_lbl = Label(self,text="How Many Total Loops Would You Like?")
        self.txt_lbl.grid(row = 1, column = 2, columnspan = 1)

        self.txt_ent = Entry(self, width = 15)
        self.txt_ent.grid(row = 1, column = 3)

        self.wth_lbl = Label(self, text = "Line Width:")
        self.wth_lbl.grid(row = 2, column = 1, columnspan = 2)

        self.color_lbl = Label(self, text= " Line Color:")
        self.color_lbl.grid( row = 3, column = 1, columnspan = 2)

        self.wth = StringVar()
        self.wth.set("1")


        Radiobutton(self, text="1", variable = self.wth,value ="1").grid(row = 2, column = 2)
        Radiobutton(self, text="2", variable = self.wth,value ="2").grid(row = 2, column = 2, sticky = E)
        Radiobutton(self, text="3", variable = self.wth, value ="3").grid(row = 2, column = 3)
         


        self.color = StringVar()
        self.color.set("black")
 
        Radiobutton(self, text="Black", variable = self.color, value = "black").grid(row = 3, column = 2)
        Radiobutton(self, text="Red", variable = self.color,  value = "red").grid(row = 3, column = 2, sticky = E)
        Radiobutton(self, text="Blue",variable = self.color, value = "blue").grid(row = 3, column = 3)

        self.spiral = PhotoImage(file="spiral.gif")
        self.random = PhotoImage(file = "random.gif")

        self.reveal = [True, True]
                
        self.spiral_bttn = Button(self, image = self.spiral, command = self.draw_spiral)
        self.spiral_bttn.grid(row= 4, column =2)
        
        self.random_bttn = Button(self, image = self.random , command = self.draw_random)
        self.random_bttn.grid(row = 4, column = 3, sticky = W)

        self.x, self.y = 150 , 150
        
    def draw_spiral(self):
        
        width = int(self.wth.get())
        colors = self.color.get()
        times = int(self.txt_ent.get())
        length = 5

        
        self.canvas.create_line(self.x - length, self.y, self.x + length, self.y, width = width, fill = colors)
        self.canvas.create_line(self.x + length , self.y, self.x + length, self.y+length *2 , width = width, fill= colors)
        self.canvas.create_line(self.x + length  , self.y + length *2 , self.x - length *2, self.y + length *2 , width = width, fill= colors)
        self.canvas.create_line(self.x - length *2 , self.y +length *2 , self.x - length *2 , self.y - length *2, width = width, fill= colors)        

 

    def draw_random(self):
        width_random = [1,2,3]
        color_random = ["black","red","blue"]
        
        colors = random.choice(color_random)
        width = random.choice(width_random)
        length = 5

        self.canvas.create_line(self.x - length, self.y, self.x + length, self.y, width = width, fill = colors)
        self.canvas.create_line(self.x + length , self.y, self.x + length, self.y+length *2 , width = width, fill= colors)
        self.canvas.create_line(self.x + length  , self.y + length *2 , self.x - length *2, self.y + length *2 , width = width, fill= colors)
        self.canvas.create_line(self.x - length *2 , self.y +length *2 , self.x - length *2 , self.y - length *2, width = width, fill= colors)        
        
        
#main
root = Tk()
root.title("Spirals!")
root.geometry("700x400")

app = Application(root)
root.mainloop()
