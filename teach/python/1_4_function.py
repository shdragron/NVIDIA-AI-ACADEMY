# 1_4_function.py


# 매개변수 없고, 반환값 없고.
def f_1():
    print("f_1")


# 매개변수 있고, 반환값 없고.
# 퀴즈
# 매개변수 2개를 받아서 덧셈을 하는 함수를 만드세요 (결과는 화면 출력)
def f_2(a, b):
    print(a + b)


# 매개변수 없고, 반환값 있고.
def f_3():
    return 3, 7


# 매개변수 있고, 반환값 있고.
# 퀴즈
# 2개의 정수로부터 큰 값을 찾는 함수를 만드세요
def max_2(a, b):
    return a if a > b else b
    # if a > b:
    #     return a
    #
    # return b


# 퀴즈
# 4개의 정수로부터 큰 값을 찾는 함수를 만드세요 (2가지 코드)
def max_4(a, b, c, d):
    # 1번
    # if a > b and b > c and c > d:
    # if a >= b and a >= c and a >= d: d = a
    # if b >= a and b >= c and b >= d: d = b
    # if c >= a and c >= b and c >= d: d = c
    #
    # return d

    # 2번
    # if a < b: a = b
    # if a < c: a = c
    # if a < d: a = d
    # return a

    # 퀴즈
    # max_2를 사용해서 문제를 해결하세요 (2가지 코드)
    # 복면가왕
    # return max_2(max_2(a, b), max_2(c, d))

    # 한국시리즈
    return max_2(max_2(max_2(a, b), c), d)


f_1()

f_2(3, 5)
f_2("hello", "python")

a, b = f_3()
print(a, b)

c = f_3()
print(c)

print(max_4(1, 3, 5, 7))
print(max_4(3, 5, 7, 1))
print(max_4(5, 7, 1, 3))
print(max_4(7, 1, 3, 5))


