# 4_2_comprehension.py
import random

# 컴프리헨션 : (리스트를 만드는) 한줄짜리 반복문

# a = []
# for i in range(5):
#     a.append(i)

a = [i for i in range(5)]
print(a)

# 퀴즈
# 100보다 작은 난수 10개로 리스트를 만드세요
random.seed(17)

for _ in range(10):
    # print(random.randrange(0, 100, 1))
    # print(random.randrange(0, 100))
    print(random.randrange(100))

b = [random.randrange(100) for _ in range(10)]
print(b)

# 퀴즈
# 리스트에서 홀수만 뽑아서 새로운 리스트를 만드세요
for i in b:
    if i % 2:
        print(i)

c = [i for i in b if i % 2]
print(c)
print(sum(c))




