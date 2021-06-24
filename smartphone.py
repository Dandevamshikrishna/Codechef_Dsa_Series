n = int(input())
inp = []
for i in range(n):
    inp.append(int(input()))
inp.sort()

def smart(n , inp):
    minm = []
    for j in range(n):
        if minm == None:
            minm = inp[j]*(n-j)
        else:
            minm.append(inp[j]*(n-j))
    
    return max(minm)
print(smart(n, inp))