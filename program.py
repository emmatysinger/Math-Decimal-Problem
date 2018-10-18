from math import *

n = int(input("Numerator? "))
d = int(input("Denominator? "))

common_factor = 1
for i in range(min(abs(n), abs(d)), 1, -1):
     if n%i == 0 and d%i == 0:
         common_factor = i
         break

n = n/common_factor
d = d/common_factor
non_repeating = [10, 5, 2]
# w = { 2:[1,0], 3:[0,1], 5:[1,0], 7:[0,6], 9:[0,1], 11:[0,2]}
print("Simplified fraction is {0}/{1}".format(int(n), int(d)))
factors = []

for k in non_repeating:
    while d%k == 0:
        factors.append(k)
        d /= k
    if k == 2:
        factors.append(int(d))


for i in factors:
    if i != 2 and i != 5:
        while True:
            k=1
            if (10**k-1)%i == 0:
                r = k
                break
            k += 1
    
    print(r)