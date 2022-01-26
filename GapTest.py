#Gap test for independence of random numbers

# import MixedMultiplicative as mm
randomVal = [4,1,3,5,1,7,2,8,2,0,7,9,1,3,5,2,7,9,4,1,6,3,3,9,6,3,4,8,2,3,1,9,4,4,6,8,4,1,3,8,9,5,5,7,3,9,5,9,5,8,3,2,2,3,7,4,
             7,0,3,6,3,5,9,9,5,5,5,0,4,6,8,0,4,7,0,3,3,0,5,5,7,9,5,1,6,6,3,8,8,8,9,2,9,1,8,5,4,4,5,0,2,3,9,7,1,2,0,3,6,3]
freq = []
count = 0
again = True
g = []
t = []
length = []
new = []
p = 0
v = 0
z = 0
upper_limit = []
rf_list = []
cf_list = []
tf_list = []
m = 0
n = 0
u = 0
cf = 0
Diff = []

#calculate gap length of each distinct digits
def count_gaplength(k):
    length = []
    i = 0
    d = 0
    for i in range(len(randomVal)):
        if s[k] == randomVal[i]:
            break
    for j in range(i + 1,len(randomVal)):
        if s[k] == randomVal[j]:
            d = j - i - 1
            length.append(d)
            if again:
                i = j

    #inserting all the gap lengths in another list
    for p in range(len(length)):
        t.append(length[p])
    return length


#to get distinct generated random numbers
def unique(list1):
    unique_list = []

    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

#generate random numbers from mixed multiplicative method of another file
# randomVal = mm.r
print("The random numbers are: ",randomVal)
N = len(randomVal)
print("Total no. of digits: ",N)

#making the list of distinct digits
distinct_list = unique(randomVal)
print("The distinct numbers are: ",sorted(distinct_list))
D = len(distinct_list)
print("Total no. of distinct digits: ",D)

#calculate total no. of gaps
total_gaps = N - D
print("Total no. of gaps: ",total_gaps)

#sorting the distinct digit list
s = sorted(distinct_list)

#to display gap length of each distinct digit
for k in range(len(s)):
    c = count_gaplength(k)
    print("Gap length of ",s[k]," =",c)

print("List of the lengths of gaps of each digits: ",t)

#get the list of all gap lengths and make it's class and frequency table
low = min(t)
high = max(t)
while(low <= high):
    c = len(list(v for v in t if low <= v < low + 4))
    freq.append(c)
    low = low + 4
    count = count + 1
print("Total no. of classes of gap length with each class interval of size 3: ",count)
print("Frequencies of each class of gap length of 3: ",freq)

#calculate relative frequency
freq_sum = sum(freq)
print("Sum of frequencies: ",freq_sum)
for z in range(len(freq)):
    rf = freq[z] / freq_sum
    rf_list.append(round(rf,5))
print("Relative frequencies: ",rf_list)

#calculate cummulative frequency
for u in range(len(rf_list)):
    cf = cf + rf_list[u]
    cf_list.append(round(cf,5))
print("Cummulative freq(Sn(x)): ",cf_list)

#create list of upper limit values
m = min(t)
n = max(t)
while m <= n:
    m = m + 3
    upper_limit.append(m)
    m = m + 1

#calculate theoretical frequencies
for i in range(len(upper_limit)):
    x = upper_limit[i]
    y = 1 - pow(0.9,x+1)
    tf_list.append(round(y,5))
print("Theoretical frequencies: ",tf_list)

#difference of theoretical & cummulative frequencies
for i in range(len(freq)):
    x = tf_list[i] - cf_list[i]
    Diff.append(round(x,5))
print("List of difference between relative & theoretical frequencies: ",Diff)
Dcal = max(Diff)
print("Calculated value of D = ",Dcal)

#take the tabulated value of D for alpha=0.05
#Dtab = 0.432
Dtab = eval(input("Enter tabulated value of D: "))

#hypothesis testing
if Dcal > Dtab:
    print("Null hypothesis is rejected")
else:
    print("Null hypothesis is accepted")













