# importing requirements

from tkinter import *
from datetime import date 

# creating the window

window = Tk()
window.geometry('550x400')
window.resizable(0,0)
window.title('Age Calc')

def calc_age():
    today = date.today()
    birthdate = date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))

    age = today.year - birthdate.year - ((today.month,today.day) < (birthdate.month,birthdate.day))
    Label(text=f'{nameValue.get()} your age is {age}',font=(12)).grid(row=6,column=1)

# labels

Label(text='Name',font=(10)).grid(row=1,padx=80,pady=20)
Label(text='Year',font=(10)).grid(row=2,padx=80,pady=20)
Label(text='Month',font=(10)).grid(row=3,padx=80,pady=20)
Label(text='Day',font=(10)).grid(row=4,padx=80,pady=20)

# initializing the variables

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(window,textvariable=nameValue,font=(10))
yearEntry = Entry(window,textvariable=yearValue,font=(10))
monthEntry = Entry(window,textvariable=monthValue,font=(10))
dayEntry = Entry(window,textvariable=dayValue,font=(10))

nameEntry.grid(row=1,column=1,pady=20)
yearEntry.grid(row=2,column=1,pady=20)
monthEntry.grid(row=3,column=1,pady=20)
dayEntry.grid(row=4,column=1,pady=20)

# button

Button(text='Calculate Age',command=calc_age,font=(17)).grid(row=5,column=1,pady=20)

# run
window.mainloop()