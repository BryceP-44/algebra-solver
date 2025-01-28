from tkinter import *
import ast
from math import *
#
def al():
    

    #def start():
    window = Tk()

    canvas1 = Canvas(window, width = 400, height = 300, bg="teal")
    canvas1.pack()

    title = Label(window, text= "Algebra Solver", font=("fixedsys", 33), bg="teal", fg="cyan")
    canvas1.create_window(200, 50, window=title)

    sub = Label(window, text= "Version 6.75 by Bryce Patterson", font=("fixedsys", 10), bg="teal", fg="cyan", justify="center")
    canvas1.create_window(200, 100, window=sub)

    e = Entry (window, text="Algebra equation solver", font=("system", 20), bg="lavender", fg="midnightblue", justify="center") 
    canvas1.create_window(200, 140, window=e)



    def callback ():
        #print (e.get())
        string = e.get()
        #string="x**2=x+2"
        if "x" not in string:
            code = ast.parse(string,mode='eval')
            answer = eval(compile(code,'',mode='eval'))
            
            title = Label(window, text= "blah____________", font=("fixedsys", 30), bg="teal", fg="teal")
            canvas1.create_window(200, 230, window=title)
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
            du=10
            dj=10
            guess = 2
            u = guess
            j = guess
            iterations = 0
            while cont == 1:
                st1 = ast.parse(left,mode='eval')
                x=u
                high = eval(compile(st1,'',mode='eval'))
                
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
                
                st2 = ast.parse(left,mode='eval')
                x=j
                low = eval(compile(st2,'',mode='eval'))

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
                #print(u,"     ", j)
                #print(" ")
                if abs(low)<.00000001:
                    answer = round(j, 10)
                    print("X =", answer)
                    answer = str(answer)
                    answer = "X = " + answer
                    title = Label(window, text= "blah____________", font=("fixedsys", 30), bg="teal", fg="teal")
                    canvas1.create_window(200, 230, window=title)
                    label1 = Label(window, text= answer, font=("fixedsys", 24), bg="teal")
                    canvas1.create_window(200, 230, window=label1)
                    cont = 0
                    break
                if abs(high)<.00000001:
                    answer = round(u, 10)
                    print("X =", answer)
                    answer = str(answer)
                    answer = "X = " + answer
                    title = Label(window, text= "blah____________", font=("fixedsys", 30), bg="teal", fg="teal")
                    canvas1.create_window(200, 230, window=title)
                    label1 = Label(window, text= answer, font=("fixedsys", 24), bg="teal")
                    canvas1.create_window(200, 230, window=label1)
                    cont = 0
                    break
                
                u = u+du
                j = j-dj
                -1*((7-(50)**(.5)))**(1/3)
                #((7+(50)**(.5))**(1/3)) + (-1*((7-(50)**(.5))))**(1/3))

                iterations+=1
                if iterations>100000:
                    itera = Label(window, text= "        Going into imaginary      ", font=("fixedsys", 15), bg="teal")
                    canvas1.create_window(200, 230, window=itera)
                    print("going into imaginary")
                    #so what i did here was swtich into imaginary coordinates and x-y coordinates. the answer of a complex number is giver as a + bi so basically that a is the x-y coordinate
                    #however, since we rotated the pov the x axis is invisible. so the a value is basicaly just the y value of this new coordinate system
                    #even if the garph does not have any solutions or roots in the real world, it has some in the imaginary world`
                    #the point where this a or the y value goes to 0 is obviously the root
                    #so the new independent variable axis is the bi axis. the i acts as a unit vector kind of.
                    #so I now replaced the old x value with a negative square root of x which is basically x**.5 i
                    #so i can now just do my solver with the same old funciton but with a substituted x
                    #however, the final answer needs to be square root and multiplied by i
                    #this is because the solution of x**2 + 8 = 0 is not x = 8 it is actually 8**.5 i
                    #i just put the i as a j in the answer because idk thats how python does it and also its easier to see
                    
                    new = left.replace("x","((-x)**.5)")
                    
                    data = new.split("=")
                    #global left

                    left = data[0]
                    cont = 1
                    low=0
                    du=10
                    dj=10
                    guess = 2
                    u = guess
                    j = guess
                    iterations = 0
                    
                    while cont == 1:
                        """st1 = ast.parse(left,mode='eval')
                        x=u
                        high = eval(compile(st1,'',mode='eval'))
                        
                        st1 = parser.expr(left)
                        code1 = st1.compile("file.py")"""

                        st1 = ast.parse(left,mode='eval')
                        x=u
                        high = str(eval(compile(st1,'',mode='eval')))
                        
                        """x=u
                        high = eval(code1)
                        high = str(high)"""
                        #print(high)
                        
                        go = 1

                        if "+" in high:
                            high = str(high)
                            high = high.split("+")
                            high = high[0]
                            high = str(high)
                            high = high.split("(")
                            high = high[1]
                            high = str(high)
                            go = 0

                        if "+" not in high:
                            if "-" not in high:
                                go = 0
                         
                        if "+" not in high:
                            if go == 1:
                                yup = high.split("-")
                                first = str(yup[0])
                                second = str(yup[1])
                                if first =="(":
                                    if "+" in high:
                                        high = second.split("+")
                                        high = str(high[0])
                                        high = "-"+high
                                    else:
                                        high = second.split("-")
                                        high = str(high[0])
                                        high = "-"+high
                                
                                if "e" in first and "j" in second:
                                    low=0
                                    go=0
                                else:
                                    if go==1:
                                        high = str(high)
                                        high = high.split("-")
                                        high = high[0]
                                        high = str(high)
                                        high = high.split("(")
                                        high = high[1]
                                        high = str(high)
                        #print(high)
                        high=float(high)     
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
                        
                        """st2 = parser.expr(left)
                        code2 = st2.compile("file.py")
                        x=j
                        low = eval(code2)                        
                        low=str(low)"""

                        st2 = ast.parse(left,mode='eval')
                        x=j
                        low = str(eval(compile(st1,'',mode='eval')))
                        
                        go = 1
                        if "+" in low:
                            low = str(low)
                            low = low.split("+")
                            low = low[0]
                            low = str(low)
                            low = low.split("(")
                            low = low[1]
                            low = str(low)
                            go = 0

                        if "+" not in low:
                            if "-" not in low:
                                go = 0
                         
                        if "+" not in low:
                            if go == 1:
                                yup = low.split("-")
                                first = str(yup[0])
                                second = str(yup[1])
                                if first =="(":
                                    if "+" in low:
                                        low = second.split("+")
                                        low = str(low[0])
                                        low = "-"+low
                                    else:
                                        low = second.split("-")
                                        low = str(low[0])
                                        low = "-"+low

                                if "e" in first and "j" in second:
                                    low = 0
                                    go = 0
                                else:
                                    if go == 1:
                                        low = str(low)
                                        low = low.split("-")
                                        low = low[0]
                                        low = str(low)
                                        low = low.split("(")
                                        low = low[1]
                                        low = str(low)
                                        #x**2+12253=0
                        #print(low)
                        low=float(low)
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
                        if abs(low)<.00000001:
                            answer = round(j, 4)
                            answer = answer **.5
                            answer = str(answer)
                            answer = "X = " + answer + "  j"
                            print(answer)
                            title = Label(window, text= "blah____________", font=("fixedsys", 30), bg="teal", fg="teal")
                            canvas1.create_window(200, 230, window=title)
                            label1 = Label(window, text= answer, font=("fixedsys", 16), bg="teal")
                            canvas1.create_window(200, 230, window=label1)
                            cont = 0 
                            break
                        
                        if abs(high)<.00000001:
                            answer = round(u, 4)
                            answer = answer **.5
                            answer = str(answer)
                            answer = "X = " + answer + "  j"
                            print(answer)
                            title = Label(window, text= "blah____________", font=("fixedsys", 30), bg="teal", fg="teal")
                            canvas1.create_window(200, 230, window=title)
                            label1 = Label(window, text= answer, font=("fixedsys", 16), bg="teal")
                            canvas1.create_window(200, 230, window=label1)
                            cont = 0  
                            break
                        
                        u = u+du
                        j = j-dj


                        iterations+=1
                        if iterations>100000:
                            print("Error \n max iterations. ")
                            break
                    break
                    


    button1 = Button(text='Calculate', command=callback, bg="maroon", fg="gainsboro")
    canvas1.create_window(200, 180, window=button1)
    mainloop()

al()
#sin(x)=.9
