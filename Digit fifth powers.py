def num(n):
  l=[]
  x=0
  n = abs(n)
  while n > 0:
    x = n % 10
    l.append(x)
    n=n//10
  return(l)




n=int(input())
l=[]
li=[]
for i in range(n):
  x=num(i)
  #print(x)
  c=0
  for j in range(len(x)):
    c=x[j]**5+c
  print(c)
  print(i)
  l.append(c)
  if(c==i):
    li.append(i)

print(li)
