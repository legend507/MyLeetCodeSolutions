class Solution:
    # I have to create my own count_occurance fn to find # of appearance of subs in s.
    def count_occurance(self, subs, s):
        count = 0
        s_copy = s
        do = True
        while do:
            found = s_copy.find(subs)
            if found == -1:
                do= False
            else:
                s_copy = s_copy[found+1:]
                count += 1
        return count

    def maximumLength(self, s: str) -> int:
        # Generate all substrings from a string.
        # For every substring, count its occurance in s. Put the substring in qualified_substrings if occurance >=3.
        # Use processed_substrings to avoid re-computation as substrings can contain dups.
        all_substrings = [s[i:j] for i in range(len(s))
                          for j in range(i+1, len(s) + 1) if len(set(s[i:j])) == 1]
        print(all_substrings)
        processed_substrings = []
        qualified_substrings = []
        # print(all_substrings)
        for subs in all_substrings:
            if subs not in processed_substrings:
                processed_substrings.append(subs)
                if self.count_occurance(subs, s) >= 3:
                    qualified_substrings.append(subs)
        qualified_substrings.sort(key=lambda item: len(item), reverse=True)
        print(qualified_substrings)
        return len(qualified_substrings[0]) if qualified_substrings else -1
    

# There is a problem with Python's count fn. The following returns 2 instead of 3.
print('aaaa'.count('aa'))