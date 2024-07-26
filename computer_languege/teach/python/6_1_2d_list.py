# 6_1_2d_list.py
import random

# 퀴즈
# 100보다 작은 난수가 10개 들어있는 리스트를 만드세요
random.seed(99)

a = [random.randrange(100) for _ in range(10)]
b = [random.randrange(100) for _ in range(5)]
c = [random.randrange(100) for _ in range(7)]
print(a)

# 퀴즈
# 2차원 리스트를 출력하세요 (반복문을 2개 사용합니다)
d = [a, b, c]

for i in range(len(d)):
    # print(d[i])
    for j in range(len(d[i])):
        print(d[i][j], end=' ')
    print()
print()

for i in d:
    # print(i)
    for j in i:
        print(j, end=' ')
    print()
print()

# 퀴즈
# 2차원 리스트에 들어있는 int 갯수를 알려주세요
total = 0
for i in d:
    print(len(i))
    total += len(i)

print(total)
print([len(i) for i in d])
print(sum([len(i) for i in d]))

# 퀴즈
# 2차원 리스트에서 가장 큰 숫자를 찾아보세요
print([max(i) for i in d])
print(max([max(i) for i in d]))

# 퀴즈
# 2차원 리스트에서 홀수 합계를 구하세요
for i in d:
    for j in i:
        if j % 2:
            print(j, end=' ')
print()

print([j for i in d for j in i if j % 2])
print(sum([j for i in d for j in i if j % 2]))

import practice

