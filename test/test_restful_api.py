# 测试tugraph restful接口
import requests
import json


def test_tugraph_login():
    url = "http://127.0.0.1:7070/login"
    headers = {
        "Accept": "application/json; charset=UTF-8",
        "Content-Type": "application/json; charset=UTF-8",
    }
    data = {"user": "admin", "password": "Xwj20021114."}
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    assert response.status_code == 200
    assert "jwt" in response.json()
    return response.json()["jwt"]


def test_tugraph_logout(jwt_token):
    url = "http://127.0.0.1:7070/logout"
    headers = {
        "Accept": "application/json; charset=UTF-8",
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + jwt_token,
    }
    response = requests.post(url, headers=headers)
    print(response.json())
    assert response.status_code == 200


def test_tugraph_cypher(jwt_token, graph="default", script="MATCH (n) RETURN n,n.name LIMIT 10"):
    url = "http://127.0.0.1:7070/cypher"
    headers = {
        "Accept": "application/json; charset=UTF-8",
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + jwt_token,
    }
    data = {"graph": graph, "script": script}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
    assert response.status_code == 200


if __name__ == "__main__":
    jwt_token = test_tugraph_login()
    test_tugraph_cypher(jwt_token, "MovieDemo1", "MATCH (n) RETURN n,n.name LIMIT 10")
    test_tugraph_logout(jwt_token)
