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
