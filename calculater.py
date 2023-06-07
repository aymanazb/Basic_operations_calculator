from tkinter import*

expression=""
def p (userinput):
    global expression
    #الهدف من هذا السطر هو قبول اكثر من عنصر واحد او رتبة واحدة
    expression=expression+str(userinput)
    eq.set(expression)
def equalpress():
    try :
        global expression
    #eval fonction pour donner la resulta d'un opiration + _ / *
        result= str(eval(expression))
        eq.set(result)  
    #حتى بعد كل مرة بعد تساوي يعود الى البداية
        expression="" 
    except:
        eq.set("error")
        expression=""
def clear():
    global expression 
    expression=""
    eq.set("")       
root=Tk()
root.geometry("280x250")
root.title("calculator")

label = Label(text="calculator", font="italic 20",bg="red")
label.grid(row=0, columnspan=4, pady= 10)
eq=StringVar()
input=Entry(root, textvariabl= eq)
input.grid(row=1, columnspan=4, padx=5, pady=10, ipadx=70)
button7= Button(root, text="7", command=lambda: p(7), height=1, width=7)
button7.grid(row=2, column=0)
button8= Button(root, text="8" ,command=lambda: p(8), height=1, width=7)
button8.grid(row=2, column=1)
button9= Button(root, text="9" ,command=lambda: p(9), height=1, width=7)
button9.grid(row=2, column=2)
button4= Button(root, text="4" ,command=lambda: p(4), height=1, width=7)
button4.grid(row=3, column=0)
button5= Button(root, text="5" ,command=lambda: p(5), height=1, width=7)
button5.grid(row=3, column=1)
button6= Button(root, text="6" ,command=lambda: p(6), height=1, width=7)
button6.grid(row=3, column=2)
button1= Button(root, text="1" ,command=lambda: p(1), height=1, width=7)
button1.grid(row=4, column=0)
button2= Button(root, text="2" ,command=lambda: p(2), height=1, width=7)
button2.grid(row=4, column=1)
button3= Button(root, text="3" ,command=lambda: p(3), height=1, width=7)
button3.grid(row=4, column=2)
button0= Button(root, text="0" ,command=lambda: p(0), height=1, width=7)
button0.grid(row=5, column=0)
buttonDOT= Button(root, text="." ,command=lambda: p("."), height=1, width=7)
buttonDOT.grid(row=5, column=1)
buttonEQUAL= Button(root, text="=" ,command=equalpress, height=1, width=7, bg="blue", fg="white")
buttonEQUAL.grid(row=5, column=2)
buttonX= Button(root, text="*" ,command=lambda: p("*"), height=1, width=7)
buttonX.grid(row=2, column=3)
buttonDIV= Button(root, text="/" ,command=lambda: p("/"), height=1, width=7)
buttonDIV.grid(row=3, column=3)
buttonSUST= Button(root, text="_" ,command=lambda: p("-"), height=1, width=7)
buttonSUST.grid(row=4, column=3)
buttonADD= Button(root, text="+" ,command=lambda: p("+"), height=1, width=7)
buttonADD.grid(row=5, column=3)
buttonC= Button(root, text="C" ,command=clear, height=1, width=7)
buttonC.grid(row=6, column=0)


root.mainloop()
