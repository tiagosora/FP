
def reapeatNumTimes(n):
   lst = []
   for k in range(0, n + 1):
      a = k
      while a > 0:
         lst.append(k)
         a -= 1
   return lst
