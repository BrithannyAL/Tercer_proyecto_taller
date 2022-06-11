from tkinter import messagebox

def ingresar_actividad(usuario,estudiantes,actividad,dia,hora_i,hora_f,radioValue,curso_r):
    if actividad == '' or dia == '' or hora_i == '' or hora_f == '':
        messagebox.showerror(message='Por favor rellene todos los campos')
    elif radioValue == 1:
        if curso_r == '':
            messagebox.showerror(message='Por favor rellene todos los campos')
        elif int(hora_i) > int(hora_f):
            print(hora_i)
            print(hora_f)
            messagebox.showerror(message='La hora de inicio es mayor a la hora final')
        else:
            usuario.actividades[dia].append(['Actividad:', actividad, 'dia:', dia, 'Hora de inicio:', hora_i, 'Hora final:',hora_f, 'Curso relacionado', curso_r])
            print(usuario.actividades)
            usuario.guardar_en_archivos()
            messagebox.showinfo(message='Actividad agregada exitosamente')
    elif radioValue == 2:
        if int(hora_i) > int(hora_f):
            print(hora_i)
            print(hora_f)
            messagebox.showerror(message='La hora de inicio es mayor a la hora final')
        else:
            usuario.actividades[dia].append(['Actividad:', actividad, 'dia:', dia, 'Hora de inicio:', hora_i, 'Hora final:',hora_f])
            print(usuario.actividades)
            while usuario.ant != None:
                usuario = usuario.ant
            usuario.guardar_en_archivos()
            messagebox.showinfo(message='Actividad agregada exitosamente')