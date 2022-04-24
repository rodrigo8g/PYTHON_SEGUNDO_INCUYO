#IMPORTACION LIBRERIAS
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#CREACION VENTANA
ventana=Tk()
ventana.title("LISTASNOVIOS.COM: ARMA TU LISTA DE CASAMIENTO ONLINE")
ventana.state("zoomed")
ventana.config(bg="snow")

#CONEXION BASE DE DATOS
conexion=sqlite3.connect("BASE/listasnovios.db")

#FRAME logo
frameLogo = Frame(ventana,bg="lightblue3",height=120)
frameLogo.pack(side=TOP,fill=X)
img = PhotoImage(file="imagenes/banner_superior.png")
lbl_img = Label(frameLogo, image=img)
lbl_img.pack()

#FRAME SUPERIOR(TÍTULO Y BUSCADOR)
frameSuperior = Frame(ventana,bg="lightblue4",height=120)
frameSuperior.pack(side=TOP,fill=X)
logoCentral=PhotoImage(file="imagenes/banner_superior.png")
datosCasamiento = Label(frameSuperior,text="Apellido Cónyuge 1:",font=("Rockwell", 15,"bold"),fg="snow",bg="lightblue4")
datosCasamiento.pack(side=LEFT,pady=(4,10),ipadx=1)
#Buscar
#1.-Dato a buscar;
#2.-Cursor;
#3.-execute
#4.-fetchall;
#5.-close

def buscador():
    buscarCasamiento= (entryCasamiento.get(),)
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM CASAMIENTO WHERE APELLIDO_CONYUGE=?", buscarCasamiento)
    casamientoBuscado= tabla.fetchall()
    tabla.close
    idCasamientoEntry.delete(0,END)
    nombreEntry.delete (0,END)
    apellidoEntry.delete (0,END)
    nombre2Entry.delete (0,END)
    apellido2Entry.delete (0,END)
    paisEntry.delete (0,END)
    provinciaEntry.delete (0,END)
    fechaDeCasamientoEntry.delete (0,END)
    salonDeEventosEntry.delete (0,END)
    aliasCbuEntry.delete (0,END)
    for fila in casamientoBuscado:
        idCasamientoEntry.insert(END,fila[0])
        nombreEntry.insert (END, fila[1])
        apellidoEntry.insert (END, fila[2])
        nombre2Entry.insert (END, fila[3])
        apellido2Entry.insert (END, fila[4])
        paisEntry.insert (END, fila[5])
        provinciaEntry.insert (END, fila[6])
        fechaDeCasamientoEntry.insert (END, fila[7])
        salonDeEventosEntry.insert (END, fila[8])
        aliasCbuEntry.insert (END,fila[9])
#        casamientoBuscado.forget(0,END)
botonEntryCasamiento=Button(frameSuperior,command=buscador,text="Buscar",font=("Rockwell",15,"bold"),fg="snow",bg="lightblue4",relief="flat")
botonEntryCasamiento.pack(side=RIGHT)
entryCasamiento=Entry(frameSuperior,text="BuscarCasamiento", font=("Calibri", 20,"bold"),fg="black",bg="snow")
entryCasamiento.pack(fill=X,pady=(4,4))

#FRAME LATERAL IZQUIERDO
frameIzquierdo=Frame(ventana,bg="lightblue3")
frameIzquierdo.pack(side=LEFT,fill=Y,ipadx=27)

def guardar():
    if(nombreEntry.get() != "" and apellidoEntry.get() != "" and nombre2Entry.get() != "" and apellido2Entry.get() != "" and paisEntry.get() != "" and provinciaEntry.get()!= "" and fechaDeCasamientoEntry.get()!="" and salonDeEventosEntry.get()!="" and aliasCbuEntry.get()!=""):
        tabla=conexion.cursor()
        casamientoGuardar = (nombreEntry.get(),apellidoEntry.get(),nombre2Entry.get(),apellido2Entry.get(),paisEntry.get(),provinciaEntry.get(),fechaDeCasamientoEntry.get(),salonDeEventosEntry.get(),aliasCbuEntry.get())
        tabla.execute("INSERT INTO CASAMIENTO(NOMBRE_CONYUGE,APELLIDO_CONYUGE,NOMBRE_CONYUGE_2,APELLIDO_CONYUGE_2,PAIS,PROVINCIA,FECHA_CASAMIENTO,SALON_EVENTOS,ALIAS_CBU) VALUES(?,?,?,?,?,?,?,?,?)",casamientoGuardar)
        conexion.commit()
        tabla.close
        messagebox.showinfo("listasnovios.com","Guardado Exitoso")
        idCasamientoEntry.delete(0,END)
        nombreEntry.delete (0,END)
        apellidoEntry.delete (0,END)
        nombre2Entry.delete (0,END)
        apellido2Entry.delete (0,END)
        paisEntry.delete (0,END)
        provinciaEntry.delete (0,END)
        fechaDeCasamientoEntry.delete (0,END)
        salonDeEventosEntry.delete (0,END)
        aliasCbuEntry.delete (0,END)
    else:
        messagebox.showwarning ("listasnovios.com", "Falta completar datos")
imagenGuardar=PhotoImage(file="imagenes/guardar.png")
botonGuardar = Button(frameIzquierdo,command=guardar,text="Guardar",image=imagenGuardar,compound="top",font=("Rockwell",15),bg="lightblue3",fg="snow",relief="flat")
botonGuardar.pack(fill=X,ipady=10,ipadx=30)

def modificar():
    if(nombreEntry.get() != "" and apellidoEntry.get() != "" and nombre2Entry.get() != "" and apellido2Entry.get() != "" and paisEntry.get() != "" and provinciaEntry.get()!= "" and fechaDeCasamientoEntry.get()!="" and salonDeEventosEntry.get()!="" and aliasCbuEntry.get()!=""):
        tabla=conexion.cursor()
        datosModificar=((nombreEntry.get(),apellidoEntry.get(),nombre2Entry.get(),apellido2Entry.get(),paisEntry.get(),provinciaEntry.get(),fechaDeCasamientoEntry.get(),salonDeEventosEntry.get(),aliasCbuEntry.get(),idCasamientoEntry.get(),))
        tabla.execute("UPDATE CASAMIENTO SET NOMBRE_CONYUGE=?,APELLIDO_CONYUGE=?,NOMBRE_CONYUGE_2=?,APELLIDO_CONYUGE_2=?,PAIS=?,PROVINCIA=?,FECHA_CASAMIENTO=?,SALON_EVENTOS=?, ALIAS_CBU=? WHERE ID_Casamiento=?",datosModificar)
        conexion.commit()
        tabla.close
        messagebox.showinfo("listasnovios.com","Dato Modificado")
        idCasamientoEntry.delete(0,END)
        nombreEntry.delete (0,END)
        apellidoEntry.delete (0,END)
        nombre2Entry.delete (0,END)
        apellido2Entry.delete (0,END)
        paisEntry.delete (0,END)
        provinciaEntry.delete (0,END)
        fechaDeCasamientoEntry.delete (0,END)
        salonDeEventosEntry.delete (0,END)
        aliasCbuEntry.delete (0,END)
    else:
        messagebox.showwarning("ListasNovios.Com","Faltan completar datos")
imagenModificar=PhotoImage(file="imagenes/editar.png")
botonModificar = Button(frameIzquierdo,command=modificar,text="Editar",image=imagenModificar,compound="top",font=("Rockwell",15),bg="lightblue3",fg="snow",relief="flat")
botonModificar.pack(fill=X,ipady=10,ipadx=30)

def eliminar():
    if(idCasamientoEntry.get() != ""):
        tabla=conexion.cursor()
        datosEliminar=(idCasamientoEntry.get(),)
        tabla.execute("DELETE FROM CASAMIENTO WHERE ID_Casamiento=?",datosEliminar)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("ListasNovios.Com","Eliminado")
        idCasamientoEntry.delete(0,END)
        nombreEntry.delete (0,END)
        apellidoEntry.delete (0,END)
        nombre2Entry.delete (0,END)
        apellido2Entry.delete (0,END)
        paisEntry.delete (0,END)
        provinciaEntry.delete (0,END)
        fechaDeCasamientoEntry.delete (0,END)
        salonDeEventosEntry.delete (0,END)
        aliasCbuEntryEntry.delete (0,END)
    else:
        messagebox.showwarning("ListasNovios.com","Primero debe Buscar")
imagenEliminar=PhotoImage(file="imagenes/borrar.png")
botonEliminar = Button(frameIzquierdo,command=eliminar,text="Borrar",image=imagenEliminar,compound="top",font=("Rockwell",15),bg="lightblue3",fg="snow",relief="flat")
botonEliminar.pack(fill=X,ipady=10,ipadx=30)

def irListar():
    tabla=conexion.cursor()
    tabla.execute("SELECT * FROM CASAMIENTO ORDER BY ID_Casamiento")
    conexion.commit()
    datos = tabla.fetchall()
    tabla.close
    for dato in datos:
        listado= str(dato[0]) + " "+ str(dato[1])+ " "+ str(dato[2])+ " y "+ str(dato[3])+ " "+ str(dato[4])+ "; País: "+ str(dato[5])+ "; Provincia: "+ str(dato[6])+ "; Fecha: "+ str(dato[7])+ "; Salón: "+ str(dato[8])+ "; Alias/CBU: " + str(dato[9])
        lista.insert (END,listado)
# no puedo limpiar el listbox        listado.clear(0,END)    
imagenListar=PhotoImage(file="imagenes/listar.png")
lista= Listbox(ventana,width =60, height=13,font=("Rockwell",12),bg="lightblue4",fg="snow")
lista.pack(side=BOTTOM,fill=BOTH, ipady=20, ipadx=30)
botonListar = Button(frameIzquierdo,command=irListar,text="Listar",image=imagenListar,compound="top",font=("Rockwell",15),bg="lightblue3",fg="snow",relief="flat")
botonListar.pack(fill=X,ipady=12,ipadx=30)
listasCasamientos=Label(text="Listas de Casamiento:",fg="white",bg="lightblue4",font=("Rockwell",15, "bold"),width =20)
listasCasamientos.pack(side=BOTTOM,fill=X,padx=1)

def salir():
    salir = messagebox.askquestion("ListasNovios.com","Seguro que desea salir del programa?")
    if(salir == "yes"):
        ventana.destroy()
imagenSalir=PhotoImage(file="imagenes/salir.png")
botonSalir = Button(frameIzquierdo,command=salir,text="Salir",image=imagenSalir,compound="top",font=("Rockwell",15),bg="lightblue3",fg="snow",relief="flat")
botonSalir.pack(side=BOTTOM,fill=X,ipady=10,ipadx=30)

#FRAME CENTRAL LABELS 1

frameCentral= Frame(ventana,bg="snow",width =30, height=15)
frameCentral.pack(side=LEFT,fill=BOTH)

#LABELS DATOS1

idCasamiento=Label(frameCentral,text="Id",bg="snow",font=("Rockwell",15),width =20)
idCasamiento.pack(side=TOP,pady=9)
nombre= Label(frameCentral,text="Nombre Cónyuge 1:",bg="snow",font=("Rockwell",15),width =20)
nombre.pack(side=TOP,pady=9)
apellido= Label(frameCentral,text="Apellido Cónyuge 1:",bg="snow",font=("Rockwell",15),width =20)
apellido.pack(side=TOP,pady=9)
nombre2= Label(frameCentral,text="Nombre Cónyuge 2:",bg="snow",font=("Rockwell",15),width =20)
nombre2.pack(side=TOP,pady=9)
apellido2= Label(frameCentral,text="Apellido Cónyuge 2:",bg="snow",font=("Rockwell",15),width =20)
apellido2.pack(side=TOP,pady=9)

#FRAME CENTRAL ENTRYS 1
frameCentral1= Frame(ventana,bg="snow",width =30, height=15)
frameCentral1.pack(side=LEFT,fill=BOTH)

#ENTRYS DATOS 1

idCasamientoEntry= Entry(frameCentral1,font=("Rockwell",15),width =25)
idCasamientoEntry.pack(side=TOP,pady=10)
nombreEntry= Entry(frameCentral1,font=("Rockwell",15),width =25)
nombreEntry.pack(side=TOP,pady=10)
apellidoEntry= Entry(frameCentral1,font=("Rockwell",15),width =25)
apellidoEntry.pack(side=TOP,pady=10)
nombre2Entry= Entry(frameCentral1,font=("Rockwell",15),width =25)
nombre2Entry.pack(side=TOP,pady=10)
apellido2Entry= Entry(frameCentral1,font=("Rockwell",15),width =25)
apellido2Entry.pack(side=TOP,pady=10)

#FRAME CENTRAL LABELS 2

frameCentral2= Frame(ventana,bg="snow",width =30, height=15)
frameCentral2.pack(side=LEFT,fill=BOTH)

#LABELS DATOS 2

pais= Label(frameCentral2,text="País Evento:",bg="snow",font=("Rockwell",15),width =25)
pais.pack(side=TOP,pady=9)
provincia= Label(frameCentral2,text="Provincia/Región Evento:",bg="snow",font=("Rockwell",15),width =20)
provincia.pack(side=TOP,pady=9)
fechaDeCasamiento= Label(frameCentral2,text="Fecha de Casamiento:",bg="snow",font=("Rockwell",15),width =20)
fechaDeCasamiento.pack(side=TOP,pady=9)
salonDeEventos= Label(frameCentral2,text="Salón del Evento:",bg="snow",font=("Rockwell",15),width =20)
salonDeEventos.pack(side=TOP,pady=9)
aliasCbu= Label(frameCentral2,text="Alias/CBU/CVU:",bg="snow",font=("Rockwell",15),width =20)
aliasCbu.pack(side=TOP,pady=9)

#FRAME CENTRAL ENTRYS 2
frameCentral3= Frame(ventana,bg="snow",width =30, height=15)
frameCentral3.pack(side=LEFT,fill=BOTH)

#ENTRYS DATOS 2

paisEntry= Entry(frameCentral3,font=("Rockwell",15),width =25)
paisEntry.pack(side=TOP,pady=10)
provinciaEntry= Entry(frameCentral3,font=("Rockwell",15),width =25)
provinciaEntry.pack(side=TOP,pady=10)
fechaDeCasamientoEntry= Entry(frameCentral3,font=("Rockwell",15),width =25)
fechaDeCasamientoEntry.pack(side=TOP,pady=10)
salonDeEventosEntry= Entry(frameCentral3,font=("Rockwell",15),width =25)
salonDeEventosEntry.pack(side=TOP,pady=10)
aliasCbuEntry= Entry(frameCentral3,font=("Rockwell",15),width =25)
aliasCbuEntry.pack(side=TOP,pady=10)

ventana.mainloop()
