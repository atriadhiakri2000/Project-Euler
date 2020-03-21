def pali(n):
  temp=n
  rev=0
  a=0
  b=1
  while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
  if(temp==rev):
    return a
  else:
    return b


t=int(input())
while(t>0):
  t=t-1
  l=[]
  li=[]
  for i in range(100,1000):
    for j in range(100,1000):
       pro = i*j
       l.append(pro)
  
  for i in range(len(l)):
    if(pali(l[i])==0):
      li.append(l[i])
  print(max(li))
    
