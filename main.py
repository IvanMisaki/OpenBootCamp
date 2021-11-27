from numpy.matrixlib.defmatrix import _convert_from_string
import pandas as pd
df = pd.read_excel("Datos.xlsx",index_col=0)
eliminarEmails = df.drop_duplicates(subset=["email"])
x_inicial = int(df.count())
x_final = int(eliminarEmails.count())
print("Son un Total de "+str(x_inicial)+ " registros, pero solo "+str(x_final)+ " son únicos")
print(eliminarEmails)