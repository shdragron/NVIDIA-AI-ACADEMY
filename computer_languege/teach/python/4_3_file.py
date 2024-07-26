# 4_3_file.py


def read_1(file_path):
    f = open(file_path, 'r', encoding='utf-8')

    poem = f.read()
    print(poem)

    # 퀴즈
    # 파일에 포함된 개행문자의 갯수를 알려주세요
    s = 0
    for c in poem:
        if c == '\n':
            print(True)
            s += 1

    newlines = [True for c in poem if c == '\n']
    print(newlines, len(newlines))

    rows = poem.split('\n')
    print(rows)
    print(len(rows))
    print(*rows, sep='\n')

    print('\n'.join(rows))

    f.close()


def read_2(file_path):
    f = open(file_path, 'r', encoding='utf-8')

    # poem = f.read(10)
    # print(poem)

    lines = f.readlines()
    print(lines)

    for line in lines:
        print(line.strip())

    f.close()


def read_3(file_path):
    f = open(file_path, 'r', encoding='utf-8')

    while True:
        line = f.readline()

        # if not line:
        if len(line) == 0:
            break

        print(line)

    f.close()


def write():
    f = open("data/sample.txt", "w", encoding="utf-8")

    f.write("아프니까 청춘이다")
    f.write("\n");
    f.write("나이든 사람도 아프다")

    f.close()


# file_path = "C:\Users\Harmony00\Desktop\python\data\poem.txt"
file_path = "data/poem.txt"

read_1(file_path)

s = "{} {:.5f} {} {}".format(12, 3.14, "rain", True)    # sprintf
print(s)

read_2(file_path)

t = """

\t\t\t   hello world   \t\t\t

"""
print("[{}]".format(t))
print("[{}]".format(t.strip()))     # trim

read_3(file_path)

write()
