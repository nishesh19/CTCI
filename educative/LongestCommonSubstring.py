def find_LCS_length(s1, s2):
    # TODO: Write your code here
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2)] for _ in range(2)]
    maxLength = 0
    for i in range(n2):
        dp[0][i] = 1 if s1[0] == s2[i] else 0

    for i in range(2):
        dp[i][0] = 1 if s2[0] == s1[i] else 0

    for i in range(1, n1):
        for j in range(1, n2):
            if s1[i] == s2[j]:
                dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

            maxLength = max(maxLength, dp[i % 2][j])
    return maxLength
