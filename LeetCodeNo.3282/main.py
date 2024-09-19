class Solution:
    def findPath(self, pos, current_path, all_path, n):
        # Base case: out of bound.
        if pos >= n:
            return

        current_path.append(pos)

        # Base case: reach destination.
        if pos == n-1:
            all_path.append(current_path)
        
        for i in range(pos+1, n):
            self.findPath(i, current_path.copy(), all_path, n)

    def findMaximumScore_tooLarge(self, nums: List[int]) -> int:
        # Thoughts: recursively create all possible ways to move from 0 to n-1.
        # This caused memory limit exceed error.
        n = len(nums)
        all_path = []
        current_path = []
        self.findPath(0, current_path.copy(), all_path, n)

        scores = []
        for path in all_path:
            score = 0
            for i in range(len(path) - 1):
                score += (path[i+1]-path[i]) * nums[path[i]]
            scores.append(score)

        return max(scores) if score else 0
    
    def findMaximumScore(self, nums: List[int]) -> int:
        # Other people's solution.
        # This is more of a math problem than a programming problem.
        # I want to start from a very big number nums[i] and take as many steps as possible (j-i)
        # so that their multiply will be larger.

        # I always want to jump to a bigger nums[j] than current nums[i].
        s=[]
        n=len(nums)
        for i in range(len(nums)-1,-1,-1):
            while s and s[-1][0]<nums[i]:
                s.pop()
            s.append([nums[i],i])
        res=0
        maxind=n-1
        for i in s:
            res+=i[0]*(maxind-i[1])
            maxind=i[1]
        return res