from zdppy_consul import Consul

# 创建对象
c = Consul("127.0.0.1", 8500)

# 注册HTTP服务
c.register_http_server(
    server_name="user-web",
    headers={
        "contentType": "application/json"
    },
    tags=["web", "zdpgo", "api"],
    server_host="127.0.0.1",
    server_port=8888,
    health_check_path="/v1/health"
)
