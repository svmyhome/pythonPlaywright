from playwright.sync_api import Page
import pytest

def test_inventory(page: Page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(response.url)
    print(response.status)
    print(response.headers)
    print(response.json())
    assert response.json()['Gold'] == 3

def test_add_user(page: Page):
    data = [
              {
                "id": 9743,
                "username": "fsd",
                "firstName": "fff",
                "lastName": "ggg",
                "email": "bbb",
                "password": "tt",
                "phone": "333",
                "userStatus": 0
              }
            ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }

    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray',data=data, headers=header)
    print(response.url)
    print(response.status)
    print(response.headers)
    print(response.json())