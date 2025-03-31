from tkinter import *


root = Tk()
root.geometry("500x500")

# b1 = Button(text="Add").pack(side=LEFT)
# b2 = Button(text="Sub").pack(side=RIGHT)
# b3 = Button(text="Mul").pack(side=TOP)
# b4 = Button(text="Div").pack(side=BOTTOM)


# l1 = Label(text="Username").grid(row=1,column=1)
# l2 = Label(text="Email").grid(row=2,column=1)
# l3 = Label(text="Password").grid(row=3,column=1)

# e1 = Entry()
# e1.grid(row=1,column=2)
# e2 = Entry()
# e2.grid(row=2,column=2)
# e3 = Entry()
# e3.grid(row=3,column=2)

# Button(text="submit").grid(row=4,column=2)



l1 = Label(text="Username").place(x=100,y=100)
l2 = Label(text="Email").place(x=100,y=150)
l3 = Label(text="Password").place(x=100,y=200)

e1 = Entry()
e1.place(x=200,y=100)
e2 = Entry()
e2.place(x=200,y=150)
e3 = Entry()
e3.place(x=200,y=200)

Button(text="submit",width=15).place(x=200,y=250)

root.mainloop()

