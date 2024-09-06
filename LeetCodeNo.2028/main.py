class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        """
        rolls[m] = m known roll values, each 1 ~ 6.
        mean:
        n: missing values

        Returns:
            Any rolls[n] that is possible.
        """
        m = len(rolls)
        total_m = sum(rolls)

        # Corner case: calculate max and min possible when roll[n] are all 6 or 1.
        # If the given mean doesn't fall in [min, max], then not possible
        mean_min = (total_m + 1 * n) / (m+n)
        mean_max = (total_m + 6 * n) / (m+n)
        if mean < mean_min or mean > mean_max:
            return []
        
        # (total_m + total_n) / (m+n) = mean, I need an array whose SUM is total_n.
        total_n = mean * (m + n) - total_m
        
        # To generate this list, 
        divide = total_n // n
        mode = total_n % n
        if mode == 0:
            return [divide for _ in range(n)]
        elif mode + divide > 6:
            # In this case, I need to distribute mode+divide to the other rolls, 1 at a time.
            ret = [divide for _ in range(n)]
            to_distribute = mode
            i = 0
            while to_distribute > 0 and i < n:
                if ret[i] < 6:
                    ret[i] += 1
                    to_distribute -= 1
                else:
                    i += 1
            return ret
        else:
            # Mode + divide <= 6, meaning mode + divide can be a roll.
            ret = [divide for _ in range(n-1)]
            ret.append(mode + divide)
            return ret
        
s = Solution()
ret = s.missingRolls([4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40)
