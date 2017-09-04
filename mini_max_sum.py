# you can find the problem from following link
# https://www.hackerrank.com/challenges/mini-max-sum/problem
# Mini-max Sum

number_list = input()
c = list(map(int,number_list.split(' ')))
#sort first
c.sort()
#sum of first 4 is min
n = len(c)
max = 0
min = 0
for i in range(4):
    min = min + c[i]
    max = max + c[(n-1)-i]
print(str(min)+'  '+str(max))
