import collections

class Solution:
    def checkInclusion_aBitSlow(self, s1: str, s2: str) -> bool:
        # Generate all possible substr of s2 that has a length = len(s1).
        # Also, the sorted of s1 and this substr must be ==.

        # This worked, but a bit slow. 

        s1_sorted = sorted(s1)
        s1_len = len(s1)

        for i in range(len(s2)):
            sub = s2[i:i+s1_len]
            # print(sub)
            sub_sorted = sorted(sub)
            if sub_sorted == s1_sorted:
                return True
        return False
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Same idea, a bit faster than my own solution.

        ln = len(s1)
        mp1 = collections.Counter(s1)
        print(mp1)
        for i in range(len(s2) - ln + 1):
            sb = s2[i:i+ln]
            if mp1 == collections.Counter(sb):
                return True
        return False
    
test = [1,2,3,4,1,1,1,1]
counter = collections.Counter(test)
print(counter)