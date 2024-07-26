# 3_4_re.py
import re

# 퀴즈
# 기상청 데이터를 정규표현식을 사용해서 json에서 했던 것처럼 예쁘게 출력하세요
json_text = '[{"code":"11","value":"서울특별시"},{"code":"26","value":"부산광역시"},{"code":"27","value":"대구광역시"},{"code":"28","value":"인천광역시"},{"code":"29","value":"광주광역시"},{"code":"30","value":"대전광역시"},{"code":"31","value":"울산광역시"},{"code":"41","value":"경기도"},{"code":"42","value":"강원도"},{"code":"43","value":"충청북도"},{"code":"44","value":"충청남도"},{"code":"45","value":"전라북도"},{"code":"46","value":"전라남도"},{"code":"47","value":"경상북도"},{"code":"48","value":"경상남도"},{"code":"50","value":"제주특별자치도"}]'

codes = re.findall(r'[0-9]+', json_text)
areas = re.findall(r'[가-힣]+', json_text)
print(codes)
print(areas)

codes = re.findall(r'"code":"([0-9]+)"', json_text)
areas = re.findall(r'"value":"([가-힣]+)"', json_text)
print(codes)
print(areas)

# for i in range(len(codes)):
#     print(codes[i], areas[i])

for code, area in zip(codes, areas):
    print(code, area)

print("--------------------------")

codes_areas = re.findall(r'{"code":"([0-9]+)","value":"([가-힣]+)"}', json_text)

# for item in codes_areas:
#     print(item)

for code, area in codes_areas:
    print(code, area)


