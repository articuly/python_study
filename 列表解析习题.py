# coding:utf-8
lst = [2, 4, -7, 19, -2, -1.45]
outcome = {'python': 89, 'java': 58, 'physics': 65, 'math': 49, 'Chinese': 78}
print([i for i in lst if i < 0])
avg = sum(outcome.values()) / len(outcome)
print(avg)
print({k for k, v in outcome.items() if v > avg})
print([sum(n ** 2 for n in range(1, 100))])
