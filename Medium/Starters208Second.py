#https://www.codechef.com/START208D/problems/SBTG

#Sabotage


T = int(input())
for _ in range(T):
  n,x,k = list(map(int,input().split()))
  A = list(map(int,input().split()))
  
  
  count = 0
  for ele in A:
    if ele > x:
      count += 1
  
  rank = count + 1
  
  B = list(A)
  if k == 0:
    print(rank)
  else:
    B.sort(reverse=True)
    
    
    for i in range(k):
      x = x + 100
      B[i] = 0
      
    B.append(x)
    B.sort(reverse=True)
    
    print(B.index(x)+1)
    
    
    