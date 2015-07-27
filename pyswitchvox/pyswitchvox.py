import requests
import json
from requests.auth import HTTPDigestAuth


class SwitchVox:
    user = ""
    password = ""
    server = ""
    headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}

    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.server = server

    def build_json(self, http_method, params):
        json_data = {'request': {'method': http_method,
                                 'parameters': params
                                 }
                     }
        return json.dumps(json_data)

    def get_info(self, extensions):
        http_method = 'switchvox.extensions.getInfo'
        params = {'extensions': extensions}
        json_data = self.build_json(http_method, params)
        r = requests.post(self.server,
                          data=json_data,
                          headers=self.headers,
                          auth=HTTPDigestAuth(self.user, self.password),
                          verify=False)
        return r.json()

    def call(self, from_phone_number, to_phone_number):
        http_method = 'switchvox.call'
        account_id = self.get_info(from_phone_number).account_id
        params = {'dial_first': from_phone_number,
                  'dial_second': to_phone_number,
                  'dial_as_account_id': account_id
                  }
        json_data = self.build_json(http_method, params)
        print(json_data)
        r = requests.post(self.server,
                          data=json_data,
                          headers=self.headers,
                          auth=HTTPDigestAuth(self.user, self.password),
                          verify=False)
        print r.json()
        return r
