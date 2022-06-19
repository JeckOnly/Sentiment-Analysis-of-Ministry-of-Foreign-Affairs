import requests
import os
import sys
import shutil


def getVList(page):
    r = requests.get(
        'https://api.bilibili.com/x/space/arc/search?mid=%s&ps=%s&tid=0&pn=%s&keyword=&order=%s&jsonp=jsonp' % (
            1087482281, 50, 1, "pubdate"))
    content = r.json()
    try:
        vlist = content['data']['list']['vlist']
    except TypeError:
        return False
    return vlist


def getBidList():
    page = 1
    result = []
    while True:
        vlist = getVList(page)
        if not vlist:
            break

        for i in vlist:
            print(i["bvid"])
            result.append(i["bvid"])
        if len(result) > 100:
            return result
        page += 1
    return result

