# 2_3_re.py
import re           # regular expression

# .  []
# ?  *  +

# 3, 34, 341, 3412
db = """3412    [|Bob|] 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534"""

# print(db)

# r: raw string
print(re.findall(r'[0-9]', db))
print(re.findall(r'[0-9]+', db))

# 퀴즈
# 직원 이름들을 찾아주세요
print(re.findall(r'[A-z]+', db))        # wrong
print(re.findall(r'[A-Za-z]+', db))     # just
print(re.findall(r'[A-Z][a-z]+', db))   # good

# 퀴즈
# T로 시작하는 이름만 찾아보세요
# T로 시작하지 않는 이름만 찾아보세요
print(re.findall(r'T[a-z]+', db))
print(re.findall(r'[^T][a-z]+', db))
print(re.findall(r'[ABCDEFGHIJKLMNOPQRSUVWXYZ][a-z]+', db))
print(re.findall(r'[A-SU-Z][a-z]+', db))
