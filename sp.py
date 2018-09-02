from urllib import request
import re
import time

'''
lpc222
用于寻找需要解锁的饰品
!!!需要翻墙，开全局
'''

def search_item(start, count, url_p1, url_p2, url_p3, url_p4):
  
    url = url_p1 + url_p2+ str(start) + url_p3 + str(count) +url_p4

    page = request.Request(url)
    page.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    page_info = request.urlopen(page).read().decode('utf-8')

    regex =  r'"descriptions":\[(.*?)\]'
    pa = re.compile(regex)#转为pattern对象
    item_des_list = re.findall(pa, page_info)
    #print(item_des_list)

    regex =  r'"value":"明光(.*?)"'     #不同物品此处需修改
    pa = re.compile(regex)
    for i in range(len(item_des_list)):
        desc = item_des_list[i].encode('utf-8').decode('unicode_escape')
        #print(desc)
        locked = re.findall(pa,desc)
        #print(locked,int(start) + i)

        try:
            if not len(locked[0]):
                print('find an item near pos ',int(start) + i)
        except Exception as e:
            print(int(start) + i,'个物品描述解析出现了问题，跳过此物品')
        


if __name__ == '__main__':

    #修改url_p1为steam市场中想要查找的物品的url
    url_p1 = "https://steamcommunity.com/market/listings/570/Helm%20of%20the%20Reef%20Kyte%20Rider"
    #以下一般不用修改
    url_p2 = "/render/?query=&start="
    url_p3 = "&count="
    url_p4 = "&country=JP&language=schinese&currency=1"
    start = 1
    count = 100

    max_item_num = 1500     #根据显示的具体物品总量设定
    
    while(start < max_item_num):

        print('searching item from '+str(start)+' to '+str(start+count-1))
        search_item(start,count,url_p1,url_p2,url_p3,url_p4)
        start += count
        time.sleep(5)


    