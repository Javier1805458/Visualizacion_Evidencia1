import pandas as pd
import matplotlib.pyplot as plt

dfBanco = pd.read_csv("BANCO.csv",header = 0, sep = ",")

dfheb = (dfBanco[(dfBanco.Sucursal == "HEB SAN PEDRO")])

Viernes = (dfheb[(dfBanco.FechaMovimiento == "01/01/2021")])
Sabado = (dfheb[(dfBanco.FechaMovimiento == "02/01/2021")])
Domingo = (dfheb[(dfBanco.FechaMovimiento == "03/01/2021")])
Lunes = (dfheb[(dfBanco.FechaMovimiento == "04/01/2021")])
Martes = (dfheb[(dfBanco.FechaMovimiento == "05/01/2021")])
Miercoles = (dfheb[(dfBanco.FechaMovimiento == "06/01/2021")])
Jueves = (dfheb[(dfBanco.FechaMovimiento == "07/01/2021")])

Montos = [Viernes.Monto.sum(), Sabado.Monto.sum(), Domingo.Monto.sum(), Lunes.Monto.sum(),
Martes.Monto.sum(), Miercoles.Monto.sum(), Jueves.Monto.sum()]

Fechas = ["Viernes","Sabado","Domingo","Lunes","Martes","Miercoles","Jueves"]

plt.scatter(Fechas, Montos)
plt.title('HEB SAN PEDRO')
plt.show()


