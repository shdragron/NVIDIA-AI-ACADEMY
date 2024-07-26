# 2_5_open_hangul.py
import re
import requests


# API : Application Programming Interface
#       함수 이름                         매개변수
# http://openhangul.com/nlp_ko2en   ?    q=파이썬
# https://www.google.com/search     ?    q=%EC%98%A4%ED%94%88%ED%95%9C%EA%B8%80&oq=%EC%98%A4%ED%94%88%ED%95%9C%EA%B8%80&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIKCAEQABiABBiiBDIKCAIQABiABBiiBDIKCAMQABiABBiiBDIKCAQQABiABBiiBKgCCLACAQ&sourceid=chrome&ie=UTF-8

# 퀴즈
# 오픈한글 "한글->알파벳" 메뉴를 사용해서
# 한글을 영어로 변환하는 함수를 만드세요
def hangul_to_english(hangul):
    url = "http://openhangul.com/nlp_ko2en?q=" + hangul
    response = requests.get(url)
    # print(response)
    # print(response.text)

    # pattern = r'<img src="images/cursor.gif"><br>([A-Za-z]+)'
    pattern = r'<img src="images/cursor.gif"><br>(.+)'
    result = re.findall(pattern, response.text)
    # print(result[0])
    # print(result)
    return result[0]


print("스쿠터 :", hangul_to_english("스쿠터"))
print("파이썬 :", hangul_to_english("파이썬"))
print("바닷가 :", hangul_to_english("바닷가"))
print("바닷가... :", hangul_to_english("바닷가에서 스쿠터를 타면서 파이썬을 공부해 보자"))

