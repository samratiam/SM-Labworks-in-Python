#generating random number using mixed multiplicative congruential method
import numpy as np
r=[]
def seedMCG(initVal):
    global rand
    rand = initVal
a = 48
b = 61
m = 19
def mcg():
    global rand
    rand=(a*rand+b)% m
    return rand
seedMCG(1)
for i in range(50):
    r.append(mcg())
print(r)

