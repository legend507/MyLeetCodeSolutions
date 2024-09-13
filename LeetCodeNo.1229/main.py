class Solution:
    def duration_long_enough(self, duration: int, slot: list[int]) -> bool:
        if slot[0] + duration <= slot[1]:
            return True
        return False

    def slots_overlap(self, slot1: list[int], slot2: list[int]) -> None | list[int]:
        if slot1[1] < slot2[0] or slot1[0] > slot2[1]:
            return None
        return [max(slot1[0], slot2[0]), min(slot1[1], slot2[1])]

    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        # To calculate the earliest available slot, I need to order the list by the first element.
        slots1 = sorted(slots1, key=lambda item: item[0], reverse=False)
        slots2 = sorted(slots2, key=lambda item: item[0], reverse=False)
        # To remove slots that too small. This solves the timeout problem.
        slots1_processed = []
        for i in slots1:
            if self.duration_long_enough(duration, i):
                slots1_processed.append(i)
        slots2_processed = []
        for i in slots2:
            if self.duration_long_enough(duration, i):
                slots2_processed.append(i)

        for slot_in_1 in slots1_processed:
            for slot_in_2 in slots2_processed:
                overlap = self.slots_overlap(slot_in_1, slot_in_2)
                if overlap != None:
                    if self.duration_long_enough(duration, overlap):
                        return [overlap[0], overlap[0] + duration]
        return []

s = Solution()
s.minAvailableDuration(
    [[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]],
    [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]],
    456085
)