def wordBreak(s, wordDict):
    word_set = set(wordDict)  # convert list to set for O(1) lookups
    dp = [False] * (len(s) + 1)
    dp[0] = True  # base case: empty string

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # no need to check further

    return dp[len(s)]
