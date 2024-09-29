# 443. String Compression
# in-place compress

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0

        compressed = []
        current_char = chars[0]
        count = 1
        for i in range(1, n):
            if chars[i] == current_char:
                count += 1
            else:
                compressed.append(current_char)
                if count > 1:
                    for ele in str(count):
                        compressed.append(ele)
                current_char = chars[i]
                count = 1
        # When reach end.
        compressed.append(current_char)
        if count > 1:
            for i in str(count):
                compressed.append(i)
        
        # print(compressed)

        idx = 0
        while idx < len(compressed):
            chars[idx] = compressed[idx]
            idx += 1
        del chars[idx:]

        return len(compressed)

