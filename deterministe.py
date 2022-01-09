import numpy as np
import math as m
import scipy.integrate as sp
import matplotlib.pyplot as plt

N=10000
beta=0.7
gamma=0.1
def pend(y,t,beta,gamma,N):
    S,I,R=y
    dydt = [-beta/N*I*S,beta/N*I*S-gamma*I,gamma*I]
    return dydt
t=np.linspace(0,100,10000)
y0=[9990,10,0]
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