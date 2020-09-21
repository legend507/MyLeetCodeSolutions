class NaiveSolution():
  def __init__(self, dic):
    self.dic = dic

  def guessWord(self, path):
    return self.isWord('', path)

  def isWord(self, prefix, path):
    ret = []
    if prefix in self.dic:
      ret.append(prefix)

    # This enumerate is equivalant to for i in range(len(path))
    # The following recursion try all combination of char
    # without changing their order. The length of any combination
    # range from 1 to len(path).
    for i, _ in enumerate(path):
      ret.extend(self.isWord(prefix + path[i], path[i+1:]))
    return ret


if __name__ == '__main__':
  dic = ['google','bah','apple','boba','tea']
  path = 'ghjkoijhghjklkjhgfde'
  NaiveSolution(dic).guessWord(path) #should guess google