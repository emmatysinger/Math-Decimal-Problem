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
        last_factor = d
        factors.append(int(d))

if last_factor != 0:
    numerator = 1
    while last_factor > numerator:
        numerator *= 10
    digit = numerator//last_factor
    new_n = numerator - digit*last_factor
    r = 1

    while new_n != 1:
        while last_factor > new_n:
            new_n *= 10
        digit = new_n//last_factor
        new_n = new_n - digit*last_factor
        r += 1


nr = int(len(factors)-1)
    
print("""
Non-repeating: {0}
Repeating: {1}
""".format(nr, r))