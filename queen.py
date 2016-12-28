# coding:utf-8
def queen(n, g):
    if n == 8:
        print g
        return
    for i in range(8):
        g[n] = i
        b = True
        for j in range(n):
            if i == g[j] or i-g[j] == n-j or i-g[j] == j-n:
                b = False
                break
        if b:
            queen(n+1, g)

g = [0]*8
queen(0, g)
