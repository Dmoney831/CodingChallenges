def wordBreak(s, wordDict):
    dp = [True] + [False]*len(s)
    for i in range(1, len(s)+1):
        for word in wordDict:
            if dp[i - len(word)] and s[:i].endswith(word):
                dp[i] = True
    return dp[-1]



s = "leetcode" 
wordDict = ["leet","code"]
s = "applepenapple" 
wordDict = ["apple","pen"]
s = "catsandog" 
wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s, wordDict))