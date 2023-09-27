import heapq
 
# initializing list
li = [5, 7, 9, 1, 3]
 
# using heapify to convert list into heap
heapq.heapify(li)
print(li)
print(list(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
