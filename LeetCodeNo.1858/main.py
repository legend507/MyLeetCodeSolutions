class Solution:
    def all_prefix(self, word):
        # This will cause memory exceed error.
        ret = [word]
        n = len(word)
        for i in range(n, 0, -1):
            ret.append(word[0:i])
        return ret

    def all_prefix_generator(self, word):
        # Changed the fn above to a generator.
        # This solved the memory exceed problem.
        n = len(word)
        for i in range(n, 0, -1):
            yield word[0:i]

    def longestWord(self, words: List[str]) -> str:
        # For each word, find all possible prefixes, 
        # For each prefix, check if it exists in words.
        # If so, put that in ret for further processing.
        ret = []
        for word in words:

            # Use generator, this saves some memory.
            not_answer = False
            for prefix in self.all_prefix_generator(word):
                if prefix not in words:
                    not_answer = True
                    break

            # Use a fn to generate all prefix and put them in a list. This takes too much memory.
            # to_find = self.all_prefix(word)
            # not_answer = False
            # for i in to_find:
            #     if i not in words:
            #         not_answer = True
            #         break
            if not not_answer:
                ret.append(word)
        ret.sort(key=lambda item: len(item), reverse=True)

        if len(ret) == 0:
            return ""

        length = len(ret[0])
        ret2 = []
        for i in ret:
            if len(i) == length:
                ret2.append(i)
        ret2.sort()
        return ret2[0]

    def longestWord_editorial(self, words: List[str]) -> str:
        # Editorial solution.

        # Sort the words lexicographically
        words.sort()

        # Set to store valid words
        valid_words = set()
        longest_valid_word = ""

        # Iterate through each word
        for current_word in words:
            # Check if the word is of length 1 or if its prefix exists in the set. 
            # This only checks current_word[:-1] (e.g. if abcd, then abc).
            # This works since words is sorted.
            if len(current_word) == 1 or current_word[:-1] in valid_words:
                # Add the current word to the set of valid words
                valid_words.add(current_word)

                # Update the longest valid word if necessary
                if len(current_word) > len(longest_valid_word):
                    longest_valid_word = current_word

        # Return the longest valid word found
        return longest_valid_word