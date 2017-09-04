# You can find the problem from the following link
# https://www.hackerrank.com/challenges/big-sorting/problem
# Big Sorting

import sys

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
# your code goes here
unsorted.sort(key=int)
for i in unsorted:
    print(i)

