import argparse

# Crear un generador sintático de variables para la terminal
parser = argparse.ArgumentParser(description = "Programa que devuelve el numero de pares deseados")
parser.add_argument("n", type = int, help = "Numero de valores pares deseados")

# Tradcuir variable sintatica a python
args = parser.parse_args()

#Ajustar codigo original
num = 0
for i in range(args.n):
  num += 2
  print(num)
