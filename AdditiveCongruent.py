#Additive Congruential Generator
b = eval(input("Enter the value of b: "))
m = eval(input("Enter the value of m (prime no.): "))
def seedACG(initVal):
    global rand
    rand = initVal
def acg():
    global rand
    a=1
    rand=(a*rand+b)% m
    return rand
seedACG(1)
for i in range(10):
    print(acg())

