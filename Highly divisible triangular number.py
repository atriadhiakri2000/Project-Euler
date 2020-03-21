'''def print_factors(x):
  c=0
  for i in range(1, x + 1):
    if x % i == 0:
      c=c+1
  if(c==500):
      return(x)

l=[]
li=[]
s=0
n=int(input())
for i in range(1,n):
  s=s+i
  l.append(s)
#print(*l)
c=0
for i in range(len(l)):
  c=print_factors(l[i])
  li.append(c)
print(li)
'''

import math
from time import time
t = time()
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
        print (x)
        break
tt = time()-t
print (tt)
