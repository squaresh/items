import json
from openpyxl import Workbook
with open('D:\pycharm\projects\learn\item\\txt\swd_gd.txt',mode='r',encoding='utf8') as f:
    a=f.read()
    k=a.replace('"requestId":null,"return_subCode":null,"data":{"totalRows":76,"rows":[{','').replace(']},"errorDetail":"","result":"success","return_subMsg":null,"errorMsg":"","responseCode":"200"}','')
    b = k.split('},{')
    for i in b:
        e=i.replace('{','').replace('}','').replace('"instanceId"','{"instanceId"').replace('"isoId":null','"isoId":null}')
        if 'swdvpcjr' in e:
            pass
        else:
            if '_gd_' in e:
                try:
                    id_list=json.loads(e)
                except:
                    print('格式发生错误',e)
                else:
                    with open('id_list.txt',mode='a+',encoding='utf-8') as f :
                        f.write(id_list['instanceName']+'\t'+id_list['instanceId']+'\n')
                   # print(id_list['instanceName'],type(id_list['instanceName']))
f.close()