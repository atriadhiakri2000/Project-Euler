n=2**1000
print(n)
c=0
res = [int(x) for x in str(n)] 
print(res)
for i in res:
    c=c+i
print(c)
