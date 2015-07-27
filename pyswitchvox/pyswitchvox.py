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
        """
        Given a valid switchvox method and a dictionary of params
        create a valid switchvox request json structure.
        """
        json_data = {'request': {'method': http_method,
                                 'parameters': params
                                 }
                     }
        return json.dumps(json_data)

    def extensions(self, extensions):
        """
        Given a list of extensions return detailed information on each extension.
        """
        http_method = 'switchvox.extensions.getInfo'
        params = {'extensions': extensions}
        json_data = self.build_json(http_method, params)
        r = requests.post(self.server,
                          data=json_data,
                          headers=self.headers,
                          auth=HTTPDigestAuth(self.user, self.password),
                          verify=False)
        return r.json()['response']['result']

    def call(self, from_phone_number, to_phone_number):
        """
        Initiate a call between a number and a second number, either internal
        or external.
        """
        http_method = 'switchvox.call'
        account_id = self.extension(from_phone_number).response.account_id
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
