t=int(input())
while(t>0):
  t=t-1
  n=1000
  l=[]
  for j in range(n+1):
    l.append(j)
  for i in range(1,n+1):
    for j in range(i,n+1):
      for k in range(j,n+1):
        if(i+j+k==1000):
          if((i**2)+(j**2)==(k**2)):
            print(i,k,j)
