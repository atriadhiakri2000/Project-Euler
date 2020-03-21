def f(n,d):
  x=n*9
  z=x
  k=1
  while(z%d):
    z=z*10+x
    k=k+1
  return(k,z/d)

x=0
z=0
k=0
for d in range(1,10):
  n=1
  print(f(n,d))
