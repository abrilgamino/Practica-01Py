import pandas as pd

exelData = pd.read_excel('C:/Users/miche/OneDrive/Documentos/EBC-Python/Practica-01Py/informe global_2_dic - copia.xlsx')
dataFrame = pd.DataFrame(exelData)

print(dataFrame.head())
