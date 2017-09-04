# You can find the problem from the following link
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Birthday Cake Candles

import sys

def birthdayCakeCandles(n, ar):
    key = max(ar)
    count = ar.count(key)
    return str(count)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
