# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Searching&sortBy

val = [1]
n = len(val) + 1
total = (n * (n+1)) // 2
print(total-sum(val))
