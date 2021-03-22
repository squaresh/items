# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from Tea.core import TeaCore
from typing import List

from alibabacloud_ecs20140526.client import Client as EcsClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_env.client import Client as EnvClient
from alibabacloud_ecs20140526 import models as ecs_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def initialization(
        region_id: str,
    ) -> EcsClient:
        """
        Initialization  初始化公共请求参数
        """
        config = open_api_models.Config()
        # 您的AccessKey ID
        config.access_key_id = EnvClient.get_env('ACCESS_KEY_ID')
        # 您的AccessKey Secret
        config.access_key_secret = EnvClient.get_env('ACCESS_KEY_SECRET')
        # 您的可用区ID
        config.region_id = region_id
        return EcsClient(config)

    @staticmethod
    def describe_instance_monitor_data(
        client: EcsClient,
        instance_id: str,
        start_time: str,
        end_time: str,
    ) -> None:
        """
        DescribeInstanceMonitorData    查询一台 Ecs 实例所有相关的监控信息
        """
        req = ecs_models.DescribeInstanceMonitorDataRequest()
        # 待查询的实例 ID
        req.instance_id = instance_id
        # 获取数据的起始时间点。按照 ISO8601 标准表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        req.start_time = start_time
        # 获取数据的结束时间点。按照 ISO8601 标准表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。 如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        req.end_time = end_time
        try:
            resp = client.describe_instance_monitor_data(req)
            ConsoleClient.log('--------------------查询Ecs所有相关的监控信息--------------------')
            ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    async def describe_instance_monitor_data_async(
        client: EcsClient,
        instance_id: str,
        start_time: str,
        end_time: str,
    ) -> None:
        """
        DescribeInstanceMonitorData    查询一台 Ecs 实例所有相关的监控信息
        """
        req = ecs_models.DescribeInstanceMonitorDataRequest()
        # 待查询的实例 ID
        req.instance_id = instance_id
        # 获取数据的起始时间点。按照 ISO8601 标准表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        req.start_time = start_time
        # 获取数据的结束时间点。按照 ISO8601 标准表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。 如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        req.end_time = end_time
        try:
            resp = await client.describe_instance_monitor_data_async(req)
            ConsoleClient.log('--------------------查询Ecs所有相关的监控信息--------------------')
            ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def describe_user_data(
        client: EcsClient,
        instance_id: str,
        region_id: str,
    ) -> None:
        """
        DescribeUserData    查询一台Ecs实例的自定义数据
        """
        req = ecs_models.DescribeUserDataRequest()
        req.region_id = region_id
        req.instance_id = instance_id
        try:
            resp = client.describe_user_data(req)
            ConsoleClient.log('--------------------查询Ecs自定义数据--------------------')
            ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    async def describe_user_data_async(
        client: EcsClient,
        instance_id: str,
        region_id: str,
    ) -> None:
        """
        DescribeUserData    查询一台Ecs实例的自定义数据
        """
        req = ecs_models.DescribeUserDataRequest()
        req.region_id = region_id
        req.instance_id = instance_id
        try:
            resp = await client.describe_user_data_async(req)
            ConsoleClient.log('--------------------查询Ecs自定义数据--------------------')
            ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 可用区域Id
        region_id = args[0]
        # 待查询的实例 ID
        instance_id = args[1]
        # 获取数据的起始时间点。按照 ISO8601 表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        start_time = args[2]
        # 获取数据的结束时间点。按照 ISO8601 标准表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。 如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        end_time = args[3]
        client = Sample.initialization(region_id)
        # 查询一台 Ecs 实例所有相关的监控信息
        Sample.describe_instance_monitor_data(client, instance_id, start_time, end_time)
        # 查询一台Ecs实例的自定义数据
        Sample.describe_user_data(client, instance_id, region_id)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 可用区域Id
        region_id = args[0]
        # 待查询的实例 ID
        instance_id = args[1]
        # 获取数据的起始时间点。按照 ISO8601 表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        start_time = args[2]
        # 获取数据的结束时间点。按照 ISO8601 标准表示，并需要使用 UTC 时间，格式为：YYYY-MM-DDThh:mm:ssZ。 如果指定的秒（ss）不是 00，则自动换算为下一分钟。
        end_time = args[3]
        client = Sample.initialization(region_id)
        # 查询一台 Ecs 实例所有相关的监控信息
        await Sample.describe_instance_monitor_data_async(client, instance_id, start_time, end_time)
        # 查询一台Ecs实例的自定义数据
        await Sample.describe_user_data_async(client, instance_id, region_id)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])