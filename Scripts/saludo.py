import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-saludo","--s", default = "", type = str)

args = parser.parse_args()

texto = args.s
texto = texto.upper()
if texto == "HOLA":
    opciones = ["Hola, ¿cómo estas?", "Mucho gusto, me llamo Computina", "Disculpa pero no quiero hablar contigo"]
    probabilidades = [0.5,0.25,0.25]
    respuesta = random.choices(opciones, probabilidades)[0]
    print(respuesta)
else:
    print("Parece que tus padres no te enseñaron a saludar...")