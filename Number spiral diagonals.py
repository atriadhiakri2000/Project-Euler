n=int(input())
l=[]
li=[]
for i in range(3,n+1):
  if(i%2!=0):
    l.append(i)
print(l)

for i in range(len(l)):
  x=(4*l[i]**2)-(6*l[i])+6
  li.append(x)

s=sum(li)
print(s+1)




(4*n**2)-(6*n)+6

