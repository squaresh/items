import json
def get_Ecename(id_host):
    with open(id_host,mode='r',encoding='utf8') as f:
        a=f.read()
        k=a.replace('"requestId":null,"return_subCode":null,"data":{"totalRows":6341,"pageSize":7000,"rows":[{','').replace('}],"pageNum":1},"errorDetail":"","result":"success","return_subMsg":null,"errorMsg":"","responseCode":"200"}','')
        b = k.split('},{')
        for i in b:
            e=i.replace('{','').replace('}','').replace('"instanceId"','{"instanceId"').replace('"isoId":null','"isoId":null}')
            if 'center' in e or 'qccx' in e or 'cxtj' in e or 'broker' in e or '并网测试' in e or '_yyjca_' in e or '_yyjcb_' in e:
                pass
            else:
                if '_sc_' in e:
                    try:
                        id_list=json.loads(e)
                    except:
                        print('格式发生错误',e)
                    else:
                        print(id_list["instanceId"])
if __name__ == '__main__':
    path=input('请输入文件全路径:')
    get_Ecename(path)