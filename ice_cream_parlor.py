
t = int(input())
for i in range(t):
    m = int(input())
    n = int(input())
    #c = list()
    cost_list = input()
    c = list(map(int,cost_list.split(' ')))
    for i in range(n):
        if c[i]<m:
            s = m - c[i]
            for j in range(i+1,n):
                if s==c[j]:
                    print(str(i+1)+' '+str(j+1))
                    break
