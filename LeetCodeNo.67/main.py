# 67. Add Binary
# The biary is repsresetend by string.
# Here, using a carry var is key.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_ptr, b_ptr = len(a)-1, len(b)-1

        result = ''
        carry = False

        while a_ptr >= 0 or b_ptr >=0:
            # This is smart, if out of index, then default to 0.
            a_digit = int(a[a_ptr]) if a_ptr >=0 else 0
            b_digit = int(b[b_ptr]) if b_ptr >=0 else 0

            # Scenarios
            # a_digit + b_digit = 0, carry = False
            if a_digit + b_digit == 0 and carry == False:
                result += '0'
                carry = False
            elif a_digit + b_digit == 1 and carry == False:
                result += '1'
                carry = False
            elif a_digit + b_digit == 2 and carry == False:
                result += '0'
                carry = True
            elif a_digit + b_digit == 0 and carry == True:
                result += '1'
                carry = False
            elif a_digit + b_digit == 1 and carry == True:
                result += '0'
                carry = True
            elif a_digit + b_digit == 2 and carry == True:
                result += '1'
                carry = True

            a_ptr -= 1
            b_ptr -= 1

        if carry == True:
            result += '1'

        return result[::-1]

s = Solution()
print(s.addBinary(a = "1010", b = "1011"))