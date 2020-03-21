n=int(input("Enter the range of the fibonacci series : "))
l=[]
li=[]
a=1
b=1
c=0
l.append(a)
l.append(b)
while(n>0):
  c=a+b
  l.append(c)
  a=b
  b=c
  n=n-1

#print(l)

for i in range(len(l)):
  Number=l[i]
  x=0
  while(Number > 0):
    Number = Number // 10
    x = x + 1
  li.append(x)
  if(li[i]==100):
    print(li[i])
