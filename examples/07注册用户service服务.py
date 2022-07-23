from zdppy_consul import Consul

# 创建对象
c = Consul("127.0.0.1", 8500)

# 注册GRPC服务
c.register_grpc_server(
    server_name="user-service",
    server_id="user-service-01",
    headers={
        "contentType": "application/json"
    },
    tags=["service", "zdpgo", "grpc"],
    server_host="127.0.0.1",
    server_port=33333,
)
