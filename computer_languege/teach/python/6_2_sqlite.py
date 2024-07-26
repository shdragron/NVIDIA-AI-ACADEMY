# 6_2_sqlite.py
import sqlite3


# 퀴즈
# weather.csv 파일을 반환하는 함수를 만드세요
def read_weather():
    f = open("data/weather.csv", "r", encoding="utf-8")

    weather = []
    for row in f:
        # print(row.split(','))
        weather.append(row.split(','))

    f.close()
    return weather


def read_weather_adv():
    with open("data/weather.csv", "r", encoding="utf-8") as f:
        return [row.split(',') for row in f]


def create_table(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = "CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEf TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)"
    cur.execute(query)

    conn.commit()
    conn.close()


def insert_row(row):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    cur.execute(query.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    conn.commit()
    conn.close()


def insert_rows(rows):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'

    for row in rows:
        # cur.execute(query.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        cur.execute(query.format(*row))

    conn.commit()
    conn.close()


def fetch_all(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # for row in cur.execute("SELECT * FROM kma"):
    #     print(row)

    # rows = [row for row in cur.execute("SELECT * FROM kma")]
    rows = list(cur.execute("SELECT * FROM kma"))

    # conn.commit()
    conn.close()

    return rows


# 퀴즈
# city가 '부산'인 모든 레코드를 보여주세요
def search_all(db_path, city):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = 'SELECT * FROM kma WHERE city="{}"'.format(city)
    rows = list(cur.execute(query))

    # conn.commit()
    conn.close()

    return rows


# weather = read_weather()
weather = read_weather_adv()
# print(*weather, sep='\n')

# CRUD: Create Read Update Delete

db_path = "data/weather.sqlite"
# create_table(db_path)

# for row in weather:
#     insert_row(row)

# insert_rows(weather)

# rows = fetch_all(db_path)
rows = search_all(db_path, '부산')
print(*rows, sep='\n')




