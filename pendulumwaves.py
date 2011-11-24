#author alplhydan
#date: 12/11/2011

# this is a script to calculate the length of each pendulum in a
# pendulum wave setup (a physics experiment to create really cool pendulum dynamics)



from math import *



T=float(15)  #in seconds (time of whole period)
g=9.81           # gravitational constant
l_0=0.73 #in cm, length of longest pendulum available
coeff=g/(4*pi**2)


lengths=[]
for i in range(10):  #use the formula for a few penduli to find lengths
    lengths.append([i,coeff*T*T
                    /( T/
                       (2*pi*sqrt(l_0/g))+i
                       )**2])


for i in lengths:
    print i[0], '->', i[1]*100



# * smoke rings
# * smoke buble
# * Van der Graaf
# * Reverse Fluid
# * Glass and balls.
# * Explosions?

