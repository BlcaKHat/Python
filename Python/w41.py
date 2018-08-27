def mystery(l):
     if len(l) < 2:
       return (l)
     else:
       return (mystery(l[1:]) + [l[0]])
res = mystery([17,12,41,28,25])
print(res)