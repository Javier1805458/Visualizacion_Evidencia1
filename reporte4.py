import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfBanco = pd.read_csv("BANCO.csv",header = 0, sep = ",")


dfHebLasPuentes = (dfBanco[(dfBanco.Sucursal == "HEB Las Puentes") & 
(dfBanco.TipoMovimiento == "PAGO") & (dfBanco.FechaMovimiento == "05/01/2021")])

CORPORATIVO = (dfBanco[(dfBanco.Sucursal == "CORPORATIVO") & 
(dfBanco.TipoMovimiento == "PAGO") & (dfBanco.FechaMovimiento == "05/01/2021")])

MiTienda = (dfBanco[(dfBanco.Sucursal == "MI TIENDA ZUAZUA") & 
(dfBanco.TipoMovimiento == "PAGO") & (dfBanco.FechaMovimiento == "05/01/2021")])

PiedrasNegras = (dfBanco[(dfBanco.Sucursal == "PIEDRAS NEGRAS") & 
(dfBanco.TipoMovimiento == "PAGO") & (dfBanco.FechaMovimiento == "05/01/2021")])

Transacciones = [dfHebLasPuentes.Monto.sum(), CORPORATIVO.Monto.sum(), MiTienda.Monto.sum(), PiedrasNegras.Monto.sum()]

Nombres = ["Heb Las Puentes", "CORPORATIVO", "MI TIENDA ZUAZUA", "PIEDRAS NEGRAS"]

plt.bar(Nombres, height = Transacciones, width = 0.5)

plt.title('Transacciones realizadas el 05/01/2021')
plt.show()

print(dfHebLasPuentes.Monto.sum())