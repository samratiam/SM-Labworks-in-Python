#Chi Square Test
import numpy as np
import MixedMultiplicative as mm

#generating random number using mixed multiplicative congruential method
#a = 63 b = 36 m = 31

print("The random numbers are: ",mm.r)
high = max(mm.r)
low = min(mm.r)
print("Minimum value: ",low)
print("Maximum value:",high)

print("Observed frequencies: ")
observed = []
count = 0
while(low<=high):
    c = len(list(x for x in mm.r if low<=x<low+3))
    observed.append(c)
    low = low + 3
    count = count + 1
print("Total no. of classes: ",count)
print("Observed frequencies: ",observed)

print("Expected frequencies: ")
for i in range(0,len(observed)):
    expected=np.array(sum(observed)/len(observed))
    calculate=np.array(((observed-expected)**2)/expected)
    print(np.round(expected,5))
print("The chi square values are:",np.round(calculate,5))
chi_square_calculated=sum(calculate)

print("The calculated sum of chi square values is: ",round(chi_square_calculated,5))

#chi_square_tabulated=18.307
print("Enter tabulated value of Chi Square at d.f=",count-1)
chi_square_tabulated = eval(input())
print("The tabulated value of Chi Square= ",chi_square_tabulated)
if chi_square_calculated<chi_square_tabulated:
    print("Hypothesis is accepted")
else:
    print("Hypothesis is rejected")


