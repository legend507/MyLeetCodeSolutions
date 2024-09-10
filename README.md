# MyLeetCodeSolutions
To enhance my coding ability. 

# How to approach a difficult problem?

1. Before write any code, write down thoughts while explaining this to the interviewer.
2. If one way doesn't work (e.g. I attempted DP for No.739), change a way of thinking.

# Common techniques

- Stack, pop / append. Use this in a for loop to compare the current value to the Stack top.
- Priority queue

# Userful snippets

```
# Concat all element in a list of int to string, also can specify separator.
''.join(map(str, encoded_str))
```

```
# Sort a dict by key (desc order)
poly1_dict_ordered = dict(sorted(poly1_dict.items(), key=lambda item: item[0], reverse=True))
```

```
# Create a matrix of m x n.
matrix = [[-1] * n for _ in range(m)]
```

```
# Dict, get the value of the max key in a dict.
d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}
print(max(d, key=d.get))
```

No.1242, multi-thread example.

```
# List, find the index of a value.
[1,2,3].index(2) # => 1
[1,2,3].index(4) # => ValueError
```