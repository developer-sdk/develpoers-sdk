from bs4 import BeautifulSoup

html_doc = """<html>
                <head>
                    <title>The Dormouse's story</title>
                </head>
                <body>
                    <!-- Comment --> 
                    <p class="title" id="p_1">
                        <b>The Dormouse's story</b>
                    </p>
                    middle data - navigable string
                    <p class="story" id="p_2">
                        Once upon a time there were three little sisters; and their names were
                        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                        <a href="http://example.com/tillie" class="sister" id="link3" data-type="sample">Tillie</a>;
                        and they lived at the bottom of a well.
                    </p>
                    <p class="description" id="p_3">
                        ...
                    </p>
                </body>
            </html>
"""

# BS의 파서는 lxml을 가장 추천한다고 함 
soup = BeautifulSoup(html_doc, 'lxml')

# find_all을 이용할 때는 정규식, 람다식 이용 가능
# <p> 태그 찾기
for p in soup.find_all("p"):
    print(p)

# id를 이용하여 <p> 태그 찾기, 1개만 찾도록 지정
for p in soup.find_all("p", id="p_3", limit=1):
    print(p)

# class를 이용하여 <p> 태그 찾기
for p in soup.find_all("p", class_="story"):
    print(p)

# id, class를 모두 이용하여 <p> 태그 찾기
for p in soup.find_all("p", id="p_2", class_="story"):
    print(p)

# 기호가 들어간 애트리뷰트를 이용해서 <p> 태그 찾기 
for p in soup.find_all("p", attrs={"data-type": "sample"}):
    print(p)


# 태그 이름으로 검색
print(soup.body.p.b)

# children은 Tag 객체의 요소
# 자식에 대한 정보를 모두 가지고 있음
for item in soup.body.children:
    print(item)

# Tag 객체의 데이터
for a in soup.find_all("a"):
    print(a)    # a 객체 출력
    print(a.name)   # 객체명: a
    print(a.text)   # 객체내 내용: Lacie
    print(a.has_attr("href"))   # href 애트리뷰틑를 가지고 있나? : True
    print(a["href"])    # href의 값: http://example.com/lacie
    print(a.attrs)  # 애트리뷰트 전체: {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
