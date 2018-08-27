from Tkinter import *

root = Tk()

def printName():
	print("hey, i m a function")

# label1= Label(root, text="Name")
# label2= Label(root, text="Password")
# #label1.pack()
# #label2.pack()

# entry1 = Entry(root)
# entry2 = Entry(root)

# label1.grid(row=0,sticky=E)
# label2.grid(row=1,sticky=E)

# entry1.grid(row=0,column=1)
# entry2.grid(row=1,column=1)

c= Checkbutton(root,text="keep me logied in")
c.grid(columnspan=2)

# topFrame = Frame(root)
# #topFrame.pack()
# bottomFrame= Frame(root)
# #bottomFrame.pack(side=BOTTOM)

# button1= Button(topFrame,text="button1",fg="red");
# button2= Button(bottomFrame,text="button2",fg="blue")


#button3.pack() cannot use as it is managed by grid
# button1.pack()
# button2.pack(side=BOTTOM)
button3= Button(root,text="print function",command=printName)
#button3.pack()
root.mainloop()
