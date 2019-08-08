from tkinter import *

root = Tk() #constructor for just blank window

def printDrink(event):
    print('ButtonClicked')

#Create and add top frame
topFrame = Frame(root)
topFrame.pack(side=TOP)  #top container
#Create and add top frame
bottomFrame = Frame(root)  #bottom container
bottomFrame.pack(side=BOTTOM)

#Create Lable
txtLablel = Label(topFrame, text="Please Select Your Drink")
#Create buttons
drink1 = Button(topFrame, text="Lemon, Lime $ Bitters", fg="red")
drink1.bind('<Button-1>', printDrink) #bind function to a button when left click occurs
drink2 = Button(topFrame, text="Raspberry", fg="red")
drink2.bind('<Button-1>', printDrink)
drink3 = Button(bottomFrame, text="Peach Ice Tea", fg="red")
drink3.bind('<Button-1>', printDrink)
drink4 = Button(bottomFrame, text="Cloudy Apple Juice", fg="red")
drink4.bind('<Button-1>', printDrink)

#add buttons to our layout
txtLablel.grid(row=0, columnspan=2)#where to put it, pack() just packs it anywhere
drink1.grid(row=1, column=0, sticky=W)
drink2.grid(row=1, column=1, sticky=E)
drink3.grid(row=2, column=0, sticky=W)
drink4.grid(row=2, column=1, sticky=E)

root.mainloop() #we need this windows continuously on our screen by infinite loop