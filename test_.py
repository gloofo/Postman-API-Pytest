from src.modules import *
from src.data import *

baseUrl = data()['base']

#test cases
def test_createUser():
    create = requests.post(baseUrl + data()['user']['add'], json=payload())
    assert create.status_code == 200 or 201
    print(create.json())
    return create.json()

def test_loginUser():
    session = requests.session()
    login = session.post(baseUrl + data()['user']['login'], json=credentials("login"))
    assert login.status_code == 200 or 201
    print(login.json())
    return login.json(), session

def test_updateUser():
    header = headers()
    connsess = session()
    userUpdate = connsess.patch(baseUrl + user(), json=credentials("update"), headers=header)
    assert userUpdate.status_code == 200 or 201
    print(userUpdate.json())
    return userUpdate.json()

def test_deleteUser():
    header = headers()
    connsess = session()
    deleteUser = connsess.delete(baseUrl + user(), headers=header)
    assert deleteUser.status_code == 200

def test_UserList():
    header = headers()
    connsess = session()
    userList = connsess.get(baseUrl + user(), headers=header)
    assert userList.status_code == 200
    print(userList.json())

def credentials(request: str)-> str:
    dataResponse = test_createUser()['user']['email']
    if request == "login":
        return {
            "email": f"{dataResponse}",
            "password": "pas@123W"
        }
    elif request == "update":
        return payload()

def user():
    return data()['user']['list']

def session():
    value = test_loginUser()
    return value[1]

def headers():
    value = test_loginUser()
    return {
        "Authorization": f"Bearer {value[0]['token']}"
    }

def payload():
    return {
    "firstName": f"{fake().first_name()}",
    "lastName": f"{fake().last_name()}",
    "email": f"{fake().email()}",
    "password": "pas@123W"
    }
