import sys
#holy shit lol
from mapprocessor import returnmiddleschools,returnhighschools,returnelementaryschools
from tkinter import *
selection = ""

class mapwindow:
    def __init__(self, master):
        self.master = master

        root.geometry('{}x{}'.format(500, 500))

        master.title("well i guess we're gonna use tinker")

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()

        #self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack()

        schools = StringVar(master)
        schools.set("one") # default value

        w = OptionMenu(master, schools, "one", "two", "three")
        w.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()



    def greet(self):
        print("Greetings!")

    def schools(self):
        print("die")#empty lines here

    def givemethetype(self):
        print("jesus h christ")


root = Tk()
my_gui = mapwindow(root)
root.mainloop()
