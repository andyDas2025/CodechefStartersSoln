#https://www.codechef.com/START208D/problems/ALJMP

#Alternate Jumps

T = int(input())
for _ in range(T):
  n = (int(input()))
  
  pad = n
  for i in range(1,n):
    #if i is odd
    if i%2!=0:
      pad = pad - (n-i)
      
    #if i is even
    else:
      pad = pad + (n-i)
  
  print(pad)

