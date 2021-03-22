# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id='LTAI4GDDng9o1Jcr7NXMyR75',
            # 您的AccessKey Secret,
            access_key_secret='esCq8FBLqFVky0EupSp1Abr9MUycaH'
        )
        # 访问的域名
        config.endpoint = 'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)


    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_instance_status_request = ecs_20140526_models.DescribeInstanceStatusRequest(
            region_id='cn-hangzhou'
        )
        print(client.describe_instance_status(describe_instance_status_request))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        describe_instance_status_request = ecs_20140526_models.DescribeInstanceStatusRequest(
            region_id='cn-hangzhou'
        )
        await client.describe_instance_status_async(describe_instance_status_request)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])

