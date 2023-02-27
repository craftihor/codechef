n, k = map(int, input().split())
a = [0] * n
for i in range(k):
    r, c = map(int, input().split())
    for j in range(r - 1, n):
        a[j] += c
        if j - r >= 0:
            a[j] -= c

print(max(a))
