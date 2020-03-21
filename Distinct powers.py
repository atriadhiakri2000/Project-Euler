def Remove(duplicate):
  final_list = []
  for num in duplicate:
    if num not in final_list:
      final_list.append(num)
  return final_list 


n=int(input())
l=[]
for i in range(301,n+1):
  for j in range(301,n+1):
    x=i**j
    l.append(x)

print(l)
l.sort()
y=Remove(l)

print(y)

u=len(y)

print(u)
