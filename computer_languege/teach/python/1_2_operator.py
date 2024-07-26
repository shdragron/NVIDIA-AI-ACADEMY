# 1_2_operator.py

# 연산 : 산술, 관계, 논리, 비트
# 산술 : +  -  *  /  %  **  //
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)        # 나눗셈(실수)
print(7 % 3)        # 나머지
print(7 ** 3)       # 지수(거듭제곱)
print(7 // 3)       # 몫, 나눗셈(정수)

# 퀴즈
# 0 ~ 999 사이의 양수의 자릿수 합계를 알려주세요
a = 123     # 6
print('합계 :', a // 100 + a // 10 % 10 + a % 10)

s = 0
s += a % 10
a //= 10        # a = 12

s += a % 10
a //= 10        # a = 1

s += a % 10
a //= 10        # a = 0

# if a > 0:
#     s += a % 10
#     a //= 10        # a = 12

# 퀴즈
# 양수의 자릿수 합계를 구하세요
# a =1234567
# while a > 0:
#     s += a % 10
#     a //= 10        # a = 12

print('합계 :', s)

# 퀴즈
# 입력한 양수보다 크거나 같은 첫 번째 5의 배수를 구하세요
# 15 -> 15
# 13 -> 15
# b = input('양수 입력 : ')
# b = int(b)
b = 15

c = (b + 4) // 5 * 5  # 16 -> 20, 17 -> 21, 18 -> 22, 19 -> 23, 20 -> 24
print(c)
print()
# 0 1 2 3 4 5 6 7 8 9 ... 20 21 22 23 24

# 관계 : >  >=  <  <=  ==  !=
print(7 > 3)
print(7 >= 3)
print(7 < 3)
print(7 <= 3)
print(7 == 3)
print(7 != 3)
print()

# 퀴즈
# age가 10대인지 알려주세요
age = 13
print(10 <= age <= 19)
print((age >= 10) * (age <= 19))
print()

# 논리 : and  or  not
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

print('hello' + 'python')
# print('hello' - 'python')     # error
print('hello' * 3)
print('-' * 30, end='')

print(len('hello'))

