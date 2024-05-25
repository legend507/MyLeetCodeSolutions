class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_sorted = sorted(g)
        s_sorted = sorted(s)

        s_len = len(s_sorted)
        g_len = len(g_sorted)

        s_sorted_index = 0

        for i in range(g_len):
            # Finds a cookie that can satisfy g_sorted[i]. Existing the loop means found a cookie or reached the end, but didn't find one.
            while s_sorted_index < s_len and g_sorted[i] > s_sorted[s_sorted_index]:
                s_sorted_index += 1
            

            # Runs out of cookie.
            if s_sorted_index == s_len:
                return i
            # Found a cookie. Move to next cookie.
            else:
                s_sorted_index += 1

        return g_len
