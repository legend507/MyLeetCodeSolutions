# This question is about find what's in common for the 2 string counting from both head and tail.
# The Q asks me to find the SINGLE diff, otherwise the Q would be very difficult.

# Complexity: O(N)

class Change(object):
  def findSingleDiff(self, a:str, b:str):
    if a == b:
      return ''
    
    lcp = self._findLCP(a, b)
    lcs = self._findLCS(a, b)

    oldStr = a[lcp:len(a) - lcs] # Expect this to be '' for the example below.
    newStr = b[lcp:len(b) - lcs] # Expect this to be '11'.

    return (oldStr, newStr)

  def _findLCP(self, a:str, b:str):
    """ Find longest-common-prefix.
    """
    minLen = min(len(a), len(b))
    for i in range(minLen):
      if a[i] != b[i]:
        # The index for the 1st no matching char.
        return i

    # Didn't find no matching char.
    return minLen
  
  def _findLCS(self, a:str, b:str):
    """ Find longest-common-suffix.
    """
    a_reversed = a[::-1]
    b_reversed = b[::-1]
    return self._findLCP(a_reversed, b_reversed)

if __name__ == '__main__':
  c = Change()
  a = 'aaabb'
  b = 'aaa11bb'

  print(c.findSingleDiff(a, b))