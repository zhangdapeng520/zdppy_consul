# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  consul.py
@Time    :  2022/7/23 19:02
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
from typing import Dict, List

import zdppy_requests


class Consul:
    """
    consul核心类
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 8500):
        self.host = host  # consul主机地址
        self.port = port  # consul端口号

    def register_http_server(self,
                             server_name: str,
                             headers: Dict,
                             tags: List[str],
                             server_host: str,
                             server_port: int,
                             health_check_path: str) -> bool:
        """
        注册HTTP服务
        :param server_name: 服务名称
        :param headers: 请求头
        :param tags: 服务标签
        :param server_host: 服务主机地址
        :param server_port: 服务端口号
        :param health_check_path: 健康检查URL或者路径
        """
        # 目标地址
        target_url = f"http://{self.host}:{self.port}/v1/agent/service/register"

        # 请求头
        if not headers:
            headers = {
                "ContentType": "application/json"
            }

        # 健康检查地址
        if not health_check_path.startswith("http"):
            if not health_check_path.startswith("/"):
                health_check_path = f"/{health_check_path}"
            health_check_path = f"http://{server_host}:{server_port}{health_check_path}"

        # 发送注册请求
        rsp = zdppy_requests.put(target_url, headers=headers, json={
            "Name": server_name,
            "ID": "user-web-01",
            "Tags": tags,
            "Address": server_host,
            "Port": server_port,
            "Check": {
                "HTTP": health_check_path,
                "Timeout": "5s",
                "Interval": "5s",
                "DeregisterCriticalServiceAfter": "15s"
            }
        })

        # 返回注册结果
        return rsp is not None and rsp.status_code == 200

    def deregister(self, server_id: str) -> bool:
        """
        注销服务
        :param server_id: 服务ID
        """
        # 请求头
        headers = {
            "ContentType": "application/json"
        }

        # 请求地址
        url = f"http://{self.host}:{self.port}/v1/agent/service/deregister/{server_id}"

        # 发送注销服务的请求
        rsp = zdppy_requests.put(url, headers=headers)

        # 返回结果
        return rsp.status_code == 200