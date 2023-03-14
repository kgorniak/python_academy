import unittest

from api_tests.challange_api_task.challange_handler import IotHandler


class IotConnected(unittest.TestCase):

    def setUp(self) -> None:
        self.iot_handler = IotHandler()

    def test_input(self):
        self.assertEqual(3, self.iot_handler.num_devices("STOPPED", 45, "04-2019"))


if __name__ == '__main__':
    unittest.main()
