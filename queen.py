# coding:utf-8
import time

def queen(n, dim, g, total):
    if n == dim:
        total[0] += 1
        # print g
        return 1
    '''g[0], g[1], g[2]...g[n-1]'''
    for i in range(dim):
        g[n] = i
        b = True
        for j in range(n):
            if i == g[j] or i-g[j] == n-j or i-g[j] == j-n:
                b = False
                break
        if b:
            queen(n+1, dim, g, total)

def queen1(n, dim, g, total):
    if n == dim:
        total[0] += 1
        # print g
        return 1
    '''g[0], g[1], g[2]...g[n-1]'''
    temp = 0
    des = range(dim)
    while temp < n:
        des.remove(g[temp])
        temp += 1
    temp = 0
    while temp < n:
        if g[temp]+n-temp in des:
            des.remove(g[temp]+n-temp)
        if g[temp]-n+temp in des:
            des.remove(g[temp]-n+temp)
        temp += 1

    for i in des:
        g[n] = i
        queen1(n+1, dim, g, total)
dim = 12
g = [0]*dim
total = [0]
t1 = time.time()
queen1(0, dim, g, total)
t2 = time.time()
print total, t2-t1
total = [0]
queen(0, dim, g, total)
t3 = time.time()
print total, t3-t2
