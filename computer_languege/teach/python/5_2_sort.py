# 5_2_sort.py


def twice(n):
    return n * 2


g = lambda n: n * 2

f = twice               # callback
print(twice(7))
print(f(7))
print(g(7), (lambda n: n * 2)(7))


a = [52, 19, 80, 36, 74]
b = sorted(a)
print(b)
print(a)

a.sort(reverse=True)        # in-place
print(a)


def last_digit(n):
    return n % 10


# c = sorted(a, key=last_digit)
c = sorted(a, key=lambda n: n % 10)
print(c)

# 퀴즈
# 문자열 리스트를 내림차순으로 정렬하세요
colors = ["red", "green", "blue", "WHITE", "YELLOW"]

print(sorted(colors, reverse=True))

# 문자열 리스트를 알파벳 순서로 정렬하세요
print(sorted(colors, key=lambda c: c.lower()))

# 문자열 리스트를 길이 순서로 정렬하세요
print(sorted(colors, key=lambda c: len(c)))
print(sorted(colors, key=len))
