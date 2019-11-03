list_of_tuple = [ (1,2,3,4,5), (1,2,3), (4,5,6) ]

def multiplyList(myList):
      result = 1
      for x in myList:
         result = result * x
      return result


l=len(list_of_tuple)
y=0
result2 = 0
while y<l:
  result1=(multiplyList(list_of_tuple[y]))
  result2=result1+result2
  y=y+1
  print(result1)

print(result2)