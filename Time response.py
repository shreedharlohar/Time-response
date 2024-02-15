#!/usr/bin/env python
# coding: utf-8
import math
import numpy as np
import pandas as pd
import sys

#Characteristic Equation of Second Order System is p S^2 + q S + r = 0

def stability(p,q,r):
    if (p==0 and q==0 and r==0):
        print('Equation of Given sytem is invalid.')
        sys.exit()
    a=round(q/p,3)         
    b=round(r/p,3)        # now Characteristic Eqn become  S^2 + a S + b = 0    a=q/p and b=r/p
    print('Characteristic Equation of given system is \n s^2 + ',a,'s + ',b,'= 0','\n')
    #Natural Frequency
    Wn = b**0.5
    print('Natural Frequency = Wn =',round(Wn,3),'rad/s\n')
    
    #damping Factor
    zeta = a/(2*Wn)
    print('Damping Factor = zeta =',round(zeta,3),'\n')
    
    #Roots of Charecteristics equation
    S1=(-a+(a**2-4*1*b)**0.5)/2
    S2=(-a-(a**2-4*1*b)**0.5)/2
    print('Roots of Characteristic equation =')
    print('S1 =',round(S1.real,3),'+',round(S1.imag,3),'i\n')
    print('S2 =',round(S2.real,3),'+',round(S2.imag,3),'i\n')
    
    #damping frequency 
    Wd = Wn*((1-zeta**2 )**0.5)
    print('Damping frequency = Wd =',Wd,'rad/s\n')
    
    if (zeta>1):
        print('System is overdamped.')
    if (zeta<1 and zeta>0):
        print('System is underdamped.')
    if (zeta==1):
        print('System is critically damped.')
    if (zeta==0):
        print('System is undamped.')


# Test your program 


stability(2,6,5)





stability(3.26,17.5,44.2)




stability(0.01,8,9)





stability(2,8,8)





stability(11,0,3)

