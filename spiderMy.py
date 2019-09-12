#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import html
from bs4 import BeautifulSoup

outputFile = open('express_name.txt','r+')

url = "http://www.radio366.com/fenlei.asp?fenlei=waiyu"
response = urllib.request.urlopen(url)
web = response.read()         # 获取到页面的源代码
# print(html.decode('utf-8'))    # 转化为 utf-8 编码
soup = BeautifulSoup(web, 'html.parser', from_encoding='utf8')

# print(soup.prettify())
# print(soup.title)
# print(type(soup.find_all('a')))
# all_line = soup.div('column-1 column-list')
# all_a = all_line.find_all('a')
# all_a = soup.div('column-1 column-list').find_all('a')
all_a1 = soup.find('div', class_="content").find_all('a')

delTail = ['速递', '速运', '快递', '快运', '物流', '货运']
for ii in range(0, len(all_a1)):
    line = all_a1[ii].text
    for tail in delTail:
        if line.endswith(tail):
            line = line.replace(tail, '')
    if '（' in line:
        lineTail = line.index('（')
        line = line[:lineTail]
    if ' ' in line:
        lineTail = line.index(' ')
        line = line[:lineTail]
    outputFile.write(line + '\n')

# all_a2 = soup.find('div', class_="column-2 column-list").find_all('a')
# for ii in range(0, len(all_a2)):
#     line = all_a2[ii].text
#     for tail in delTail:
#         if line.endswith(tail):
#             line = line.replace(tail, '')
#     if '（' in line:
#         lineTail = line.index('（')
#         line = line[:lineTail]
#     if ' ' in line:
#         lineTail = line.index(' ')
#         line = line[:lineTail]
#     outputFile.write('|' + line + '\n')