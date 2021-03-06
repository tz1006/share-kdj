#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: sort_price.py

from datetime import datetime
import threading
#from concurrent.futures import ThreadPoolExecutor, wait

#pool = ThreadPoolExecutor(max_workers=20)

############PROXY###########
timeout = 3

from tools import *

###多线程筛选
def sort_list(l, price=18):
    start_time = datetime.now()
    a = len(l)
    l1 = sort_price_list(l, price)
    b = len(l1)
    end_time = datetime.now()
    timedelsta = (end_time - start_time).seconds
    print('过滤掉%s支股票，还剩%s支股票，耗时%s秒。' % (a-b, b, timedelsta))
    return(l1)

########################### 筛选价格 #############################

def sort_price(share_code, target_price=18):
    #print('检查 %s 价格是否低于%s元' % (share_code, target_price))
    price = price_now(share_code)[0]
    if price == '':
        li.remove(share_code)
        #print('%s 无法获取价格。' % share_code)
    elif price > target_price:
        li.remove(share_code)
        #print('%s 不符合条件。' % share_code)
    else:
        pass
        #print('%s 符合条件!' % share_code)


# 多线程筛选价格
def sort_price_list(l, target_price=18):
    global li
    print('筛选价格中, 一共%s支股票。' % len(l))
    li = list(l)
    #futures = []
    threads = []
    for i in l:
        a = threading.Thread(target=sort_price, args=(i, target_price))
        threads.append(a)
        a.start()
        #futures.append(pool.submit(sort_price, (i, target_price)))
    for t in threads:
        t.join()
    #wait(futures)
    a = len(l)
    b = len(li)
    print('移除 %s 支股票价格低于%s元，列表中还剩 %s' % (a-b, target_price, b))
    return(li)




def help():
    print('''
    多线程
    sort_list(list, price=18, day=10)
        sort_price_list(list, target_price=18)
          sort_price()
    help()
    ''')
