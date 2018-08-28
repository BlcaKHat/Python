def reverse(l):
     if len(l) < 2:
       return (l)
     else:
       return (reverse(l[1:]) + [l[0]])
res = reverse([17,12,41,28,25])
print(res)
