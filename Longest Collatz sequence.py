def cs(n):
  l=[]
  c=1
  while(n!=1):
    l.append(n)
    if n%2!=0:
      n=n*3+1
    else:
      n=n//2
  l.append(n)
  k=len(l)
  #print(l)
  return(k)

m=0
l=[]
for i in range(1000000,1,-1):
  n=cs(i)
  if(n>m):
    m=n
    v=i
print(v)
'''
li=[]
for i in l:
  li.append(cs(i))
#print((li))
#print(max(li))

z=li.index(525)
print(z)
'''
