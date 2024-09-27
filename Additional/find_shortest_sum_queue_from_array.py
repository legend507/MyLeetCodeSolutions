# "Question details
# Warm-up question

# Given an array of queues, where pop() is a very expensive operation (e.g. remote network request), find the length of the shortest queue.

# Background
# Let the candidate know they can assume the following

# Queue is a class with methods pop() and empty().
# The Queue class does not provide a size() method.
# The contents of the queue are unsigned integers. This does not affect the warm-up question and is an assumption for the follow-up question.
# It does not matter if the solution destroys the contents of the queues. You don't need to restore the elements of the queues after counting.
# Depending on context (e.g. programming language and candidate level), the interviewer can choose whether to include the assumptions in the question statement or expect the candidate to ask for clarification.

# Common Issues
# How to address frequently asked questions or places where the candidate commonly gets stuck

# Different queues may have significant differences in length. If candidate finds a suboptimal solution, interviewer can try to help candidate realize it is not necessary to go through all elements of the long queues.

# Follow Up Question #1: Lowest sum queue
# Given an array of queues of unsigned integers, where pop() is a very expensive operation, find the queue with the smallest sum, and output the sum."

# Answer
# Look out for these aspects in the candidate’s responses

# Warm-up question

# Each time, pop one element from all queues, until a queue is empty. The empty queue is the shortest.

# The number of pop() calls is n*l, where n is the number of queues and l is the length of the shortest queue. When the queues have different lengths, we do not have to go through all the long queues, thus saving the time calling unnecessary pop()s.

# Follow-up question

# In the worst case, we have to call pop() as many times as the sum of all queue lengths. One example of the worst case is:

# queues[0] = [0,0,0,0,5],
# queues[1] = [0,0,0,0,0,0,8],
# queues[2] = [0,0,0,0,0,2],
# queues[3] = [0,0,0,0,0,0,0,0,0,0,1],
# In cases like this, we must reach the end of all queues to find the queue of the lowest sum. This worst case applies to all possible algorithms.

# For L3 interview, the interviewer could provide this example to the candidate.

# Solution 1:

# Each time, pop one element from all queues, and maintain the partial sum of all queues. Whenever a queue is empty (i.e. we have reached its end), suppose its sum is S, in the future we will never pop from queues whose partial sum is greater than or equal to S.

# This algorithm works well if the lengths of queues vary significantly and the short queues have relatively small sums.

# Solution 2:

# Compute the sum of queues one by one, maintaining a global minimum sum. Whenever processing a queue, if the current sum is greater than or equal to the global minimum, skip the rest of the queue and start to process the next queue.

# Compared to Solution 1, this algorithm works well if the lengths of queues do not differ much, but the number of queues is large, because the space complexity is reduced to O(1), better than the O(n).

# Python
import math

def warm_up_question(queues):
    length = 0
    while True:
      for q in queues:
        if q.empty():
          return l
        q.pop()
      length += 1

def follow_up_question_solution_1(array):
  min_sum=math.inf
  partial_sums = [0]*len(array)
  done = [False]*len(array)
  num_done = 0 # number of True elements in `done`
  while num_done < len(array):
    for i, q in enumerate(array):
      if done[i]:
        continue
      if q.empty():
        min_sum = min(min_sum, partial_sums[i])
      if partial_sums[i] >= min_sum:
        done[i]=True
        num_done+=1
        continue
      partial_sums[i] += q.pop()
  return min_sum

def follow_up_question_solution_2(array):
  min_sum = math.inf
  for i, q in enumerate(array):
    current_sum = 0
    while !q.empty():
      current_sum += q.pop()
      if current_sum >= min_sum:
        break
    min_sum = min(min_sum, current_sum)
  return min_sum
# Rating guidance
# Use rubrics as your primary guidance source. You can supplement the rubric by referring to question-specific guidance below.

# L3
# Programming
# Warm-up question: Candidate comes up with a working solution that attempts to minimize the number of pop() calls as much as possible.

# Follow up question: Candidate has the right idea of not exhausting all the queues.

# Data Structures & Algorithms
# Candidate understands the goal of the problem is to minimize the number of pop() calls.

# Candidate is able to analyze the costs of the algorithm measured by the number of pop() and also the time and space complexity.

# Candidate can identify some cases that would make the number of pop() calls vary, e.g. when given best case and worst case examples, candidate can give correct analysis.

# L4
# Programming
# Candidate comes up with a working solution that minimizes the number of pop() calls for both warm-up and follow-up questions.

# The code is correct and can deal with edge cases such as empty queues, multiple queues having the same length or the same sum.

# Data Structures & Algorithms
# Candidate understands the goal of the problem is to minimize the number of pop() calls.

# Candidate is able to analyze the costs of the algorithm measured by the number of pop() and also the time and space complexity.

# Candidate can identify most common cases that would make the number of pop() calls vary, e.g. finding best case and worst case examples.