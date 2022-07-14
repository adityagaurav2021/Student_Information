from tkinter import *
root = Tk()
def Successfully():
    print("Completed")


root.geometry("955x556")
root.title("Shri Tara Computer Academy")
Label(root,text="Student Information Form",font="comicsansms 18 bold").grid(row=0,column=3)
name = Label(root,text="Name").grid(row=1,column=2)
Gender = Label(root,text="Gender").grid(row=2,column=2)
Father = Label(root,text="Father's Name").grid(row=3,column=2)
Mother = Label(root,text=" Mother's Name").grid(row=4,column=2)
birth = Label(root,text="DOB").grid(row=5,column=2)
Contact = Label(root,text="Contact NO").grid(row=6,column=2)
Address = Label(root,text="Address").grid(row=7,column=2)
payment = Label(root,text="Payment Mode").grid(row=8,column=2)

namevalue = StringVar()
Gendervalue = StringVar()
Fathervalue = StringVar()
Mothervalue = StringVar()
birthvalue = StringVar()
Contactvalue = StringVar()
Addressvalue = StringVar()
paymentvalue = StringVar()
Delaration=IntVar

nameentry = Entry(root, textvariable=namevalue)
Genderentry = Entry(root, textvariable=Gendervalue)
Fatherentry = Entry(root, textvariable=Fathervalue)
Motherentry = Entry(root, textvariable=Mothervalue)
birthentry = Entry(root, textvariable=birthvalue)
Contactentry = Entry(root, textvariable=Contactvalue)
Addressentry = Entry(root, textvariable=Addressvalue)
paymententry = Entry(root, textvariable=paymentvalue)

nameentry.grid(row=1, column=3)
Genderentry.grid(row=2, column=3)
Fatherentry.grid(row=3, column=3)
Motherentry.grid(row=4, column=3)
birthentry.grid(row=5, column=3)
Contactentry.grid(row=6, column=3)
Addressentry.grid(row=7, column=3)
paymententry.grid(row=8,  column=3)

Declaration = Checkbutton(text='''I Hereby declar that the information given in this application is true and correct to the best of my knowledge
and belie.In case any information given in this application proves to false or incorrect,I Shall be responsible for the consequences''')
Declaration.grid(row=9,column=3)

Button(text="Submit", command=Successfully).grid(row=10, column=3)
root.mainloop()