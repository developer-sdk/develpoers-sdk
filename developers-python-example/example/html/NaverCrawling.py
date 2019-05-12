#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2019.02.09

@author: hs_seo
'''
import requests
from bs4 import BeautifulSoup

def main():
    html_url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105"
    
    r = requests.get(html_url)
    #bs = BeautifulSoup(r.text, 'html.parser')   # 기본 파서 
    bs = BeautifulSoup(r.text, 'lxml')      # lxml 파서
    #print(bs.prettify()) 
    
    # li 엘리먼트 검색 
    for li in bs.find_all('li'):
        print(li.prettify())
    
    # type06_headline클래스를 가지는 ul엘리먼트를 찾아서 li만 검색 
    ul = bs.find("ul", class_="type06_headline")
    for li in ul.find_all("li"):
        print(li.prettify())

if __name__ == '__main__':
    main()