from flask_jsonrpc.proxy import ServiceProxy
import requests


class Client:

    def __init__(self, service_id):
        pass
        self.service = requests.get(
            'http://192.168.0.100:8500/v1/agent/services').json().get(
            service_id)
        print(self.service)

    def select_result(self, sql):
        address = self.service.get("Address")
        port = self.service.get("Port")
        server = ServiceProxy('http://{}:{}/'.format(address, port))
        response = server.select_sql(sql).get('result')
        return response


sqlite_client = Client("10001")
result = sqlite_client.select_result('select name from student_table')
for i in result:
    print(i[0])
