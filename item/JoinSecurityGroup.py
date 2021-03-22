#!/usr/bin/env python
#coding=utf-8
#writer=fangshuai

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.JoinSecurityGroupRequest import JoinSecurityGroupRequest
SecurityGroup_Id=['sg-bp1a7lba05nxpkhxiha6']
Instance_Id=['i-bp10wl8w02ofh7chbcal']
def JoinSecurityGroup(Sid,Iid):
    client = AcsClient('', '', 'cn-hangzhou')

    request = JoinSecurityGroupRequest()
    request.set_accept_format('json')

    request.set_SecurityGroupId(Sid)
    request.set_InstanceId(Iid)
    response = client.do_action_with_exception(request)
# python2:  print(response)
    print(str(response, encoding='utf-8'))
for Sid in SecurityGroup_Id:
    for Iid in Instance_Id:
        JoinSecurityGroup(Sid,Iid)