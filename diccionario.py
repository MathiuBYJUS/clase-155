from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("diccionario")
root.config(bg="blue")

significados={'Mutable':'Que se pueden cambiar',
              'Inmutable':'Que no se puede cambiar',
              'Tkinter':'Una libreria de programacion'}

def mutable() :
    label_1["text"]= significados['Mutable']

def inmutable() :
    label_2["text"]= significados['Inmutable']
    
def tkinter() :
    label_3["text"]=significados['Tkinter']
    


label_1=Label(root ,text="c")
label_1.place(relx=0.5 , rely=0.8 , anchor=CENTER)
button_1=Button( root ,text="Significado de mutbale", command=mutable)
button_1.place(relx=0.5 , rely=0.7 , anchor=CENTER)



label_2=Label(root , text="b")
label_2.place(relx=0.5 , rely=0.6 , anchor=CENTER)
button_2=Button(root, text="siginificado de inmutable",command=inmutable)
button_2.place(relx=0.5 , rely=0.5 , anchor=CENTER)



label_3=Label(root , text="a")
label_3.place(relx=0.5 , rely=0.4 , anchor=CENTER)
button_3=Button(root , text="Significado de Tkinter",command=tkinter)
button_3.place(relx=0.5 , rely=0.3 , anchor=CENTER)



label_4=Label(root , text="Diccionario de metodologia en programacion")
label_4.place(relx=0.5 , rely=0.2 , anchor=CENTER)
root.mainloop()

