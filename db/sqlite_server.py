from flask import Flask
from flask_jsonrpc import JSONRPC
from flask import make_response
import requests
import json
import sqlite3


app = Flask(__name__)

jsonrpc = JSONRPC(app, '/')


@app.route('/check')
def check():
    return make_response('server online', 200)


@jsonrpc.method('select_sql')
def select_sql(sql):
    conn = sqlite3.connect("testing_db.sql3")
    cursor = conn.cursor()

    cursor.execute(sql)
    response_result = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    return response_result


def register_service():
    try:
        data = json.dumps({
            "ID": "sqlitdatabase1",
            "Name": "sqlite_query",
            "Tags": [
                "primary",
                "v1"
            ],
            "Address": "192.168.0.100",
            "Port": 3000,
            "EnableTagOverride": False,
            "Check": {
                "http": "http://192.168.0.100:3000/check",
                "Interval": "10s"
            }
        }
        )

        requests.put(
            "http://192.168.0.100:8500/v1/agent/service/register", data=data)
    except Exception as e:
        print("service register failed")


if __name__ == '__main__':
    register_service()
    app.run(host='0.0.0.0', debug=True, port=3000)
