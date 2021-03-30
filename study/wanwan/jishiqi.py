# -*- coding: utf-8 -*-
import time
print('计时器：输入1，开始记时')
print('计时器：按住ctrl +c 退出记时')
while 1==1:
    start=input()
    print(type(start))
    if start =='1':
        start_time=time.time()
        print('开始记break时')
        time.sleep(1)
        try:
            while 1==1:
                print(round(time.time()-start_time))
                time.sleep(2)
                # with open('jisq.txt', mode='a+') as f:
                #     f.write(str(time.time()-start_time))
        except:
            end_time=time.time()
            print('总共耗时：{}'.format(end_time-start_time))
            break
    else:
        print('输入错误')

