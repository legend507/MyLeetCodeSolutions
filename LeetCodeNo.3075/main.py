class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total_happiness = 0
        happiness = sorted(happiness)

        for i in range(k):
            current_happinese = happiness[-1] - i 
            if current_happinese < 0:
                current_happinese = 0
            total_happiness += current_happinese
            happiness.pop()

        return total_happiness

    # Too slow, causing time limit exceeded error.
    def maximumHappinessSum_too_slow(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness)

        # Apply this fn to every element in the list after each pick.
        def afterPick(ele: int) -> int:
            if ele > 0:
                ele -= 1
            else:
                ele = 0
            return ele

        total_happiness = 0
        for i in range(k):
            total_happiness += happiness[-1]
            # Remove the largest element in the list.
            happiness.pop()
            happiness = list(map(afterPick, happiness))
        return total_happiness
            