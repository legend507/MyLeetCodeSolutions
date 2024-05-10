class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score, reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        # 1, 2, 3 map to medals, everything else to string.
        rank_mapping = {score: medals[i] if i < 3 else str(i + 1) for i, score in enumerate(rank)}
        return [rank_mapping[i] for i in score]