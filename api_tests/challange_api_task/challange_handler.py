"""Required modules"""
import time
from datetime import datetime
import requests
from dateutil import relativedelta


class IotHandler:
    """Handler class for challange_slide_182"""

    url = "https://jsonmock.hackerrank.com/api"
    iot_devices_endpoint = "/iot_devices/search"

    def get_data(self):
        """Get all data from API and return in weird shape"""

        params = {
            "page": 1
        }
        response_body_all = []
        for _ in range(10):
            response = requests.get(f"{self.url}{self.iot_devices_endpoint}",
                                    params=params, timeout=10)
            response_body = response.json()
            response_body_all.append(response_body["data"])
            params["page"] += 1

        return response_body_all

    def parse_all_records(self):
        """Parse data and return as list of dictionaries"""

        final_table_records = []
        data = self.get_data()
        for i in data:
            temp_table = []
            temp_table.append(i)
            for j in temp_table[0]:
                final_table_records.append(j)
            temp_table = []
        return final_table_records

    def num_devices(self, status_query: str, threshold: int, date_str: str) -> int:
        """Return num of devices with given parameters"""

        counter = 0
        check_list = []
        timestamp_start = int(time.mktime(datetime.strptime(date_str, "%m-%Y").timetuple()))
        timestamp_end = int((datetime.fromtimestamp(timestamp_start) +
                            relativedelta.relativedelta(months=1)).timestamp())

        final_table = self.parse_all_records()
        for dictionary in final_table:
            if dictionary["status"] == status_query \
                    and dictionary["operatingParams"]["rootThreshold"] > threshold\
                    and timestamp_start * 1000 < dictionary["timestamp"] < timestamp_end * 1000:
                counter += 1
                check_list.append(dictionary)
        return counter
