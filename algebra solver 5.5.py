from tkinter import *
import parser
from math import *


window = Tk()

canvas1 = Canvas(window, width = 400, height = 300, bg="teal")
canvas1.pack()

title = Label(window, text= "Algebra Solver", font=("fixedsys", 33), bg="teal", fg="cyan")
canvas1.create_window(200, 50, window=title)

sub = Label(window, text= "Version 5.5 by Bryce Patterson", font=("fixedsys", 10), bg="teal", fg="cyan", justify="center")
canvas1.create_window(200, 100, window=sub)

e = Entry (window, text="Algebra equation solver", font=("system", 20), bg="lavender", fg="midnightblue", justify="center") 
canvas1.create_window(200, 140, window=e)

def callback ():
    #print (e.get())
    string = e.get()
    if "x" not in string:
        ex = parser.expr(string)
        code5 = ex.compile("file.py")
        ex = eval(code5)
        answer = ex
        label1 = Label(window, text= answer, font=("fixedsys", 24), bg="teal")
        canvas1.create_window(200, 230, window=label1)
        
        
    if "x" in string:      
        data = string.split("=")
        left1 = data[0]
        right = data[1]
        new = left1 + "+" + "(-1*(" + right + "))=0"
        data = new.split("=")
        global left
        
        left = data[0]
        #print(left)
        cont = 1
        low=0
        du=1
        dj=1
        guess = 0
        u = guess
        j = guess
        iterations = 0
        while cont == 1:
            st1 = parser.expr(left)
            code1 = st1.compile("file.py")
            x=u
            high = eval(code1)
            if high<0 and low>0:
                if abs(low)<abs(high):
                    u = j
                    j = j
                    du = du/10
                    dj = dj/10
                if abs(high)<abs(low):
                    u = u
                    j = u
                    du = du/10
                    dj = dj/10
            if high>0 and low<0:
                if abs(low)<abs(high):
                    u = j
                    j = j
                    du = du/10
                    dj = dj/10
                if abs(high)<abs(low):
                    u = u
                    j = u
                    du = du/10
                    dj = dj/10
            
            st2 = parser.expr(left)
            code2 = st2.compile("file.py")
            x=j
            low = eval(code2)
            if high<0 and low>0:
                if abs(low)<abs(high):
                    u = j
                    j = j
                    du = du/10
                    dj = dj/10
                if abs(high)<abs(low):
                    u = u
                    j = u
                    du = du/10
                    dj = dj/10
            if high>0 and low<0:
                if abs(low)<abs(high):
                    u = j
                    j = j
                    du = du/10
                    dj = dj/10
                if abs(high)<abs(low):
                    u = u
                    j = u
                    du = du/10
                    dj = dj/10
            #print("low: ", low)
            #print("high: ", high)
            #print(u, j)
            if abs(low)<.0000001:
                answer = round(j, 4)
                print("X =", answer)
                answer = str(answer)
                answer = "x = " + answer
                title = Label(window, text= "Algebra Solver", font=("fixedsys", 30), bg="teal", fg="teal")
                canvas1.create_window(200, 230, window=title)
                label1 = Label(window, text= answer, font=("fixedsys", 24), bg="teal")
                canvas1.create_window(200, 230, window=label1)
                cont = 0
                break
            if abs(high)<.0000001:
                answer = round(u, 4)
                print("X =", answer)
                answer = str(answer)
                answer = "x = " + answer
                title = Label(window, text= "Algebra Solver", font=("fixedsys", 30), bg="teal", fg="teal")
                canvas1.create_window(200, 230, window=title)
                label1 = Label(window, text= answer, font=("fixedsys", 24), bg="teal")
                canvas1.create_window(200, 230, window=label1)
                cont = 0
                break
            
            u = u+du
            j = j-dj

            iterations+=1
            if iterations>100000:
                itera = Label(window, text= "Error \n max iterations or no sign change. ", font=("fixedsys", 15), bg="teal")
                canvas1.create_window(200, 230, window=itera)
                break
                

button1 = Button(text='Calculate', command=callback, bg="maroon", fg="gainsboro")
canvas1.create_window(200, 180, window=button1)

mainloop()
