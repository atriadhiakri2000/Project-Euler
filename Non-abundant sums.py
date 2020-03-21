def abno(n):
  l=[]
  for i in range(1,n):
    if(n%i==0):
      l.append(i)
  s=sum(l)
  #print(l)
  #print(s)
  if(s!=n):
    return(1)
  else:
    return(0)

print(abno(12))
n=int(input())
l=[]
for i in range(1,n):
  c=abno(i)
  if(c==1):
    print(i)
