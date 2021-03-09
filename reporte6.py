import pandas as pd
import matplotlib.pyplot as plt
dfBanco = pd.read_csv("BANCO.csv",header = 0, sep = ",")

dfCORPORATIVO = (dfBanco[(dfBanco.TipoProducto == "CREDITO") & 
(dfBanco.Sucursal  == "CORPORATIVO")])

dfHEB_VALLE_ALTO = (dfBanco[(dfBanco.TipoProducto == "CREDITO") & 
(dfBanco.Sucursal  == "HEB VALLE ALTO")])

dfTAMPICO_II = (dfBanco[(dfBanco.TipoProducto == "CREDITO") & 
(dfBanco.Sucursal  == "TAMPICO II")])

dfPIEDRAS_NEGRAS = (dfBanco[(dfBanco.TipoProducto == "CREDITO") & 
(dfBanco.Sucursal  == "PIEDRAS NEGRAS")])

dfMI_TIENDA_AZTLAN = (dfBanco[(dfBanco.TipoProducto == "CREDITO") & 
(dfBanco.Sucursal  == "MI TIENDA AZTLAN")])

Cantidad_1 = (dfCORPORATIVO.NoBimestre.sum())
Cantidad_2 = (dfHEB_VALLE_ALTO.NoBimestre.sum())
Cantidad_3 = (dfTAMPICO_II.NoBimestre.sum())
Cantidad_4 = (dfPIEDRAS_NEGRAS.NoBimestre.sum())
Cantidad_5 = (dfMI_TIENDA_AZTLAN.NoBimestre.sum())

Cantidades = [Cantidad_1, Cantidad_2, Cantidad_3, Cantidad_4, Cantidad_5]

sucursales = ["CORPORATIVO", "HEB VALLE ALTO", "TAMPICO II", "PIEDRAS NEGRAS", "MI TIENDA AZTLAN"]

plt.plot(sucursales,Cantidades)

plt.show()