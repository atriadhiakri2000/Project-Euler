t=int(input())
while(t>0):
  t=t-1
  n=int(input())
  l=[]
  li=[]
  for i in range(n+1):
    a=i*i
    l.append(a)
  print(l)
  for i in range(n+1):
    li.append(i)
  print(li)
  s1=sum(l[0:n+1])
  print(s1)
  s2=sum(li[0:n+1])
  print(s2)
  s3=s2*s2
  print(s3)
  print(s1-s3)
