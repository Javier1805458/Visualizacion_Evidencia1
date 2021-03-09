import pandas as pd
import matplotlib.pyplot as plt

dfBanco = pd.read_csv("BANCO.csv",header = 0, sep = ",")

dfCorporativo = (dfBanco[(dfBanco.Sucursal == "CORPORATIVO") & 
(dfBanco.FechaMovimiento == "06/01/2021")])
MontoVendidoEnCorporativo = (dfCorporativo.Monto.sum())

dfOtraSucursal = (dfBanco[(dfBanco.Sucursal != "CORPORATIVO") & 
(dfBanco.FechaMovimiento == "06/01/2021")])

MontoVendidosEnOtraSucursal = (dfOtraSucursal.Monto.sum())
#colores
colores = ['red', 'blue']
#Labels
Lista = ['CORPORATIVO', 'OTRA SUCURSAL']
#Cantidades 
Cantidades = [MontoVendidoEnCorporativo, MontoVendidosEnOtraSucursal]

plt.bar(Lista, height = Cantidades, width = 0.5, color = colores)

plt.title('Corporativo vs sucursales')
plt.show()