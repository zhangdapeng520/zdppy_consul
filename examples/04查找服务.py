import zdppy_requests

headers = {
    "contentType": "application/json"
}

service_id = "user-service-id"
service = "user-service"
url = "http://127.0.0.1:8500/v1/agent/services"
params = {
    "filter": f'Service == "{service}"'
}
rsp = zdppy_requests.get(url, params=params).json()
for key, value in rsp.items():
    print(key, value)
