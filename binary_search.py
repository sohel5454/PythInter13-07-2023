a = [20,50,43,85,69,47]
target = 85

def binary(a,target):
  left = 0
  right = len(a)+1
  while(left <= right):
    mid = (left+right)//2
    if a[mid] == target:
      return mid
    elif a[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

result = binary(a,target)
print(result)
