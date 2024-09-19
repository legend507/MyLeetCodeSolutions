class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each str in strs, split str into single char and order by asc.
        # Then concate the single chars into a key, the value is the index in strs.
        # Use a dict to store the key-value.

        # Corner case.
        n = len(strs)
        if n <= 1:
            return [strs]

        record = {}
        for i in range(n):
            # Split the str in to single char, recorder them, then concate them as a key.
            sorted_char = sorted(list(strs[i]))
            key = ''.join(sorted_char)
            if key in record:
                record[key].append(i)
            else:
                record[key] = [i]
        # print(record)
        ret = []
        for key, item in record.items():
            one_ret = []
            for i in item:
                one_ret.append(strs[i])
            ret.append(one_ret)
        return ret
