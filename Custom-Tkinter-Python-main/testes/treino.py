from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry('600x300')


lista=[
    ['Programação I','64'],
       ['Autoração Multimídia I','64'],
        ['História do Design','64'],
        ['Programação II','64'],
        ['Comunicação Visual I','64'],
        ['Projeto I','64'],
        ['Autoração Multimídia II','64'],
]


tv = ttk.Treeview(app,columns=('cadeira','hora'), show='headings')


tv.column('cadeira',minwidth=0,width=100)
tv.column('hora',minwidth=0,width=100)
tv.heading('cadeira',text='CADEIRA')
tv.heading('hora',text='HORA')

tv.pack()

for (c,h) in lista:
    tv.insert("","end",values=(c,h))
    
app.mainloop()