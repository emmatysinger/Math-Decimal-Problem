from math import *

n = int(input("Numerator? "))
d = int(input("Denominator? "))

common_factor = 1
for i in range(min(abs(n), abs(d)), 1, -1):
     if n%i == 0 and d%i == 0:
         common_factor = i
         break

n = n/i
d = d/i
     
print("Simplified fraction is {0}/{1}".format(int(n), int(d)))
