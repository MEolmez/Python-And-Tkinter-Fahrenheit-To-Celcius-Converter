from tkinter import *
 
window = Tk()
 
window.title("Fahrenheit To Celcius")
 
window.geometry('250x150')
 
lbl = Label(window, text="Enter Fahrenheit Value")
 
lbl.grid(column=0, row=1)

lbl2 = Label(window, text=" ")
lbl2.grid(column=0, row=2)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=1)

#spin = Spinbox(window, from_=1, to=10, width=5)

#spin.grid(column=0,row=2)



def clicked():
 
    
    Celsius=(int(txt.get()) - 32) * 5.0/9.0

    Celsius =round(Celsius,1)
    Celsius=str(Celsius)
 	
    lbl2.configure(text="Its "+Celsius+" degree celsius")
 

btn = Button(window, text="Calculate", command=clicked)

btn.grid(column=2, row=1)
 
window.mainloop()
