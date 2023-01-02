import unittest
from faker import Faker
import requests
from api_tests.gorest_api_handler import APIHandler


class TestGorest(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler

    def test_Create_user(self):
        url = "https://gorest.co.in/public/v2/users"
        faker = Faker()
        fake_email = faker.free_email()
        print(fake_email)
        header = {
            "Authorization": "Bearer 0cc9c693995f6c1c628b5c00bd47c4b46dffb1acdbedc5f0a867ff70a11190b5"
        }
        params = {
            "name": "Tenali Ramakrishna",
             "gender": "male",
             "email": fake_email,
             "status": "active"
        }

        create_user = requests.post(url, headers=header, params=params)
        # print(create_user.status_code)
        created_user_body = create_user.json()
        user_id = created_user_body["id"]
        print(user_id)
        self.assertTrue(created_user_body["id"])

        params2 = {
            "name": "Adam Test"
        }
        update_url = f"{url}/{user_id}"
        print(update_url)
        requests.put(f"{url}/{user_id}", params=params2)
        updated_user = requests.get(f"{url}/{user_id}").json()
        print(updated_user)
        print(updated_user["name"])
        print(params2["name"])
        # self.assertEqual(updated_user["name"], params2["name"])


if __name__ == '__main__':
    unittest.main()
