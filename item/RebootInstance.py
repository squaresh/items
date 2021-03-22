#!/usr/bin/env python
#coding=utf-8
#writer=fangshuai

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
def RebootInstance(id):
    client = AcsClient('LTAI4GJDpDmE4deuNfabu2ao', 'tfhMwTCCZpZswkRw8IIo2wcbZH1AGX', 'cn-hangzhou')

    request = RebootInstanceRequest()
    request.set_accept_format('json')

    request.set_InstanceId(id)

    response = client.do_action_with_exception(request)
# python2:  print(response)
    print(str(response, encoding='utf-8'))
id_list=['i-bp10wl8w02ofh7chbcal']
for id in id_list:
    RebootInstance(id)
