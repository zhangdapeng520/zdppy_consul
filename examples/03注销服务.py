from zdppy_consul import consul


def unregister(server_name, ip, port):
    c = consul.Consul()
    print(f"开始退出服务{server_name}")
    c.agent.service.deregister(f'{server_name}-{ip}-{port}')


if __name__ == '__main__':
    unregister("test_server", "127.0.0.1", 8500)
