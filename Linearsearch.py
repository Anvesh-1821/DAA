def linearsearch(arr,n,key):
  for i in range(n):
    if arr[i]==key:
      return i
  return -1
arr=[10,20,30,40,50]
key=20
n=len(arr)
print("linear search:",linearsearch(arr,n,key))
