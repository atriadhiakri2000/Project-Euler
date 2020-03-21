t=int(input())
while(t>0):
  t=t-1
  n=int(input())
  a=1
  b=2
  c=0
  l=[]
  l.append(a)
  l.append(b)
  for i in range(n-2):
    c=a+b
    l.append(c)
    a=b
    b=c

  li=[]
  for i in range(len(l)):
    if(l[i]%2==0):
      li.append(l[i])

  print(sum(li[0:n]))
