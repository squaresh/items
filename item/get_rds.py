from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkrds.request.v20140815.DescribeDBInstancesRequest import DescribeDBInstancesRequest
import json

client = AcsClient('', '', 'cn-hangzhou')

request = DescribeDBInstancesRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response)
# print(str(response, encoding='utf-8'))
id=json.loads(response)
id_list=id['Items']['DBInstance']
for i in id_list:
    print(i['DBInstanceId'])