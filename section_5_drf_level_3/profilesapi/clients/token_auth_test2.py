import requests


def client():
    # data = {
    #     "username": "Test",
    #     "email" : "test@rest.com",
    #     "password1": "Testme1234",
    #     "password2": "Testme1234"
    #     }
    
    # response = requests.post(
    #     "http://127.0.0.1:8000/api/rest-auth/registration/", 
    #     data=data)

    token = "Token 1304ce3e9a85c784d350e2764b8fdd219a57867f"
    headers = {"Authorization": token}

    response = requests.get(
        "http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code : ", response.status_code)
    print("Response Data : ", response.json())


if __name__ == "__main__":
    client()
