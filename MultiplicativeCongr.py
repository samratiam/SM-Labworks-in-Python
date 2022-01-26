#Multiplicative Congruential Generator
a = eval(input("Enter the value of a: "))
m = eval(input("Enter the value of m (prime no.): "))
def seedMCG(initVal):
    global rand
    rand = initVal
def mcg():
    global rand
    b=0
    rand=(a*rand+b)% m
    return rand
seedMCG(1)
for i in range(50):
    print(mcg())

