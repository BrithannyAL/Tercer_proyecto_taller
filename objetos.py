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
    

        
