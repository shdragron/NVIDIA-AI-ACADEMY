# 4_5_csv.py
import csv


# 퀴즈
# weather.csv 파일을 읽고, 예쁘게 출력하는 함수를 만드세요
# 서울ㆍ인천ㆍ경기도::서울::A02::2024-07-22 00:00::흐리고 비::25::31::80
def show_csv():
    f = open("data/weather.csv", "r", encoding="utf-8")

    # for line in f.readlines():
    # for line in f:
    #     # print(line.strip())
    #     # print(line.strip().split(","))
    #     print("::".join(line.strip().split(",")))

    for line in csv.reader(f):
        print(line)

    f.close()


# 퀴즈
# us-500.csv 파일을 리스트 형태로 함수로 만들어서 출력하세요
def show_us500():
    f = open("data/us-500.csv", "r", encoding="utf-8")

    for line in csv.reader(f):
        print(line)

    f.close()


def write_csv():
    f1 = open("data/weather.csv", "r", encoding="utf-8")
    f2 = open("data/weather_copy.csv", "w", encoding="utf-8", newline="")

    rows = []
    for line in csv.reader(f1):
        rows.append(line)

    csv.writer(f2, delimiter=',', quoting=csv.QUOTE_ALL).writerows(rows)

    f1.close()
    f2.close()


# show_csv()
# show_us500()
write_csv()
