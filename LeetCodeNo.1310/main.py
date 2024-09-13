class Solution:
    def __init__(self):
        # This solution will timeout without this cache.
        self.cache = {}
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Thought is simply generate a sub_arr based on every query in queries,
        # and calculate xor for every sub_arr.
        ret = []
        for query in queries:
            if tuple(query) in self.cache:
                # print(tuple(query))
                ret.append(self.cache[tuple(query)])
            else:
                left = query[0]
                right = query[1]
                sub_arr = arr[left:right+1]
                result = 0
                for ele in sub_arr:
                    result = result ^ ele
                ret.append(result)
                self.cache[tuple(query)] = result
                # print(tuple(query), self.cache)
        return ret
