# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    

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