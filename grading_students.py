# You can find the problem from te following link
# https://www.hackerrank.com/challenges/grading/problem
# Grading Students

import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        if grades[i]>= 38:
            dif = 5 - (grades[i]%5)
            if dif<3:
                grades[i] = grades[i] + dif
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
