# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 13:53:02 2022

@author: richi
"""

# -*- coding: utf-8 -*-
from scipy.stats import norm
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime

start = '1/1/2013' #fecha inicio
end = '31/12/2018' #fecha fin

# Obtención de los datos
apple = pdr.get_data_yahoo("AAPL", start=start, end=end)
microsoft = pdr.get_data_yahoo("MSFT", start=start, end=end)
amazon = pdr.get_data_yahoo("AMZN", start=start, end=end)

#Para obtener el valor real de las acciones el 31/12/2020
start2 = '31/12/2020' 
end2 = '31/12/2020' 

apple_2020 = pdr.get_data_yahoo("AAPL", start=start2, end=end2)['Close'] #Nos quedamos con el valor de cierre
microsoft_2020 = pdr.get_data_yahoo("MSFT", start=start2, end=end2)['Close']
amazon_2020 = pdr.get_data_yahoo("AMZN", start=start2, end=end2)['Close']

'''
Función que lleva a cabo los cálculos pedidos
'''
def analisis(empresa,nombre):
    
    accion=empresa['Close']
    val=accion[-1] #valor de la acción el 31/12/2018
    
    #Cálculo r
    r=0
    dt=1.0/260 # Aproximación 52 semanas*5 dias
    for i in range(len(accion)-1):
        r+=np.log(accion.iloc[i+1]/accion.iloc[i])
    r=r/(len(accion)-1)/dt
    
    #Cálculo s2
    s2=0
    for i in range(len(accion)-1):
        s2+=(np.log(accion.iloc[i+1]/accion.iloc[i])-r*dt)**2
    s2=s2/(len(accion)-1)/dt
    
    #Cálculo valor esperado el 31/12/2020
    R=r+s2**2*0.5
    esp=val*np.exp(2*R)
    
    #Probabilidad 2020
    t=2
    x=np.log(1.2)
    media=r*t
    sigma=np.sqrt(s2*t)
    prob2020=1-norm.cdf(x, loc=media, scale=sigma)
    
    
    #Probabilidad 2022
    t=2
    x=np.log(47.32/132.69)
    media=r*t
    sigma=np.sqrt(s2*t)
    prob2022=1-norm.cdf(x, loc=media, scale=sigma)
    
    
    print("Empresa: %s"%nombre)
    print("r=%f"%r)
    print("s2=%f"%s2)
    print("R=%f"%R)
    print("Valor_2018=%f"%val)
    print("Valor_esperado_2020=%f"%esp)
    print("Probabilidad_ganancia_2020: %f"%prob2020)
    print("Probabilidad_ganancia_2022: %f"%prob2022)
    print("")

analisis(apple,"Apple")    
analisis(microsoft, "Microsoft")
analisis(amazon, "Amazon")


#Parámetros Black-Scholes entre 2018 y 2020 Microsoft
start3 = '31/12/2018' 
end3 = '31/12/2020' 
micro= pdr.get_data_yahoo("MSFT", start=start3, end=end3)['Close']

#Cálculo r
r=0
dt=1.0/260 # Aproximación 52 semanas*5 dias
for i in range(len(micro)-1):
    r+=np.log(micro.iloc[i+1]/micro.iloc[i])
r=r/(len(micro)-1)/dt

#Cálculo s2
s2=0
for i in range(len(micro)-1):
    s2+=(np.log(micro.iloc[i+1]/micro.iloc[i])-r*dt)**2
s2=s2/(len(micro)-1)/dt