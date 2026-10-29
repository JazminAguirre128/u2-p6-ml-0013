import pandas as pd
import  numpy as np

series_amigos = ["Pedro", "Morgan", "Farfan", "Adrian", "Jessie", "Ricardo", "Caleb"]
print("------ Serie listado de amigos   NC = 0013 ------")
amigos = pd.Series(series_amigos)
print(amigos)

series_billetes = [20, 50, 100, 200, 500, 1000]
print("------ Serie listado de billetes   NC = 0013 ------")
billetes = pd.Series(series_billetes)
print(billetes)

series_billetes = [20, 50, 100, 200, 500, 1000]
serie_letras = ["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
print("------ Serie listado nombre y valor de billetes MX NC = 0013 ------")
tablabilletes = pd.Series(serie_letras, series_billetes)
print(tablabilletes)
# Diccinario DataFrame
# Diccionario monedas valor y nombre 
print("------ Datos de diccionario a Data Frame en Pandas ------")
dicc_monedas = {
    "series_billetes" : [20, 50, 100, 200, 500, 1000],
    "serie_letras" : ["Veinte", "Cincuenta", "Cien", "Doscientos", "Quinientos", "Mil"]
}
tablajazmin = pd.DataFrame(dicc_monedas, index = ["A", "B", "C", "D", "E", "F"])
print(tablabilletes)

print("Casa de cambio  de Meredith Aguirre NC = 0013")