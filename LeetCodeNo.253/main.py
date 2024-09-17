class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort by meeting start time.
        intervals.sort(key=lambda item: item[0])

        # For each interval,
        #   Check start time against stored end time, if end <= start, meaning we can free a meeting room for current interval. If find such stored end time, overwrite the end time with current meeting's end time. If not, meaning we need a new room for this meeting (append current meeting's end time to the store end times).
        meeting_ends = []
        new_meeting_room = True
        max_room = 1
        for inter in intervals:
            new_meeting_room = True
            this_meeting_start = inter[0]
            for i in range(len(meeting_ends)):
                if meeting_ends[i] <= this_meeting_start:
                    meeting_ends[i] = inter[1]
                    new_meeting_room = False
                    break
            if new_meeting_room:
                meeting_ends.append(inter[1])
                max_room = max(max_room, len(meeting_ends))

        return max_room
