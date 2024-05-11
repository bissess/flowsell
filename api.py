import json
import logging
import time
import requests
from datetime import datetime


# class ClientsAPI:
#     def __init__(self, main_headers):
#         self.main_headers = main_headers
#         self.base_url = 'https://api.alteg.io/api/v1'
#
#     def create_body(self, page, page_size):
#         body = {
#             "page": page,
#             "page_size": page_size,
#             "fields": [
#                 "id",
#                 "name",
#                 "phone",
#                 "email",
#                 "discount",
#                 "first_visit_date",
#                 "last_visit_date",
#                 "sold_amount",
#                 "visit_count"
#             ],
#             "order_by": "id",
#             "order_by_direction": "desc",
#             "operation": "AND"
#         }
#         return body
#
#     def get_clients(self, company_id, page, page_size):
#         self.url = f'{self.base_url}/company/{company_id}/clients/search'
#         self.body = self.create_body(page, page_size)
#
#         self.max_retries = 3
#         self.retries_delay = 5
#         self.retries = 0
#
#         while self.retries < self.max_retries:
#             try:
#                 response = requests.post(self.url, json=self.body, headers=self.main_headers)
#                 if response.status_code == 200:
#                     clients_data = response.json()
#                     clients_list = clients_data.get("data", [])
#                     return clients_list
#                 else:
#                     logging.error(f'Error retrieving data: {response.text}')
#
#             except requests.exceptions.RequestException as e:
#                 logging.warning(f'Error: {e}')
#
#             self.retries += 1
#             time.sleep(self.retries_delay)
#
#         logging.error(f'Connection error. Attempts were made: {self.retries}')
#         raise ConnectionError(f'Connection error. Attempts were made: {self.retries}')


class ClientsRecordsAPI:
    def __init__(self, main_headers):
        self.main_headers = main_headers
        self.base_url = 'https://api.alteg.io/api/v1'

    def create_params(self, page, total_count):
        params = {
            "page": page,
            "total_count": total_count,
            "data":
                [
                    {
                        "id": None,
                        "company_id": None,
                        "staff_id": None,
                        "services": None,
                        "staff": None,
                        "date": None,
                        "datetime": None,
                        "create_date": None,
                        "comment": None,
                        "online": None,
                        "confirmed": None,
                        "seance_length": None,
                        "length": None,
                        "from_url": None,
                        "visit_id": None,
                        "created_user_id": None,
                        "deleted": None,
                        "prepaid": None,
                        "prepaid_confirmed": None,
                        "last_change_date": None,
                        "documents": None,
                        "record_from": None
                    }
                ]

        }
        return params


class RecordsAPI(ClientsRecordsAPI):
    def __init__(self, main_headers):
        super().__init__(main_headers)

    def get_list_of_visits(self, company_id, page, total_count):
        self.url = f'{self.base_url}/records/{company_id}'
        self.body = self.create_params(page, total_count)

        self.max_retries = 3
        self.retries_delay = 5
        self.retries = 0

        while self.retries < self.max_retries:
            try:
                response = requests.get(self.url, json=self.body, headers=self.main_headers)
                if response.status_code == 200:
                    visits_data = response.json()
                    visits_list = visits_data.get('data', [])
                    return visits_list
                else:
                    logging.warning(f'Warning from visits: {response.text}')
            except requests.exceptions.RequestException as e:
                logging.exception(f'Exception error of visits: {e}')


class StaffAPI(ClientsRecordsAPI):
    def __init__(self, main_headers):
        super().__init__(main_headers)

    def get_staff_info(self, company_id, page, total_count):
        self.url = f'{self.base_url}/records/{company_id}'
        self.body = self.create_params(page, total_count)

        self.max_retries = 3
        self.retries_delay = 5
        self.retries = 0

        while self.retries < self.max_retries:
            try:
                response = requests.get(self.url, json=self.body, headers=self.main_headers)
                if response.status_code == 200:
                    staff_data = response.json()
                    staff_container = []
                    for staff in staff_data['data']:
                        staff_list = staff['staff']
                        staff_container.append(staff_list)
                    return staff_container
                else:
                    logging.warning(f'Warning from staff: {response.text}')

            except requests.exceptions.RequestException as e:
                logging.exception(f'Except error of staff: {e}')


class ServicesAPI(ClientsRecordsAPI):
    def __init__(self, main_headers):
        super().__init__(main_headers)

    def get_list_of_services(self, company_id, page, total_count):
        self.url = f'{self.base_url}/records/{company_id}'
        self.body = self.create_params(page, total_count)

        self.max_retries = 3
        self.retries_delay = 5
        self.retries = 0

        while self.retries < self.max_retries:
            try:
                response = requests.get(self.url, json=self.body, headers=self.main_headers)
                if response.status_code == 200:
                    services_data = response.json()
                    for services in services_data['data']:
                        services_list = services['services']

                        return services_list
                else:
                    logging.warning(f'Warning from services: {response.text}')
            except requests.exceptions.RequestException as e:
                logging.exception(f'Exception error of services: {e}')


class ClientsAPI(ClientsRecordsAPI):
    def __init__(self, main_headers):
        super().__init__(main_headers)

    def get_list_of_clients(self, company_id, page, total_count):
        self.url = f'{self.base_url}/records/{company_id}'
        self.body = self.create_params(page, total_count)

        max_retries = 3
        retries_delay = 5
        retries = 0

        while retries < max_retries:
            try:
                response = requests.get(self.url, json=self.body, headers=self.main_headers)

                if response.ok:
                    clients_data = response.json()
                    for clients in clients_data['data']:
                        clients_list = clients['client']

                        return clients_list
                else:
                    logging.warning(f'Warning from clients: {response.text}')

            except requests.exceptions.RequestException as e:
                logging.exception(f'Except error from clients: {e}')