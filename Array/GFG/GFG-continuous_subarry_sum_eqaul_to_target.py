"""In GFG this problem is named as - Indexes of Subarray Sum"""
#   https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&category=Searching&sortBy

val = [1, 2, 3, 7, 5]
target = 12
o/p: [2,4] #return the starting index and end

"""Brute Force Approach"""
result = []
found = 0
for i in range(len(val)):
    current_sum = 0
    for j in range(i, len(val)):
        current_sum += val[j]
        if current_sum == target:
            result.append(i+1)
            result.append(j+1)
            found = 1
            break
    if found:
        break
print(result)


"""Optimized Approach"""
left = found = 0
current_sum = 0
result = []
for right in range(len(val)):
    current_sum += val[right]
    while current_sum > target and left <= right:
        current_sum -= val[left]
        left += 1
    if current_sum == target:
        result.append(left+1)
        result.append(right+1)
        found = 1
        break
if found:
    print(result)
else:
    print([-1])
