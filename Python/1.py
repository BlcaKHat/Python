def h(m,n):
  ans = 1
  while (n > 0):
    (ans,n) = (ans*m,n-2) 
  print(ans)
h(6,8)