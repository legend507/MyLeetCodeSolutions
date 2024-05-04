class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        def findCoordinate(numRows, now):
            next = [0, 0, 0]
            # Move down. E.g. if numRows = 3, move down when now[1] = 0, 2, 4, ..., if numRows = 4, move down when now[1] = 0, 3, 6, ...
            if now[1] % (numRows - 1) == 0:
                # Move down.
                if now[0] < numRows - 1:
                    next[0] = now[0] + 1
                    next[1] = now[1]
                # At the last, move upper right.
                else:
                    next[0] = now[0] - 1
                    next[1] = now[1] + 1
            else:
                # Move upper right.
                next[0] = now[0] - 1
                next[1] = now[1] + 1

            return next

        # Assign coordinates to each char in s, structured like [[x, y], char].
        now = [0, 0, s[0]]
        idx = []
        idx.append(now)
        for i in range(1, len(s)):
            next = findCoordinate(numRows, now)
            next[2] = s[i]
            now = next
            idx.append(next)
        
        # Sort coordinates. Customized sorting key.
        idx.sort(key = lambda k: (k[0], k[1]))

        # Traverse coordinate list, create result.
        result = ''
        for i in idx:
            result += i[2]

        return result

so = Solution()
s = "PAYPALISHIRING"
numRows = 3

print(so.convert(s, numRows))
