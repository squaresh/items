# age=input('请输入你的年龄:')
# print(age,type(age))
# print('''
# ************
# 欢迎来到真心话大冒险
# ************''')
# name=input('请输入用户名:')
# while name!='方帅' or name!='刘雨静':
#     print('用户名错误请重新输入')
#     name = input('请输入用户名:')
# cipher=input('请输入密码:')
# while cipher!='good':
#     print('密码错误请重新输入:')
#     cipher = input('请输入密码:')
# print('''尊敬的会员%s，欢迎来到真心话大冒险
# 祝你玩的愉快！！！'''%(name))
# number=int(input('请输入你的数字:'))
# print(number)

# for i in'fanghsuai':
#     if i=='s':
#         continue
#     else:
#         print(i)
# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print('这是 pass 块')
# #    print('当前字母 :', letter)
# # import math
# # dir(math)
# a='fang'
# b='shuai'
# e=['das',13,'dwwa']
# c=('aaa','bbb','ccc')
# d={'k':21312,'g':'dasd'}
# print(e[0],e[1])
# print(c[2])
# print(d['k'])
# import time
# print('当前时间为:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# import json
# a = json.load(open("id_list.txt",'r',encoding='utf8'))
# ecs_list = a['data']['rows']
# for line in ecs_list:
#     print(line['instanceId'],end='\t\t')
#     print(line['instanceName'])
# import json
# with open('id_list.txt',mode='r',encoding='utf8') as f:
#     id=json.load(f)
#     dd=id['data']['rows']
#     print(dd)

#
# dd={'ddd':'fs','ccc':4354,'kk':{'gg':{'fss':['cs',98,'fsa','dkls'],'sf':[{'ddd':'fs','ccc':4354}]},'bb':987}}
# rr=dd['kk']['gg']['fss']
# cc=dd['kk']['gg']
# print(rr,type(rr),cc,type(cc))


# import json
# with open('./txt/sc_ecs.txt',mode='r',encoding='utf8') as f:
#     id_dict=json.load(f)
#     id_list=id_dict['data']['rows']
#     for i in id_list:)
#          print('instanceId:{},instanceName:{}'.format(i['instanceId'],i['instanceName']))
# '''
# def_one nmber(a):
#     try:
#         use_nm=int(a)
#         print('a',use_nm)
#         return use_nm
#     except:
#         print('c',a)
#         print('输入有误请重新输入')
#         a = input('请输入你猜测的数字:')
#         print('b',a)
#         nmber(a)
#
# if __name__ == '__main__':
#     a=input('请输入你猜测的数字:')
#     nmber(a)
#     k=nmber(a)
# '''
# a='dasdasd'
# b=a+r'\n'+'dasdsa'
aa='dsadas'