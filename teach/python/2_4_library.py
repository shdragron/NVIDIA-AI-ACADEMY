# 2_4_library.py
import re
import requests

url = "http://211.251.214.176:8800/index.php?room_no=2"
response = requests.get(url)
print(response)
print(response.text)

empty = re.findall(r'([0-9]+) 석</td>', response.text)
print("빈 좌석 갯수 :", empty[5])

# 퀴즈
# 흥덕 도서관 노트북실의 빈 좌석 번호를 알려주세요
print(re.findall(r'<font style="color:green;font-size:13pt;font-family:Arial"><b>([0-9]+)</b></font>', response.text))

