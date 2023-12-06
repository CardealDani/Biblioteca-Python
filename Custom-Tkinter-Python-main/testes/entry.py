from tkinter import *

def impDados():
    print(f"Nome: {vnome.get()}\nNúmero: {vnumero.get()}\nEmail: {vemail.get()}\nObs: {vobs.get('1.0',END)}")
    vnome.delete('0',END)
    vnumero.delete('0',END)
    vemail.delete('0',END)
    vobs.delete('1.0',END)
    


app = Tk()

app.title('Entry')
app.geometry('500x300')
app.configure(background="#dde")

Label(app,text='Nome',background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnome = Entry(app)
vnome.place(x=10,y=30,width=200,height=20)

Label(app,text='Número',background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vnumero = Entry(app)
vnumero.place(x=10,y=80,width=200,height=20)

Label(app,text='Email',background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vemail = Entry(app)
vemail.place(x=10,y=130,width=200,height=20)

Label(app,text='OBS',background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vobs = Text(app)
vobs.place(x=10,y=180,width=300,height=80)

Button(app,text="Pegar valores", command=impDados).place(x=10,y=270,width=100,height=20)

app.mainloop()