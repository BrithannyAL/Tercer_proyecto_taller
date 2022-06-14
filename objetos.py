from tkinter import messagebox

class usuario:
    nombre = None
    carreras = []
    cursos = []
    usuario = None
    contrasena = None
    actividades = None
    sig = None
    ant = None

    def __init__(self,n,ca,cu,u,c,act):
        self.nombre = n
        self.carreras= ca
        self.cursos= cu
        self.usuario= u
        self.contrasena = c
        self.actividades = act
        
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
        rn.ant = puntero
        
    def recorrer_lista(self) -> str:
        actual = self
        respuesta = "["
        while actual.sig != None:
            respuesta+=f"'{actual.nombre, actual.carreras, actual.cursos, actual.usuario, actual.contrasena, actual.actividades}',"
            actual=actual.sig
        respuesta+= f"'{actual.nombre, actual.carreras, actual.cursos, actual.usuario, actual.contrasena, actual.actividades}']"
        return respuesta
    
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("usuario.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.nombre, puntero.carreras, puntero.cursos, puntero.usuario, puntero.contrasena, puntero.actividades].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.nombre, puntero.carreras, puntero.cursos, puntero.usuario, puntero.contrasena, puntero.actividades].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la información en los archivos")                      
            

class emociones:
    usuario = None
    actividad = None
    emociones = None
    sig = None
    ant = None

    def __init__(self, u, a, e):
        self.usuario = u
        self.actividad = a
        self.emociones = e

    def recorrer_lista(self) -> str:
        actual = self
        respuesta = "["
        while actual.sig != None:
            respuesta+=f"'{actual.usuario, actual.actividad, actual.emociones}',"
            actual=actual.sig
        respuesta+= f"'{actual.usuario, actual.actividad, actual.emociones}']"
        return respuesta
    
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
        rn.ant = puntero
        
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("emociones.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.usuario, puntero.actividad, puntero.emociones].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.usuario, puntero.actividad, puntero.emociones].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la informaciÃ³n en los archivos")
    

        
