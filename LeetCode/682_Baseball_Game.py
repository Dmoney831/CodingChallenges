# + -> is the sum of the previous two scores.
# D -> *2 the previous score
# C -> remove previous socre

# def calPoints(ops):
#     score = []
#     for i in ops:
#         if i == "C":
#             score.pop()
#         elif i == "D":
#             a = score[-1]
#             score.append(a*2)
#         elif i == "+":
#             score.append(score[-1] + score[-2])
#         else:
#             score.append(int(i))
#     return sum(score)

def calPoints(ops):
    score = []
    for i in ops:
        if i == "C":
            score.pop()
        elif i == "D":
            a = score[-1]
            score.append(a*2)
        elif i == "+":
            score.append(score[-1]+score[-2])
        else:
            score.append(int(i))
    return sum(score)

ops = ["5","2","C","D","+"]
# Output: 30
ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
print(calPoints(ops))