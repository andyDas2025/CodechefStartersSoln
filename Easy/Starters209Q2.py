#https://www.codechef.com/START209D/problems/P2209

#Divisible Duel

T = int(input())
for _ in range(T):
  x,y = list(map(int,input().split()))
  
  Even = []
  Odd = []
  sum_even = sum_odd = 0
  
  for i in range(x,y+1):
    if (i%x == 0):
      if i%2 == 0:
        Even.append(i)
      else:
        Odd.append(i)
      
  sum_even = sum(Even)
  sum_odd = sum(Odd)
  
  if(sum_even >= sum_odd):
    print("YES")
  else:
    print("NO")



