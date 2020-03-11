# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:39:14 2020

@author: rodri
"""

def BT(S0,k,rf,t,v,tipo=1,style=1,steps=100):
    """S0 is spot price at time 0
    k is strike price
    rf is risk free
    t is time in years
    v is volatility 
    tipo is equal to 1 when it is a call and -1 when it is a put
    style is equal to 1 when it is an american option and 0 when a european option
    Automatically prices an American Call option
    steps is the number of steps in binomial trees
    """
    import numpy as np    
    x=np.zeros(steps-1)
    
    for n in range(1,steps):
        dt=t/n
        u=np.exp(v*np.sqrt(dt))
        d=1/u
        p=(np.exp(rf*dt)-d)/(u-d)
        q=1-p
        S=np.zeros((n+1,n+1))
        for i in range(n+1):
            for j in range(n-i+1):
                S[i,j+i]=S0*u**j*d**i
        C=np.zeros((n+1,n+1))
        for i in range(n+1):
                if (tipo==1):
                    C[i,n]= np.maximum(S[i,n]-k,0)
                if(tipo==-1):
                    C[i,n]=np.maximum(k-S[i,n],0)
        for j in range(n,0,-1):
            for i in range(j):
                C[i,j-1]=np.maximum((C[i,j]*p+C[i+1,j]*q)*np.exp(-rf*dt),
                 (S[i,j-1]-k)*tipo*style)
        x=C[0,0]
    if tipo==1 and style==1:
        print("American Call:", x)
    elif tipo==-1 and style==1:
        print("American Put", x)
    elif tipo==1 and style==0:
        print("European Call:", x)
    elif tipo==-1 and style==0:
        print("European Put:", x)
    else:
        print("Please insert the accepted values for tipo and style" )
    return
