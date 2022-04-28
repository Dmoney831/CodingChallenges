# def productFib(prod):
#     ans = [0 for i in range(prod)]
#     ans[1], ans[2] = 1, 1
#     for i in range(3, prod):
#         ans[i] = ans[i-1] + ans[i-2]
#         if ans[i-1] * ans[i] == prod:
#             return [ans[i-1], ans[i], True]
#         if ans[i-1] * ans[i] > prod:
#             return [ans[i-1], ans[i], False]         


def productFib(prod):
    x, y = 0, 1
    while prod > x * y:
      x, y = y, x+y
    return [x, y, prod == x*y]

# 3 5 8 13 21 34 55 