import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfBanco = pd.read_csv("BANCO.csv",header = 0, sep = ",")

dfcredito = (dfBanco.TipoProducto == "CREDITO")
totalCredito = (dfcredito.sum())

dfahorro = (dfBanco.TipoProducto == "AHORRO")
totalAhorro = (dfahorro.sum())

dfnomina = (dfBanco.TipoProducto == "NOMINA")
totalNomina = (dfnomina.sum())

Lista = [totalCredito, totalAhorro, totalNomina]
indice = (dfBanco.TipoProducto.unique())

dfMovimientos = (dfBanco[(dfBanco.Sucursal == "HEB Las Puentes") & 
(dfBanco.TipoMovimiento == "PAGO") & (dfBanco.FechaMovimiento == "03/01/2021")])

plt.pie(Lista, labels = indice, shadow = False, autopct = '%1.1f%%')

plt.title('HEB Las Puentes')
plt.show()