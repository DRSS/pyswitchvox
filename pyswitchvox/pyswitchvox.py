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
        print r.json()
        return r.json()

    def get_account_id(self, extension):
        account_id = self.get_info([extension])['response']['result'][
            'extensions']['extension']['account_id']
        return account_id

    def call(self, dial_first, dial_second):
        http_method = 'switchvox.call'
        account_id = self.get_account_id(dial_first)
        params = {'dial_first': dial_first,
                  'dial_second': dial_second,
                  'dial_as_account_id': account_id,
                  'ignore_user_api_settings': 1,
                  'ignore_user_call_rules': 1, }
        json_data = self.build_json(http_method, params)
        print(json_data)
        r = requests.post(self.server,
                          data=json_data,
                          headers=self.headers,
                          auth=HTTPDigestAuth(self.user, self.password),
                          verify=False)
        print r.json()
        return r

    def get_call_log(self, extension, startdate, enddate):
        http_method = 'switchvox.callLogs.search'
        account_id = self.get_account_id(extension)
        params = {'start_date': startdate,
                  'end_date': enddate,
                  'account_ids': [account_id], }
        json_data = self.build_json(http_method, params)
        print(json_data)
        r = requests.post(self.server,
                          data=json_data,
                          headers=self.headers,
                          auth=HTTPDigestAuth(self.user, self.password),
                          verify=False)
        print r.json()
        return r
