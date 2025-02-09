"""
A heap queue or priority queue is a data structure that allows us to quickly access the smallest (min-heap) or 
largest (max-heap) element. A heap is typically implemented as a binary tree, where each parent node’s value is smaller 
(for a min-heap) or larger (for a max-heap) than its children. However, in Python, heaps are usually implemented as min-heaps 
which means the smallest element is always at the root of the tree, making it easy to access.
Heap is a special tree structure in which each parent node is less than or equal to its child node. 
Then it is called a Min Heap. If each parent node is greater than or equal to its child node then it is called a max heap
"""

import heapq

# Creating a Heap
"""
A heap is created by simply using a list of elements with the heapify function and the heapify function rearranges
the elements bringing the smallest element to the first position
"""
  
val = [1, 2, 3, 5, 4]
heapq.heapify(val)
print(val)

h = [10, 20, 15, 30, 40]
heapq.heapify(h)


# heap methods

# Appending an element
  
"""
heapq.heappush() function adds a new element to the heap while maintaining the heap order.
"""
  
heapq.heappush(val, 18)
print(val)  # [1, 2, 3, 5, 4, 18]

heapq.heappush(h, 5)
print(h) # [5, 20, 10, 30, 40, 15] ==> Element 5 is pushed into the heap and after the operation, it gets placed at the root because it is the smallest element.


# heapq.heapify(heaplist)
print("heapify") 
heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 80)

heapq.heapify(heap)
print(heap)


# Remove element from the heap
"""
can remove the element at first index by using this function.
"""
heapq.heappop(val)
print(val) # [2, 4, 3, 5, 18]

min = heapq.heappop(h)
print(h) # [10, 20, 15, 30, 40]
print("smallest: ",min) # 5


# Replace an element
"""
The heap replace function always removes the smallest element of the heap and inserts the new incoming element at some place not fixed by any order.
heapq.heapreplace() function is a combination of pop and push. It pops the smallest element from the heap and inserts a new element into the heap
"""
heapq.heapreplace(val,6)
print(val)


#Appending and Popping Simultaneously
"""
This function allows us to push an element onto the heap and pop the smallest element in one combined operation.
"""

min = heapq.heappushpop(h, 5)

print(min) # 5
print(h) # [10, 20, 15, 30, 40] ==> Element 5 is appended to the heap using heappush(). Then, heappop() is used to remove the smallest element (5), which was just added.

# Merge Operation
"""
heapq.merge() function is used to merge multiple sorted iterables into a single sorted heap. It returns an iterator over the sorted values, which we can then iterate through.
"""

# Creating a heap
h1 = [10, 20, 15, 30, 40]
heapq.heapify(h1)
h2 = [2, 4, 6, 8]
# Merging the lists
h3 = list(heapq.merge(h1, h2))
print("Merged heap:", h3) # Merged heap: [2, 4, 5, 6, 8, 20, 15, 30, 40]



# nlargest() and nsmallest()
"""
heapq.nlargest(n, iterable) returns the n largest elements from the iterable.
heapq.nsmallest(n, iterable) returns the n smallest elements from the iterable.
"""

h = [10, 20, 15, 30, 40]
heapq.heapify(h)

# Find the 3 largest elements
maxi = heapq.nlargest(3, h)
print("3 largest elements:", maxi)

# Find the 3 smallest elements
min = heapq.nsmallest(3, h)
print("3 smallest elements:", min)












