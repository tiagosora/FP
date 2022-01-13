
def positionOfFirstLargest(arr):
   p = 0
   v = arr[0]
   for n in range(len(arr)):
      if arr[n] > v:
         p = n
         v = arr[n]
   return p
