class Solution:
    def arrayRankTransform_tooSlow(self, arr: List[int]) -> List[int]:
        # This should only have the unique elements, ranked ascending.
        rank = list(set(arr))
        rank.sort()

        ret = []
        for ele in arr:
            ret.append(rank.index(ele) + 1)
        return ret
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Editorial solution.
        num_to_rank = {}
        sorted_arr = sorted(arr)
        rank = 1
        for i in range(len(sorted_arr)):
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_to_rank[sorted_arr[i]] = rank
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr