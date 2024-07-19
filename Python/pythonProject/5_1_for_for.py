# 5_1_for_for.py

# 퀴즈: 아래와 같이 출력하세요.
# *****
# *****
# *****
# *****
def show_stars(n):
    for j in range(n):
        print("*", end= "")
    print()

for i in range( 0, 4 ):
    show_stars(5)

