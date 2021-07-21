import requests


def client():
    credentials = {"username": "admin", "password": "durwltkwl123"}
    response = requests.post(
        "http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    print("Status Code : ", response.status_code)
    print("Response Data : ", response.json())


if __name__ == "__main__":
    client()
