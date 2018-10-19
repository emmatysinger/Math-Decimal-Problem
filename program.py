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
factors = []

for k in non_repeating:
    while d%k == 0:
        factors.append(k)
        d /= k
    if k == 2:
        last_factor = d
        factors.append(int(d))


if last_factor != 1:
    numerator = 1
    r = 0
    while last_factor > numerator:
        numerator *= 10
        r += 1
    digit = numerator//last_factor
    new_n = numerator - digit*last_factor

    while new_n != 1:
        while last_factor > new_n:
            new_n *= 10
        digit = new_n//last_factor
        new_n = new_n - digit*last_factor
        r += 1
else:
    r = 0


nr = int(len(factors)-1)
    
print("""
Non-repeating: {0}
Repeating: {1}
""".format(nr, 0))