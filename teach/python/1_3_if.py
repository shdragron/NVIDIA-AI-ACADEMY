# 1_3_if.py

# 퀴즈
# 어떤 양수가 홀수인지 짝수인지 알려주세요
a = 13

if a % 2:
    print("홀수")
else:
    print("짝수")

# 퀴즈
# 어떤 양수가 3의 배수인지 5의 배수인지 3과 5의 배수가 아닌지 알려주세요
# (15, 30, 45, ... 입력 금지)
a = 11
if a % 3 == 0:
    print("3의 배수")
elif a % 5 == 0:
    print("5의 배수")
else:
    print("3과 5의 배수 아님")

# 퀴즈
# 앞의 코드에 3과 5 모두의 배수인 경우를 추가하세요
if a % 3 == 0:
    if a % 5 == 0:
        print("3과 5의 배수")
    else:
        print("3의 배수")
elif a % 5 == 0:
    if a % 3 == 0:
        print("3과 5의 배수")
    else:
        print("5의 배수")
else:
    print("3과 5의 배수 아님")

# if a % 3 == 0 and a % 5 == 0:
if a % 15 == 0:
    print("3과 5의 배수")
elif a % 3 == 0:
    print("3의 배수")
elif a % 5 == 0:
    print("5의 배수")
else:
    print("3과 5의 배수 아님")
