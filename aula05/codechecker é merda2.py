
def removeAdjacentDuplicates(s):
   t = ""
   s = list(s)
   for n in range(-len(s), 0):
      m = n + 1
      if s[n] == s[m]:
         s[n] = ""
   s = t.join(s)
   return s
