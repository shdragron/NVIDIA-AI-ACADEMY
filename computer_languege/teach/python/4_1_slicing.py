# 4_1_slicing.py

a = list("abcdefg")
print(a)

print(a[-1])

# 퀴즈
# 앞쪽 절반만 출력하세요
print(a[0:3])               # 시작:종료
print(a[:3])

# 뒤쪽 절반만 출력하세요
print(a[3:7])               # 시작:종료
print(a[3:])

# 퀴즈
# 짝수 번째만 출력하세요
print(a[0:7:2])
print(a[::2])

# 홀수 번째만 출력하세요
print(a[1:7:2])
print(a[1::2])

# 퀴즈
# 리스트를 거꾸로 출력하세요
print(a[2:3])
print(a[2:2])
print(a[6:0:-1])
print(a[6:-1:-1])
print(a[-1:-1:-1])
print(a[::-1])      # 증감(양수: 정방향, 음수: 역방향)

for i in range(len(a)):
    print(a[i], end=' ')
print()

for i in reversed(range(len(a))):
    print(a[i], end=' ')
print()

for i in a:
    print(i, end=' ')
print()

for i in reversed(a):
    print(i, end=' ')
print()

for i, v in enumerate(a):
    print(i, v)
print()

