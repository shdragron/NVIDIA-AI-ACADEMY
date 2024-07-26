# 3_1_list.py


def show_me(money=100):     # default parameter
    print(money)


def key_func(a, b, c):
    print(a, b, c)


def test_func(a=0, b=0, c=0):
    print(a, b, c)


def changable(*args):       # 가변인자(갯수, 타입), (여러 개 > 1개) packing
    print(args, *args)      # *: unpacking(1개 > 여러 개)


a = [1, 'abc', 3.14]
print(a)
print(len(a))
print(a[-1], a[len(a)-1])

s = "hello"
print(len(s))
print(s[-1], s[len(s)-1])

# 0 1 2 3 4 -> 0, 5, 1
for i in range(0, 5, 1):    # 시작, 종료, 증감
    print(i, end=' ')
print()

for i in range(0, 5):       # 시작, 종료, 1
    print(i, end=' ')
print()

for i in range(5):          # 0, 종료, 1
    print(i, end=' ')
print()

# 거짓: 0, 0.0, False, None, [], {}
print(show_me(10000))       # None 반환
print(show_me())

help(print)

key_func(1, 2, 3)               # positional argument
key_func(a=1, b=2, c=3)         # keyword argument
key_func(c=3, a=1, b=2)
key_func(1, 2, c=3)
# key_func(a=1, 2, c=3)         # positional은 keyword 앞에만 가능
print()

# 퀴즈
# test_func 함수를 호출하는 5가지 코드를 만드세요
test_func()
test_func(1)
test_func(c=3)
test_func(1, c=3)
test_func(c=3, a=1)
print()

changable()
changable(12)                   # (12,) (12) (3+5)*5
changable(12, "abc")
changable(12, "abc", 3.14)
print()

a, b = 3, 7
c = 2, 8                    # packing
print(c)
print(c[0], c[1])

a, b = c                    # unpacking
print(a, b)
print(*c)                   # unpacking (force)

t = [1, 3, 5]
print(t)
print(*t)

# d, e, f = c               # error


