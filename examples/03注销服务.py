import zdppy_requests

headers = {
    "contentType": "application/json"
}

service_id = "user-web-01"
url = f"http://127.0.0.1:8500/v1/agent/service/deregister/{service_id}"
rsp = zdppy_requests.put(url, headers=headers)
if rsp.status_code == 200:
    print("注销成功")
else:
    print(f"注销失败：{rsp.status_code}")
