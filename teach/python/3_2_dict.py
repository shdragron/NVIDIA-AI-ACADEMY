# 3_2_dict.py

# 퀴즈
# 리스트에서 중복된 값들을 모두 삭제하세요
a = [1, 3, 5, 2, 3, 5, 1, 2, 3]
b = set(a)
print(b)
print(list(b))

# map, dict
# 한영 사전: 한글 단어를 찾으면 영어 설명이 나옴
# 한글 단어: key
# 영어 설명: value
#     key    value
d = {'name': 'kim', 'age': 21}      # , 71: 'seven-one'
print(d)
print(d['name'], d['age'])

d['hobby'] = 'climbing'         # add
print(d)

d['hobby'] = 'paragliding'      # update
print(d)

print(d.keys())
print(d.values())
# print(d.keys()[0])            # error
print(d.items())

for k in d.keys():
    print(k, d[k])

for k in d:
    print(k, d[k])

# 퀴즈
# 딕셔너리의 items 함수를 for문에 적용하세요
for kv in d.items():
    print(kv, kv[0], kv[1])

for k, v in d.items():
    print(k, v)
