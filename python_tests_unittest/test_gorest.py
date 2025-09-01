import unittest

import requests
from faker import Faker
from api_tests.gorest_api_handler import APIHandler


class TestGorest(unittest.TestCase):

    def setUp(self) -> None:
        self.api_handler = APIHandler("0cc9c693995f6c1c628b5c00bd47c4b46dffb1acdbedc5f0a867ff70a11190b5")
        self.faker = Faker()

    def test_create_modify_and_delete_user(self):

        # create user
        new_user = {
            "name": self.faker.name(),
            "gender": "male",
            "email": self.faker.free_email(),
            "status": "active"
        }

        create_user_body = self.api_handler.create_user(new_user)
        self.user_id = create_user_body["id"]
        self.assertTrue(self.user_id)

        # get user
        user_body = self.api_handler.get_user(self.user_id)
        self.assertTrue(user_body)

        # update user
        data_to_update = {
            "name": "Adam Test",
            "gender": "female"
        }

        self.api_handler.update_user(user_id=self.user_id, params=data_to_update)
        updated_user_body = self.api_handler.get_user(self.user_id)
        self.assertEqual(data_to_update["name"], updated_user_body["name"])
        self.assertEqual(data_to_update["gender"], updated_user_body["gender"])

        # delete user
        self.api_handler.delete_user(user_id=self.user_id)
        res = requests.get(f"{self.api_handler.url}{self.api_handler.user_endpoint}/{self.user_id}",
                           headers=self.api_handler.headers)
        self.assertEqual(404, res.status_code)


if __name__ == '__main__':
    unittest.main()
