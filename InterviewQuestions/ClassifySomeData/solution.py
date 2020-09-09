"""
k-NN based.
Using priority heap is a bonus.
"""

import heapq
A = (1.0,2.0,3.0)
B = (4.0,5.0)
X = 4.0
K = 2
i = -1
heap = []


"""
Traverse every element in A, B tuples, calc distance with X.
Then append the distance with the lable i to heapq.
"""
# 1st loop: c = A (a tuple), 2nd loop: c = B (a tuple)
for c in A,B:
  i = i + 1 # Identifier A = 0, B = 1.
  
  # datnum is the acture data in A, B tuples.
  for datum in c:
    # If push 10, 1, 8.
     heapq.heappush(heap, ( (X-datum)*(X-datum), i))
     
count_A = 0

"""
For the smallest K distances, check if more than half are from A tuple.
"""
for i in range(K):
  # This fn will pop 1, 8, 10. Regardless of heap, this fn will always pop from the smaller element.
  if heapq.heappop(heap)[1] == 0:
    count_A = count_A + 1
if count_A > K / 2:
  print('class A')
else:
  print('class B')