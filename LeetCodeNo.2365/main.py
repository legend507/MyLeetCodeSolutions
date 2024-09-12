
# This solves the problem, but too slow.
class Solution_slow:
    def __init__(self) -> None:
        self.wait_counter = {}

    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        # Thoughtrs: use a dict to record each task's waitng days.
        # Traverse the tasks once.

        
        task_done = False
        day_count = 0
        
        for task in tasks:
            task_done = False
            while task_done == False:
                # Never done this type of task before or waiting days = 0.
                if task not in self.wait_counter or self.wait_counter[task] <= 0:
                    print(f'Do task {task}')
                    # -1 to all waiting days in wait_counter.
                    self._wait_counter_decrease_1()
                    self.wait_counter[task] = space
                    task_done = True
                    day_count += 1
                else:
                    # Wait for 1 day.
                    print(f'Break due to {task}')
                    self._wait_counter_decrease_1()
                    day_count += 1
        return day_count
    def _wait_counter_decrease_1(self):
        for key, _ in self.wait_counter.items():
            self.wait_counter[key] -= 1


# Made a bit speed improvement, but still too slow.
class Solution_still_slow:

    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        # Thoughtrs: Use a list to append daily work.
        # When checking, only need to check daily_word[-space:].
        daily_work = []
        for task in tasks:
            task_done = False
            while task_done == False:
                if task in daily_work[-space:]:
                    print(f'Break due to {task}')
                    daily_work.append(None)
                else:
                    print(f'Do {task}')
                    task_done = True
                    daily_work.append(task)
        return len(daily_work)


# Other people's solution, 
class Solution:

    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        next_available_day, days  = {}, 0
        for t in tasks:
            # dict.get(key, default_value) will return default_value if key doesn't exist.

            # For the current task, figure out when is the day that it can be done.
            # If task in the dict, meaning we have to wait. Otherwise we can do it today, therefore days +1.
            days = max(next_available_day.get(t, 0), days + 1)
            next_available_day[t] = days + 1 + space
        return days



s= Solution()
s.taskSchedulerII([1,2,1,2,3,1]
, 3)