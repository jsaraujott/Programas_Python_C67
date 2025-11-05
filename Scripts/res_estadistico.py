# Cargar librerias
import pandas as pd
import argparse

# Crear generador sintatico
parser = argparse.ArgumentParser()
parser.add_argument("file", type = str)

#Traducir variables de la terminal
args = parser.parse_args()

# Ajustar código
datos = pd.read_csv(args.file, header = None)
resumen = datos.describe().round(1).loc[["mean","std","25%","50%","75%"]]
resumen.index = ["Media", "Desv. Est.", "Q1", "Mediana", "Q3"]
resumen.columns = ["Metricas"]
print(resumen)