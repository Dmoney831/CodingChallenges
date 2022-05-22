def processLogs(logs, maxSpan):
    
    logs.sort()
    new_logs = []
    for i in logs:
        new_logs.append(i.split())
    # print(new_logs)
    ans = []
    left = 0
    for j in range(1, len(new_logs)):
        x = int(new_logs[j][1]) - int(new_logs[left][1])
        # print(x)
        # print(new_logs[left][0], new_logs[j][0])
        if new_logs[left][0] == new_logs[j][0] and abs(x) <= maxSpan:
            ans.append(new_logs[j][0])
        left += 1
        
    
    return ans



logs = ["99 1 sign-in", "100 10 sign-in", "50 20 sign-in", "100 15 sign-out", "50 26 sign-out", "99 2 sign-out"]
maxSpan = 5
# logs = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "20 80 sign-in", "12 120 sign-out", "20 101 sign-out", "21 110 sign-in"]
# maxSpan = 20
print(processLogs(logs, maxSpan))