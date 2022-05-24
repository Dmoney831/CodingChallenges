def xx(sentence_list):
    root = {}
    for sentence in sentence_list:
        base = root
        for word in sentence.split(' '):
            if not base.get(word):
                base[word] = {}
            base = base[word]
    return root

# print(xx(["hello world", "hello there"]))

def xxx(nums):
    has_pos = False
    has_neg = False
    for num in nums:
        has_pos = num > 0
        has_neg = num < 0
    return (has_pos, has_neg)

nums = []
# print(xxx(nums))

import queue
import time
import threading
q = queue.Queue()
for i in [3,2,1]:
    def f():
        time.sleep(i)
        q.put(i)
    threading.Thread(target=f).start()
# print(q.get())


f = lambda n: 1 if n <= 1 else n * f(n -1)
g = f(4)
# print(g)

def func(a,b):
    a += 1
    b.append(1)
a, b = 0, []
func(a,b)
print(a,b)

