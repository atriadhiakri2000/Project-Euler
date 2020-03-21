import fractions

def lcm(n):
  a=1
  for i in range(1,n+1):
    a=(a*i)/fractions.gcd(a,i)
  return a
  
t=int(input())
while(t>0):
  t=t-1
  n=int(input())
  l=lcm(n)
  print(l)
