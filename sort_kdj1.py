#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: sort_kdj1.py

from datetime import datetime
import threading
#from concurrent.futures import ThreadPoolExecutor, wait

#pool = ThreadPoolExecutor(max_workers=20)

############PROXY###########
timeout = 3

from tools import *

###多线程筛选
def sort_list(l, day=1):
    start_time = datetime.now()
    a = len(l)
    l1 = sort_kdj_list(l, day)
    b = len(l1)
    end_time = datetime.now()
    timedelsta = (end_time - start_time).seconds
    print('过滤掉%s支股票，还剩%s支股票，耗时%s秒。' % (a-b, b, timedelsta))
    return(l1)

########################### 筛选KDJ #############################

def sort_kdj(share_code, day=1):
    #print('检查 %s K是否低于J' % (share_code))
    kdj = kdj_now(share_code, day+1)
    if kdj == []:
        li.remove(share_code)
        print('%s 无法获取kdj。' % share_code)
    else:
        kdj.remove(kdj[0])
        for i in kdj:
            if i[0] > i[1]:
                li.remove(share_code)
                print('%s 不符合条件。' % share_code)
                break
            else:
                pass
        #print('%s 符合条件!' % share_code)


# 多线程筛选KDJ
def sort_kdj_list(l, day=1):
    global li
    print('筛选KDJ中, 一共%s支股票。' % len(l))
    li = list(l)
    #futures = []
    threads = []
    for i in l:
        a = threading.Thread(target=sort_kdj, args=(i, day))
        threads.append(a)
        a.start()
        #futures.append(pool.submit(sort_kdj, (i, day)))
    for t in threads:
        t.join()
    #wait(futures)
    a = len(l)
    b = len(li)
    print('移除 %s 支股票J低于K，列表中还剩 %s' % (a-b, b))
    return(li)




def help():
    print('''
    多线程
    sort_list(list, day=1)
        sort_kdj_list(list, day=1)
          sort_kdj()
    help()
    ''')
