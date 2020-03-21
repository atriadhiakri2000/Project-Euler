#75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23



'''triangle = [
  [75],=75
  [95, 64],=170
  [17, 47, 82],=217
  [18, 35, 87, 10],=304
  [20, 04, 82, 47, 65],=386
  [19, 01, 23, 75, 03, 34],=461
  [88, 02, 77, 73, 07, 63, 67],=534
  [99, 65, 04, 28, 06, 16, 70, 92],=562
  [41, 41, 26, 56, 83, 40, 80, 70, 33],=645
  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],=692
  [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],=735
  [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],=808
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],=899
  [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],=966
  [04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23],=
]
'''
'''

from itertools import islice 

inp = list(map(int,input().split()))
print(inp)
print(len(inp))

  
# Input list initialization 
Input = inp 

l=[]
for i in range(1,16):
  l.append(i)
print(l)
output=[]
# Using islice 
Inputt = iter(Input) 
output = [list(islice(Inputt, elem)) 
          for elem in l] 
s=0
print(*output)
for i in range(len(output)):
  l=len(output[i])
  c=max(output[i])
  s=s+c
  print(s)

  x=output[i].index(c)
  print(x)
'''
'''
def maxi(x,y):
  if(x>y):
    return (x)
  else:
    return(y)

from itertools import islice 

inp = list(map(int,input().split()))
print(inp)
print(len(inp))

  
# Input list initialization 
Input = inp 

l=[]
for i in range(2,16):
  l.append(i)
print(l)
output=[]
# Using islice 
Inputt = iter(Input) 
output = [list(islice(Inputt, elem)) 
          for elem in l] 
s=0
print(output)
output.reverse() 
print(output)
s=0
i=0
c=0
j=0
li=[]
for i in range(len(output)):
  for j in range(len(output[i])):
    s=s+output[i][j]+output[i][j]
  c=max(output[i])
  j=output[i].index(c)
  c=maxi(output[i][j-1],output[i][j])
  s=s+c
print(s)
'''
'''
  print(c)
  s=s+c
  print('#')
  print(s)
  j=output[i].index(c)
  #print(j)
print(s'''


#Project Euler Problem 18
table = list(map(int,input().split()))
#table = [map(int, s.split()) for s in l]

for row in range(len(table)-1, 0, -1):
    for col in range(0, row):
        table[row-1][col] += max(table[row][col], table[row][col+1])

print (table[0][0])
