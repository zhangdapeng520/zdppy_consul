from zdppy_consul import consul

c = consul.Consul()

# 新增或更新
c.kv.put('username', '张大鹏'.encode("utf8"))  # 不支持直接传中文

# 获取
index, data = c.kv.get('username')
print(index, data)
print(data['Value'].decode("utf8"))
