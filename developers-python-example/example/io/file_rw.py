#!/usr/bin/python

# mode
#    r: 읽기 모드 
#    w: 쓰기 모드 
#    a: 추가 모드. 파일의 마지막에 내용 추가 
with open('파일명', 'r') as f:
    for line in f:
        print(line)

# 추가 모드 
with open('파일명', 'a') as f:
    for i in range(1, 10):
        f.write(i)

