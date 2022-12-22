import unittest
import requests
import api_tests


class ApiTestIP(unittest.TestCase):

    def test_check_IP(self):
        response_body = requests.get(url="https://api.ipify.org?format=json").json()
        print(response_body)
        self.assertTrue(response_body["ip"])

    def test_check_IP_regex(self):
        response_body = requests.get(url="https://api.ipify.org?format=json").json()
        print(response_body)
        self.assertRegex(response_body["ip"], "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}")
        segments = response_body["ip"].split(".")
        for segment in segments:
            self.assertTrue(0 <= int(segment) < 255)


if __name__ == '__main__':
    unittest.main()
