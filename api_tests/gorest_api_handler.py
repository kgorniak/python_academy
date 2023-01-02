import requests


class APIHandler:
    url = "https://gorest.co.in/public/v2"
    user_endpoint = "/users"

    def create_user(self, user_data):
        res = requests.post(f"{self.url}{self.user_endpoint}")
        return res

    def get_user(self, user_id):
        res = requests.get(f"{self.url}{self.user_endpoint}/{user_id}")
