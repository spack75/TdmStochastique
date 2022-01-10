import numpy as np
import math as m
import Interpreteurtxt as i
import scipy.integrate as sp
import matplotlib.pyplot as plt

Param=i.LireSettings("settings.txt")

N=Param["population"]
beta=Param["infectuosite"]
gamma=Param["severite"]
Tf=Param["temps de simulation"]
N0=Param["population saine initiale"]
NP=Param["nombre d'évaluations"]
R=Param["population rétablie initiale"]

I0=N-N0-R


def pend(y,t,beta,gamma,N):
    S,I,R=y
    dydt = [-beta/N*I*S,beta/N*I*S-gamma*I,gamma*I]
    return dydt
t=np.linspace(0,Tf,NP)
y0=[N0,I0,R]
sol = sp.odeint(pend,y0,t,args=(beta,gamma,N))

S=[i[0] for i in sol]
I=[i[1] for i in sol]
R=[i[2] for i in sol]

plt.figure()
plt.plot(t,S,"b",label='individu sain')
plt.plot(t,I,"r",label='individu infecté')
plt.plot(t,R,"g",label='individu rétabli')
plt.grid()
plt.legend()
plt.xlabel("temps")
plt.ylabel("effectif")
plt.show()