<<<<<<< HEAD
from datetime import datetime
from proyecto3 import rostro
from control import detectar_emociones
 
def noSe():
    hora1 = datetime.strptime("00:00:00", "%X").time()
    hora2 = datetime.strptime("00:15:00", "%X").time()
    hora_act = datetime.now().time()
    
    if hora_act > hora1 and hora_act < hora2:
        print ("SI")
        print(hora_act)
    elif hora_act < hora1 and hora_act > hora2:
        print ("NO")
=======
import pandas as pd
import matplotlib.pyplot as plt

# Let's create a Dataframe using lists
countries = ['Alegria', 'Pena', 'Ira', 'Sorpresa']

area = [2, 106, 6, 97]

pop_density = [19341, 8041, 5620, 2046]

# Now, create a pandas dataframe using above lists
df_pop_density = pd.DataFrame(
    {'Country' : countries, 'Area(100kmsq)' : area,
    'Population Density(/kmsq)' : pop_density})

df_pop_density




# Creating figure and axis objects using subplots()
fig, ax = plt.subplots(figsize=[9, 7])

ax.plot(df_pop_density['Country'],
         df_pop_density['Area(100kmsq)'],
         marker='o', linewidth=2, label='Area')
ax.plot(df_pop_density['Country'],
         df_pop_density['Population Density(/kmsq)'],
         marker='o', linewidth=2, 
         label='Population Density')
plt.xticks(rotation=60)
ax.set_xlabel('Countries')
ax.set_ylabel('Area / Population Density')
plt.legend()
plt.show()
>>>>>>> 555a490e9d4e6fb7952426a79d36c5fff2122f62
