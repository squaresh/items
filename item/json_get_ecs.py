import json
import time
def find_ecsid(a):
    try:
        with open(a,mode='r',encoding='utf8') as f:
            id_dict=json.load(f)
            id_list=id_dict['data']['rows']
            for i in id_list:
                print('instanceId:{},instanceName:{}'.format(i['instanceId'],i['instanceName']))
                # time.sleep(2)
    except Exception as s:
        print('输入文件不存在或者输入文件格式错误')
        print(s)
        a=input('请重新输入:')
        find_ecsid(a)
if __name__ == '__main__':
    path=input('请输入全文件路径:')
    find_ecsid(path)
