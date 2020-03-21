t=int(input())
while(t>0):
  t=t-1
  s=0
  n=int(input())
  for i in range (n):
    if((i%3==0 or i%5==0) or (i%3==0 and i%5==0)):
       s=s+i
  print(s)
