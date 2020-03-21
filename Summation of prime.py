import math

def chkp(num):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        return 0
    else:
      return num
  else:
   return 0

t=int(input())
while(t>0):
  t=t-1
  li=[]
  n=int(input())
  l=[]
  for i in range(n):
    l.append(i)
  for i in range(n):
    c=chkp(l[i])
    li.append(c)
  print((li))
