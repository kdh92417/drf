import requests


def client():
    credentials = {"username": "admin", "password": "durwltkwl123"}
    token = "Token 12d239e8a03eecdcb6fdee36d183a53df185d541"

    #response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    headers = {"Authorization": token}

    response = requests.get(
        "http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code : ", response.status_code)
    print("Response Data : ", response.json())


if __name__ == "__main__":
    client()
