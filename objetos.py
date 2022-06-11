from tkinter import messagebox

class usuario:
    nombre = None
    carreras = []
    cursos = []
    usuario = None
    contrasena = None
    horario = None 
    actividades = None
    sig = None
    ant = None

    def __init__(self,n,ca,cu,u,c,act,dich):
        self.nombre = n
        self.carreras= ca
        self.cursos= cu
        self.usuario= u
        self.contrasena = c
        self.actividades = act
        self.horario = dich
   
    def recorrer_lista(self) -> str:
        actual = self
        respuesta = "["
        while actual.sig != None:
            respuesta+=f"'{actual.nombre, actual.carreras, actual.cursos, actual.usuario, actual.contrasena,actual.actividades, actual.horario}',"
            actual=actual.sig
        respuesta+= f"'{actual.nombre, actual.carreras, actual.cursos, actual.usuario, actual.contrasena,actual.actividades, actual.horario}']"
        return respuesta

    def buscar(self,a):
        actual = self
        while actual.sig != None:
            if actual.usuario == a:
                return actual.nombre, actual, actual.carreras, actual.cursos, actual.usuario, actual.contrasena, actual.actividades,actual.horario
            else:
                actual = actual.sig
                if actual.usuario == a:
                    return actual.nombre, actual.carreras, actual.cursos, actual.usuario, actual.contrasena, actual.actividades, actual.horario
        return False
    
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
        rn.ant = puntero
        
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("estudiantes.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.nombre, puntero.carreras, puntero.cursos, puntero.usuario, puntero.contrasena, puntero.actividades, puntero.horario].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.nombre, puntero.carreras, puntero.cursos, puntero.usuario, puntero.contrasena, puntero.actividades, puntero.horario].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la información en los archivos")