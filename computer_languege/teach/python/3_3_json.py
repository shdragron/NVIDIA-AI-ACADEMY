# 3_3_json.py
import json
import requests

a = '{"ip": "8.8.8.8"}'
b = json.loads(a)
print(b, type(b))
print(b['ip'])

# 퀴즈
# 딕셔너리를 문자열로 변환하세요
c = json.dumps(b)
print(c, type(c))
# print(c['ip'])            # 에러

# 퀴즈
# 원격에서 수신한 아래 데이터로부터 값만 출력하세요
dt = '''{
   "time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''
t = json.loads(dt)
print(t)
print(t.values())
for k in t:
    print(t[k])
print("-----------------------------------")

# 퀴즈
# 기상청 데이터를 수신해서 지역 이름과 코드만 예쁘게 출력하세요
# 11 서울특별시
# 26 부산광역시
url = "http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt"
response = requests.get(url)
print(response)
print(response.text)

print(type(response.content))               # bytes
text = response.content.decode('utf-8')     # euc-kr
print(text)

items = json.loads(text)
print(items)
print(type(items), len(items))

for i in range(len(items)):
    item = items[i]
    # print(type(item))

    # for k in item:
    #     print(item[k], end=' ')
    # print()

    # print(*item.values())

    print(item['code'], item['value'])

for item in items:
    print(item['code'], item['value'])

# 객체, 문자열
# dumps : 객체 -> 문자열
# loads : 문자열 -> 객체

# save : 파일에 쓰기(영구기억장치)
# load : 메모리 쓰기(임시기억장치)











