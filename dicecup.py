N, M = map(int, raw_input().split())

if N <= M:
    i = N + 1
    while i <= (M + 1):
        print i
        i += 1
elif M < N:
    i = M + 1
    while i <= (N + 1):
        print i
        i += 1
