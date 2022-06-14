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

    def __init__(self,n,ca,cu,u,c,act):
        self.nombre = n
        self.carreras= ca
        self.cursos= cu
        self.usuario= u
        self.contrasena = c
        self.actividades = act
    
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
            
"""actividades = {'Monday': [['Estudiar', '00:12:10', '00:12:30', 'Comunicacion escrita']],
                'Thursday': [],
                'Wednesday': [],
                'Friday': [],
                'Saturday': [['Dormir', '22:00:00', '23:00:00', 'None']],
                'Sunday': [['Dormir', '00:14:00', '00:23:00', 'None']]}
            
objeto_usuario = usuario('Brithanny Arguello', [3], [1, 2, 3, 4, 5, 6], 'barguello', '827ccb0eea8a706c4c34a16891f84e7b', actividades)
objeto_usuario.guardar_en_archivos()"""
            
            

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
    

        
