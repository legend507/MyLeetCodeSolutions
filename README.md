# MyLeetCodeSolutions
To enhance my coding ability. 

# How to approach a difficult problem?

1. Before write any code, write down thoughts while explaining this to the interviewer.
2. If one way doesn't work (e.g. I attempted DP for No.739), change a way of thinking.

# Common techniques

- Stack, pop / append. Use this in a for loop to compare the current value to the Stack top.
- Priority queue

# Userful snippets

```python
# Concat all element in a list of int to string, also can specify separator.
# Here, the str is str(), that converts int to string.
''.join(map(str, encoded_str))
```

```python
# Sort a dict by key (desc order)
poly1_dict_ordered = dict(sorted(poly1_dict.items(), key=lambda item: item[0], reverse=True))
```

```python
# Create a matrix of m x n.
matrix = [[-1] * n for _ in range(m)]
```

```python
# Dict, get the value of the max key in a dict.
d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}
print(max(d, key=d.get))
```

No.1242, multi-thread example.

```python
# List, find the index of a value.
[1,2,3].index(2) # => 1
[1,2,3].index(4) # => ValueError
```

```python
# Get all distinct char from a string, order them, then join them into another string.
word_distinct_sorted = ''.join(sorted(list(set(word))))
```

Whey using Python dict, and worry about if a certain key exists or not, use `dict.get(key, default_value)`!

```python
# Generate all possible substrings from a string s.
all_substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)]
```

```python
# Assign a var to negative inf.
ret = float('-inf')
```

LeetCodeNo.179, how to define a customized comparison function for sort.

```python
# Example of removing duplicates from a list of lists. Need to use numpy.
# ret is the list of lists.
np.unique(np.array(ret), axis=0).tolist()
```

```python
# Reverse a string.
reversed_string = str[::-1]  # Reverse the string
```

```python
# Split a string based on multiple deliminators, e.g. +, -, /.
# Note that \ may be needed depending on what deliminiator it is.
import re
split_str = re.split('\+|\-|\/', str)
```

```python
# Python has math lib to calculate Greatest Common Divisor and Least Common Multiple.
import math
math.gcd(4, 6) # Gives 2.
math.lcm(2, 3) # Gives 6.
```

```python
# Deal with index out of bound problem.
# a is a string, this logic is in a loop. I want to assign a default value 0 when a_ptr reaches out of bound.
a_char = a[a_ptr] if a_ptr >=0 else 0
a_ptr -= 1
```

```python
# List index.
nodes = [i for i in range(10)]
print(nodes[0:4]) # [0, 1, 2, 3], namely nodes[0] to nodes[3]
print(nodes[4:9]) # [4, 5, 6, 7, 8], note that node[9] is NOT included.
print(nodes[4:100]) # [4, 5, 6, 7, 8, 9], note not of bound index will be ignored.
print(nodes[-1:5]) # [], noting is printed.
```

```python
# Python string, find start idx of all occurance of a substring.
string = "hello world, hello again!"
substring = "hello"

matches = []
start = 0

while True:
    start = string.find(substring, start)
    if start == -1:
        break
    matches.append(start)
    start += len(substring)

print(matches)
```

```python
# Python insert into list at idx.
# In-place insert, the memory address of nums won't change.
nums.insert(idx, value)
```

```python
# Use Counte to count the occurance of elements. The input can be a list or a string.
test = [1,2,3,4,1,1,1,1]
counter = collections.Counter(test)
print(counter) # Counter({1: 5, 2: 1, 3: 1, 4: 1})
```

```python
# Given 2 lists, monsters and coins of equal length, sort them into a list of (one_monster, one_coin) based on coin.
monster_and_coin = sorted(zip(monsters, coins), key=lambda x: x[0])
```

```python
# Usage of heapq.
# Note that heapq by default is min_heap, meaning
# the elements will be ordered ascending.
# If I want a max_heap, simply modify the element by adding
# '-' sign to it when push.

min_heap = []
# Add an element to min_heap.
heapq.heappush(min_heap, element)
# Pop the smallest element in the heap.
min_element = heapq.heappop(min_heap)
```

```python
# String split each char.
# num is an int, I want a list with each digit as a char.
num_str = [i for i in str(num)]
```

```python
# Generate all subsets of a list recursively.
nums = [1,2,3]
all_subsets = []
def backtrack(start, current_subset):
    all_subsets.append(current_subset)
    for i in range(start, len(nums)):
        current_subset.append(nums[i])
        backtrack(i + 1, current_subset)
        current_subset.pop()

backtrack(0, [])
```