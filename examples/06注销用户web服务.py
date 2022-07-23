from zdppy_consul import Consul

# 创建对象
c = Consul("127.0.0.1", 8500)

# 注销服务
service_id = "user-web-01"
c.deregister(service_id)
