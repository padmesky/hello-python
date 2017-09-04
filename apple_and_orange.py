# You can find the problem from the followin link
# https://www.hackerrank.com/challenges/apple-and-orange/problem
# Apple and Orange

import sys

def calculate_count(arr,point,s,t):
    c = 0;
    for i in range(len(arr)):
        position = arr[i] + point
        if ((position>=s) & (position<=t)):
            c = c + 1
    return str(c)

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
print(calculate_count(apple,a,s,t))
print(calculate_count(orange,b,s,t))

