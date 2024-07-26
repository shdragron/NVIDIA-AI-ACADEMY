# 2_2_list.py
import random

#         순서 o       순서 x
#         검색 x       검색 o
# 콜렉션 : 리스트, 튜플, 셋, 딕셔너리
#         list   tuple set dict
#         []     ()    {}  {}

a = [1, 3, 5, 7]
print(a)
print(a[0], a[1], a[2])
print(len(a))

i = 0
while i < 3:
    print(i, a[i])
    i += 1

list.append(a, 9)
a.append(11)
a.insert(0, 99)

# 퀴즈
# 리스트를 거꾸로 출력하세요
print(a[2], a[1], a[0])         # 2 1 0
i = len(a) - 1
while i >= 0:
    print(a[i])
    i -= 1

print(a)

# 퀴즈
# 리스트에서 마지막 요소를 삭제하세요
a.pop(0)
a.pop(5)
a.pop(len(a) - 1)
print(a)

# 퀴즈
# 0 ~ 99 사이의 난수 10개가 들어있는 리스트를 만드세요
random.seed(23)

b = []
i = 0
while i < 10:
    b.append(random.randrange(100))
    # print(random.randrange(100))
    i += 1
print(b)

# c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c = [0] * 10
i = 0
while i < 10:
    c[i] = random.randrange(100)
    # print(random.randrange(100))
    i += 1
print(c)
print(b + c)

# 퀴즈
# 난수 리스트의 합계를 구하세요
# 난수 리스트에 들어있는 홀수 합계와 짝수 합계를 구하세요
odd, even = 0, 0
i = 0
while i < len(c):
    if c[i] % 2:
        odd += c[i]
    else:
        even += c[i]

    i += 1

print("홀수 합계 :", odd)
print("짝수 합계 :", even)






