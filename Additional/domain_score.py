# You are given a list of domain names and an integer "score" for each of them. A domain is a "leaf" if it doesn't have any child domains in the input. A leaf domain's "total score" is the sum of the scores of itself and all its ancestor domains.

# Write a program that, given a list of domains and their scores, outputs a list of leaf domains with their respective total scores.

# Example input:

# test.mydomain.com       10
# mail.test.mydomain.com  15
# test.com               -10
# com                     20
# mydomain.com             5
# www.mydomain.com        10
# mail.test.com           10
# www.test.com            -5
# Example output:

# mail.test.mydomain.com      50          // (20 + 5 + 10 + 15)
# www.mydomain.com            35          // (10 + 5 + 20)
# mail.test.com               20          // (10 - 10 + 20)
# www.test.com                 5          // (-5 - 10 + 20)

from sys import stdin
from collections import defaultdict


def calculate_total_scores(domain, score, tree, scores):
  if not tree[domain]:  # leaf domain
    print(domain, score + scores[domain])
    return
  for child in tree[domain]:
    calculate_total_scores(child + '.' + domain, score + scores[domain],
                           tree, scores)


def main():
  tree = defaultdict(set)
  scores = defaultdict(int)
  for line in stdin:
    domain, score = (x.strip() for x in line.split())
    scores[domain] = int(score)
    while True:
      child, _, domain = domain.partition('.')
      if not domain:
        break
      tree[domain].add(child)

  for domain in set(tree):
    if '.' not in domain:  # root domain
      calculate_total_scores(domain, 0, tree, scores)


if __name__ == '__main__':
  main()