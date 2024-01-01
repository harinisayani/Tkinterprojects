from tkinter import *
window=Tk(className="Calculator")
window.geometry("275x347")
x=" "
def clicked(item):
    global x
    x=x+str(item)
    v.set(x)
def remove():
    global a
    global x
    v.set(" ")
    x=" "
    a=" "
def result():
    global x
    v.set(" ")
    a=eval(x)
    v.set(a)
Entryframe=Frame(window,width=275,height=85,bg="gray")
Entryframe.pack(side=TOP)
Buttonframe=Frame(window,width=275,height=250,bg="white")
Buttonframe.pack()
v=StringVar()
textfield=Entry(Entryframe,width=24,font=("arial",14,"bold"),bg="lightyellow",justify=RIGHT,textvariable=v)
textfield.grid(row=0,column=0,ipady=20)
one=Button(Buttonframe,text="1",width=8,height=3,bg="lightblue",command=lambda:clicked(1),cursor="hand2").grid(row=3,column=0,padx=0,pady=0)
two=Button(Buttonframe,text="2",width=8,height=3,bg="lightblue",command=lambda:clicked(2),cursor="hand2").grid(row=3,column=1,padx=0,pady=0)
three=Button(Buttonframe,text="3",width=8,height=3,bg="lightblue",command=lambda:clicked(3),cursor="hand2").grid(row=3,column=2,padx=0,pady=0)
four=Button(Buttonframe,text="4",width=8,height=3,bg="lightblue",command=lambda:clicked(4),cursor="hand2").grid(row=2,column=0,padx=0,pady=0)
five=Button(Buttonframe,text="5",width=8,height=3,bg="lightblue",command=lambda:clicked(5),cursor="hand2").grid(row=2,column=1,padx=0,pady=0)
six=Button(Buttonframe,text="6",width=8,height=3,bg="lightblue",command=lambda:clicked(6),cursor="hand2").grid(row=2,column=2,padx=0,pady=0)
seven=Button(Buttonframe,text="7",width=8,height=3,bg="lightblue",command=lambda:clicked(7),cursor="hand2").grid(row=1,column=0,padx=0,pady=0)
eight=Button(Buttonframe,text="8",width=8,height=3,bg="lightblue",command=lambda:clicked(8),cursor="hand2").grid(row=1,column=1,padx=0,pady=0)
nine=Button(Buttonframe,text="9",width=8,height=3,bg="lightblue",command=lambda:clicked(9),cursor="hand2").grid(row=1,column=2,padx=0,pady=0)
add=Button(Buttonframe,text="+",width=8,height=3,bg="lightpink",command=lambda:clicked("+"),cursor="hand2").grid(row=2,column=3,padx=0,pady=0)
sub=Button(Buttonframe,text="-",width=8,height=3,bg="lightpink",command=lambda:clicked("-"),cursor="hand2").grid(row=1,column=3,padx=0,pady=0)
div=Button(Buttonframe,text="/",width=8,height=3,bg="lightpink",command=lambda:clicked("/"),cursor="hand2").grid(row=0,column=2,padx=0,pady=0)
mod=Button(Buttonframe,text="%",width=8,height=3,bg="lightpink",command=lambda:clicked("%"),cursor="hand2").grid(row=3,column=3,padx=0,pady=0)
mul=Button(Buttonframe,text="*",width=8,height=3,bg="lightpink",command=lambda:clicked("*"),cursor="hand2").grid(row=0,column=3,padx=0,pady=0)
equal=Button(Buttonframe,text="=",width=18,height=3,bg="lightgray",command=lambda:result(),cursor="hand2").grid(row=4,column=2,padx=0,pady=0,columnspan=2)
clear=Button(Buttonframe,text="C",width=18,height=3,bg="lightgray",command=lambda:remove(),cursor="hand2").grid(row=0,column=0,padx=0,pady=0,columnspan=2)
zero=Button(Buttonframe,text="0",width=8,height=3,bg="lightblue",command=lambda:clicked(0),cursor="hand2").grid(row=4,column=0,padx=0,pady=0)
dot=Button(Buttonframe,text=".",width=8,height=3,bg="lightblue",command=lambda:clicked("."),cursor="hand2").grid(row=4,column=1,padx=0,pady=0)
window.mainloop()