def EV(N,M,lst):
    dp = [[0 for i in range(M)] for j in range(N)]
    dp[0][0] = lst[0][0]
    for i in range(1, M):
        dp[0][i] = dp[0][i - 1]+lst[0][i]
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0]+lst[i][0]
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = lst[i][j] + max(dp[i - 1][j], dp[i][j - 1])
    mx = dp[N-1][M-1]
    return mx
    

for _ in range(int(input())):
    N , M = map(int,input().split())
    lst = []
    for i in range(N):
        _lst = list(map(int,input().split()))
        lst.append(_lst)
    print(EV(N,M,lst))