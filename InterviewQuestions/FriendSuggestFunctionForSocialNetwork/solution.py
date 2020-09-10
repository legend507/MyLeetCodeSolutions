# The key to solve this Q is about data representation.

# Represent friends connections with undirected graph, using Adjacency sets.
from functools import reduce

class Person(object):
  def __init__(self, name):
    self.name = name
    self.friends = set()
  
  def friend(self, other: Person):
    if other not in self.friends:
      self.friends.add(other)
      other.friends.add(self)

  def __repr__(self):
    """
    When I print an instance of this class, this fn is called.
    """
    return self.name

def get_2nd_degree_friends(person: Person):
  """
  Construct a new set from person's all friends' friends.
  """
  # "union" creates a new set from 2 sets.
  # reduce(function, iterable) is a built-in function to call the function on the iterable.
  return reduce(set.union, [f.frients for f in person.friends])

def get_2nd_degree_new_friends(person: Person):
  """
  From all 2nd degree friends, remove already friends and the person himself.
  """
  return get_2nd_degree_friends(person).difference(person.friends).difference(set([person]))

def get_suggested_friends(person: Person):
  candidates = get_2nd_degree_new_friends(person)
  ranked_candidates = []

  for c in candidates:
    # Find the number of common friends between this person and a candidate.
    common_friends_num = len(c.friends.intersection(person.friends))
    ranked_candidates.append((c, common_friends_num))
  
  # Rank candidates based on he and the person's number of shared friends.
  ranked_candidates.sort(key = lambda c:c[1], reverse=True)

  return ranked_candidates

