from itertools import permutations 
def pathc(n):
  p=[]
  c=0
  sol=[]
  for i in range (n):
    p.append(0)
    p.append(1)
  print(p)
  perm = permutations(p,n*2)
  for i in perm:
    if i not in sol:
      print(i)
      c=c+1
      sol.append(i)
  print(c)
pathc(100)
