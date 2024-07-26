# 6_3_songs.py
import requests
import re

# GET : 주소창 사용(보안 취약, 길이 제한)
# POST: 백그라운드 전송(암호화, 대용량, 폼 데이터)


# 퀴즈
# 한국음악저작권협회에서 지드래곤의 노래 목록을 보여주세요
def get_songs(code, page):
    payload = {
        "S_PAGENUMBER": page,
        "S_MB_CD": code,
        # "S_HNAB_GBN": "I",
        # "hanmb_nm": "G-DRAGON",
        # "sort_field": "SORT_PBCTN_DAY",
    }

    url = "https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp"
    response = requests.post(url, data=payload)
    # print(response)
    # print(response.text)

    tbody = re.findall(r"<tbody>(.+?)</tbody>", response.text, re.DOTALL)
    # print(len(tbody))
    # print(tbody[1])

    tr = re.findall(r"<tr>(.+?)</tr>", tbody[1], re.DOTALL)
    # print(len(tr))
    # print(tr[0])

    if len(tr) == 0:
        return False

    for row in tr:
        # row = row.replace(r"<br/>", ",")
        row = re.sub(r"<br/>", ",", row)
        # row = re.sub(r' <img src="/images/common/control.gif"  alt="" />', "", row)
        # row = re.sub(r' <img src="/images/common/control.gif" alt="" />', "", row)
        row = re.sub(r' <img .+? />', "", row)

        td = re.findall(r"<td>(.+?)</td>", row)
        td[0] = td[0].strip()
        print(td)

    return True


# 퀴즈
# 앞에서 만든 코드를 함수로 만드세요(코드, 페이지 번호)
page = 1
while get_songs(code="W0726200", page=page):
    print("------------------", page)
    page += 1


