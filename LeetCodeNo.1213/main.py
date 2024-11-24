class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        # Editorial solution.
        ans = []

        # you can use a dict to count the frequencies
        # or you can use collections.Counter
        # more info is available here:
        # https://docs.python.org/3/library/collections.html

        counter = collections.Counter(
            arr1 + arr2 + arr3
        )  # concatenate them together

        for item in counter:
            if counter[item] == 3:
                ans.append(item)
        return ans