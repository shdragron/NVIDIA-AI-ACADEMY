# 1_1_basic.py


# 퀴즈
# hello, python!!을 3번 출력하는 코드를 만드세요 (3가지)
print("hello, python!!")
print("hello, python!!")
print("hello, python!!")

print("hello, python!!" "hello, python!!" "hello, python!!" )
print("hello, python!!", "hello, python!!", "hello, python!!" )

print("hello, python!! hello, python!! hello, python!! ")
print()

# 퀴즈
# hello 주변에 작은 따옴표와 큰 따옴표를 출력하세요
print('"hello"', "'hello'")
print('\'hello\'', "\"hello\"")
print()

#    int  float bool  str
print(12, 3.14, True, "coffee")
print(type(12), type(3.14), type(True), type("coffee"))

# print((int) 3.14)
print(int(3.14))
print()

# 퀴즈
# a와 b의 값을 교환하세요
# a = 7
# b = 3
a, b = 7, 3         # int a = 7, b = 3;
print(a, b)

t = a
a = b
b = t
print(a, b)

a, b = b, a
print(a, b)

# alt + 1
# alt + 4
