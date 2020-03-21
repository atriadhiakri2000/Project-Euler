def mi(n):
  l=[]
  li=[]
  for i in range(1,n):
    if(n%i==0):
      l.append(i)
  s=sum(l)
  print(l,s)
  for i in range(1,s):
    if(s%i==0):
      li.append(i)
  c=sum(li)
  print(li,c)
  if(c==n):
    return(1)
  else:
    return(0)
  
mi(220)
mi(1)
mi(2)
mi(3)
mi(4)
mi(5)
mi(6)
mi(7)
mi(8)
mi(9)
mi(10)
n=int(input())
c=0
for i in range (n):
  if (mi(i)==1):
    c=c+1
  else:
    c=c+0
print(c)
