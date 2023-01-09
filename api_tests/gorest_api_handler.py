import requests
import os


class APIHandler:
    url = "https://gorest.co.in/public"
    user_endpoint = "/users"
    api_version_dict = {
        "v1": "/v1",
        "v2": "/v2",
        "public": "/public-api"
    }

    def __init__(self, token="", api_ver="v2"):
        self.url = f"{self.url}{self.api_version_dict[api_ver]}"
        if not token:
            token = os.environ["GOREST_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def create_user(self, user_data, expected_status_code=201):
        res = requests.post(f"{self.url}{self.user_endpoint}", json=user_data, headers=self.headers)
        if expected_status_code:
            assert expected_status_code == res.status_code
        return res.json()

    def get_user(self, user_id):
        res = requests.get(f"{self.url}{self.user_endpoint}/{user_id}", headers=self.headers)
        # if expected_status_code:
        #     assert expected_status_code == res.status_code
        return res.json()

    def update_user(self, user_id, params):
        requests.put(f"{self.url}{self.user_endpoint}/{user_id}", params=params, headers=self.headers)

    def delete_user(self, user_id):
        requests.delete(f"{self.url}{self.user_endpoint}/{user_id}", headers=self.headers)
