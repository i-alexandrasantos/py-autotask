import pyautogui
import time
from datetime import datetime

pyautogui.PAUSE = .5

#abre o bloco de notas
pyautogui.press("win")
pyautogui.write("bloco")
pyautogui.press("enter")


name = "Alexandra!"
horaAtual = datetime.now().hour

if 6 <= horaAtual < 18:
    saudacao = "Bom dia, "
else:
    saudacao = "Boa noite, "

pyautogui.write(saudacao+name)


#importa as frases
import pandas as pd

frases = pd.read_json("frases.json", encoding="utf-8")

print(frases.head())

fraseAleatoria = frases.sample(n=1)
frase = fraseAleatoria['Frase'].values[0]

pyautogui.write(" Frase de hoje... ")
pyautogui.write(frase)