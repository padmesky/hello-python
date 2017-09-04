# you can find the problem from following link
# https://www.hackerrank.com/challenges/mini-max-sum/problem
# Mini-max Sum

number_list = input()
c = list(map(int,number_list.split(' ')))
x = sum(c)
print (str(x-max(c))+' '+str(x-min(c)))
