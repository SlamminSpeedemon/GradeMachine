from tkinter import *
def entryPanes(): #this function will run each time the user clicks "enter another"
    global entryWindow
    entryWindow = Tk()
    entryWindow.title("student grades")
    standardWidth = 25
    global programming
    global art
    global science
    global math
    global history

    #set up entry boxes
    programming = Entry(entryWindow, width=standardWidth)
    programming.grid(column = 1, row=0)
    art = Entry(entryWindow, width=standardWidth)
    art.grid(column = 1,row=1)
    science = Entry(entryWindow, width=standardWidth)
    science.grid(column = 1,row=2)
    math = Entry(entryWindow, width=standardWidth)
    math.grid(column = 1,row=3)
    history = Entry(entryWindow, width=standardWidth)
    history.grid(column = 1,row=4)

    #set up labels so user knows which is which
    prog = Label(entryWindow, text="Programming: ")
    prog.grid(column=0, row=0)
    ar = Label(entryWindow, text="Art: ")
    ar.grid(column=0, row=1)
    scien = Label(entryWindow, text="Science: ")
    scien.grid(column=0, row=2)
    ma = Label(entryWindow, text="Math: ")
    ma.grid(column=0, row=3)
    hist = Label(entryWindow, text="History: ")
    hist.grid(column=0, row=4)

    #buttons
    save = Button(entryWindow, text = "Next", command = lambda: store())
    save.grid(column = 0, row = 5)
    clear = Button(entryWindow, text = "Clear", command = lambda: done())
    clear.grid(column = 1, row = 5)
    next = Button(entryWindow, text = "Add", command = lambda: addAnother())
    next.grid(column = 0, row = 6, columnspan = 2)


    entryWindow.mainloop()

def store(): #store values in list and destroy
    global grades
    global programming
    global art
    global science
    global math
    global history
    holder = [programming.get(),art.get(),science.get(),math.get(),history.get()]
    holder = roundAll(holder)
    grades.append(holder)

    entryWindow.destroy()

def addAnother(): #store values in list, destroy, and then create entrypanes again
    global grades
    global programming
    global art
    global science
    global math
    global history
    holder = [programming.get(), art.get(), science.get(), math.get(), history.get()]
    holder = roundAll(holder)
    grades.append(holder)#it would be more efficent to have each class have its own list; future development

    entryWindow.destroy()
    entryPanes()

def done():
    entryWindow.destroy()

def roundAll(list):
    for i in range(len(list)):
        if list[i] % 1 >= 0.5:
            list[i] += 0.5
            list[i] = int(list[i])
        else:
            list[i] = int(list[i])
    return list

grades = []  #list that stores grades
entryPanes() #get info and store in list

mainWindow = Tk()
mainWindow.title("Summary")

#headings
heading1 = Label(mainWindow, text = "Class Name:")
heading1.grid(column = 0, row = 0)
heading2 = Label(mainWindow, text = "# Scores Entered:")
heading2.grid(column = 0, row = 1)
heading3 = Label(mainWindow, text = "Current Average:")
heading3.grid(column = 0, row = 2)
heading4 = Label(mainWindow, text = "High Score:")
heading4.grid(column = 0, row = 3)
heading5 = Label(mainWindow, text = "Low Score:")
heading5.grid(column = 0, row = 4)

#calculation functions
def average(classSpot, list): #returns average
    adder = 0
    for i in range(len(list)):
        adder += list[i][classSpot]
    return adder/len(list)

def maxGrade(classSpot, list): #returns max from class spot in list
    holder = []
    for i in range(len(list)):
        holder.append(list[i][classSpot])
    return max(holder)

def minGrade(classSpot, list): #returns minimum from class spot in list
    holder = []
    for i in range(len(list)):
        holder.append(list[i][classSpot])
    return min(holder)

#programming display
programming1 = Label(mainWindow, text = "Programming")
programming1.grid(column = 1, row = 0)
programming2 = Label(mainWindow, text = str(len(grades)))
programming2.grid(column = 1, row = 1)
programming3 = Label(mainWindow, text = str(average(0,grades)))
programming3.grid(column = 1, row = 2)
programming4 = Label(mainWindow, text = str(maxGrade(0,grades)))
programming4.grid(column = 1, row = 3)
programming5 = Label(mainWindow, text = str(minGrade(0,grades)))
programming5.grid(column = 1, row = 4)

#art display
art1 = Label(mainWindow, text = "Art")
art1.grid(column = 1, row = 0)
art2 = Label(mainWindow, text = str(len(grades)))
art2.grid(column = 1, row = 1)
art3 = Label(mainWindow, text = str(average(1,grades)))
art3.grid(column = 1, row = 2)
art4 = Label(mainWindow, text = str(maxGrade(1,grades)))
art4.grid(column = 1, row = 3)
art5 = Label(mainWindow, text = str(minGrade(1,grades)))
art5.grid(column = 1, row = 4)