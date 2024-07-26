# 5_1_for_for.py


# 차원(dimension)

# 퀴즈
# 아래와 같이 출력하세요

# *****
# *****
# *****
# *****

def show_stars(n):
    for j in range(n):
        print("*", end='')
    print()


# for i in range(4):
#     # print("*****")
#
#     # for j in range(5):
#     #     print("*", end='')
#     # print()
#
#     show_stars(n=7)

for i in range(4):
    for j in range(5):
        print("*", end='')
    print()
print()

# for (int i = 0; i < 4; i++) {
#     for (int j = 0; j < 5; j++) {
#         printf("*");
#     }
#     printf("\n");
# }

# 퀴즈
# 아래처럼 출력하세요
# 1번
#   0123
# 0 *---
# 1 **--
# 2 ***-
# 3 ****
for i in range(4):
    for j in range(4):
        if i >= j:
            print("*", end='')
        else:
            print("-", end='')
    print()
print()

# for i in range(4):
#     # if i == 0:
#     #     print("*")          # i+1
#     # elif i == 1:
#     #     print("**")         # i+1
#     # elif i == 2:
#     #     print("***")        # i+1
#     # elif i == 3:
#     #     print("****")       # i+1
#
#     for j in range(i+1):
#         print("*", end='')
#     print()
# print()

# 2번
# ****
# ***
# **
# *

#   0123
# 3 ****
# 2 ***-
# 1 **--
# 0 *---
for i in range(3, -1, -1):
    for j in range(4):
        if i >= j:
            print("*", end='')
        else:
            print("-", end='')
    print()
print()

# for i in range(4):
#     # if i == 0:
#     #     print("****")       # 4-i  i+별=4
#     # elif i == 1:
#     #     print("***")        # 4-i
#     # elif i == 2:
#     #     print("**")         # 4-i
#     # elif i == 3:
#     #     print("*")          # 4-i
#
#     for j in range(4-i):
#         print("*", end='')
#     print()
# print()

# 3번
#    *
#   **
#  ***
# ****
for i in range(4):
    for j in reversed(range(4)):
        if i >= j:
            print("*", end='')
        else:
            print("-", end='')
    print()
print()

# 4번
# ****
#  ***
#   **
#    *
for i in reversed(range(4)):
    for j in reversed(range(4)):
        if i >= j:
            print("*", end='')
        else:
            print("-", end='')
    print()
print()





