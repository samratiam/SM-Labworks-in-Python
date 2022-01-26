#Mixed Multiplicative Congruential Generator
a = eval(input("Enter the value of a(a>1): "))
b = eval(input("Enter the value of b(b>0): "))
m = eval(input("Enter the value of m(prime no.): "))
def seedMCG(initVal):
    global rand
    rand = initVal
def mcg():
    global rand
    rand=(a*rand+b)% m
    return rand
seedMCG(1)
r = []
for i in range(50):
    r.append(mcg())
#print(r)



