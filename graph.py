import pandas as pd
import matplotlib.pyplot as plt

def crear_grafica(lista):

  emociones = ['Alegria', 'Pena', 'Ira', 'Sorpresa', 'Confusion']

  veces = [lista[0],lista[1],lista[2],lista[3],lista[4]]


  df_veces = pd.DataFrame(
      {'emociones' : emociones, 
      'Veces de la emocion presentada' : veces})

  df_veces


  fig, ax = plt.subplots(figsize=[9, 7])

  ax.plot(df_veces['emociones'],
          df_veces['Veces de la emocion presentada'],
          marker='o', linewidth=2, 
          label='Veces de la emocion presentada')
  plt.xticks(rotation=60)
  ax.set_xlabel('emociones')
  ax.set_ylabel('Veces de la emocion presentada')
  plt.legend()
  plt.show()