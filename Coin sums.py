coins = [1, 2, 5, 10, 20, 50, 100, 200]
aim = int(input("Enter the total value needed to be calculated : "))
l=[1] + [0]*aim
for i in coins:
  for j in range(i,aim+1):
    if (j  >= i):
      l[j] = l[j] + l[j-i]
print(l)
    
