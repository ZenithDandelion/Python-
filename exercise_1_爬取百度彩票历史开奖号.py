# -*- coding: utf-8 -*-
# @Author: Zenith Dandelion
# @Date:   2016-07-16 16:58:48
# @Last Modified by:   Zenith Dandelion
# @Last Modified time: 2016-07-16 16:59:50
 
import urllib,re

def Get():
    html = urllib.urlopen('http://baidu.lecai.com/lottery/draw/list/50?type=latest&num=100').read()
    reg = r'<em>(\d{2})</em><em>(\d{2})</em><em>(\d{2})</em><em>(\d{2})</em><em>(\d{2})</em><em>(\d{2})</em>[\s\S]*?<em>(\d{2})</em>'
    reg = re.compile(reg) # 编译正则表达式
    a = re.findall(reg,html)
    return a

game = Get()

wj = open('game.txt','a+')
for i in game:
    for n in i:
        wj.write(n + ' ')
    wj.write('\n')
wj.close()

exit()