from tkinter import *

OPTIONS = [
"Lemon, Lime & Bitter",
"Raspberry Cordial",
"Peach Ice Tea",
"Cloudy Applt Juice"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    print ("value is:" + variable.get()) #here we gettin input variable

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
