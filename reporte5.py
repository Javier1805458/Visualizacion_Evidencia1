import pandas as pd
import matplotlib.pyplot as plt
dfBanco = pd.read_csv("BANCO.csv",header = 0, sep = ",")

df2101 = (dfBanco[(dfBanco.BINE == 2101) & 
(dfBanco.FechaMovimiento == "01/01/2021")])

df2601 = (dfBanco[(dfBanco.BINE == 2601) & 
(dfBanco.FechaMovimiento == "01/01/2021")])

df2201 = (dfBanco[(dfBanco.BINE == 2201) & 
(dfBanco.FechaMovimiento == "01/01/2021")])

Monto1 = (df2101.Monto.sum())
Monto2 = (df2601.Monto.sum())
Monto3 = (df2201.Monto.sum())

Cantidades = [Monto1, Monto2, Monto3]

Bine = (dfBanco.BINE.unique())

plt.pie(Cantidades, labels = Bine, shadow = False, autopct = '%1.1f%%')

plt.title('Montos por BINE')
plt.show()

