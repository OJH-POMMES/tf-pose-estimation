#!/usr/bin/env python
# -*- encoding:utf-8 -*-


import requests
# import settings


class KintoneHandler:
    def __init__(self, _KINTONE_TOKEN: str, kintone_domain: str, app=5):
        self.token = _KINTONE_TOKEN
        self.app = app
        self.url_1recode = f'https://{kintone_domain}/k/v1/record.json'
        self.url_allrecodes = f'https://{kintone_domain}/k/v1/records.json'
        self.headers = {
            'X-Cybozu-API-Token': self.token
        }

    def get_kintone(self, _data: dict = {}):
        """get kintone records

        Args:
            _data (dict, optional): target record's field name. Defaults to {}.

        Returns:
            list: records
        """

        url = self.url_allrecodes
        request_data = {
            'app': self.app
        }
        request_data.update(_data)

        headers = self.headers
        res = requests.get(url, params=request_data, headers=headers)

        return res.json()

    def register_kintone(self, data: dict) -> bool:
        """register a record to kintone

        Args:
            data (dict): data {'field': 'value'}

        Returns:
            bool: success of fail
        """

        record = {d[0]: {'value': d[1]} for d in data.items()}
        request_data = {
            'app': self.app,
            'record': record,
        }

        res = requests.post(self.url_1recode, json=request_data, headers=self.headers)

        # レスポンスの例外処理
        res_data = res.json()

        if 'id' in res_data.keys():
            return True
        else:
            return False

    # def register_many_kintone(self, _data):
    # 	'''
    # 	:param _data: [{'field': 'value'}]
    # 	:return: True or False
    # 	'''

    # 	records = list()
    # 	for data in _data:
    # 		recode = {d[0]: {'value': d[1]} for d in data.items()}
    # 		records.append(recode)

    # 	request_data = {
    # 		'app': self.app,
    # 		'records': records
    # 	}

    # 	res = requests.post(self.url_allrecodes, json=request_data, headers=self.headers)

    # 	# レスポンスの例外処理
    # 	print(res.text)
    # 	res_data = res.json()

    # 	if 'ids' in res_data.keys():
    # 		return True
    # 	else:
    # 		return False

    def update_kintone(self, _id, _data):
        '''
        :param _data:{'field': 'value'}
        :return: True or False
        '''

        record = {d[0]: {'value': d[1]} for d in _data.items()}
        request_data = {
            'app': self.app,
            'record': record,
            'id': _id
        }

        res = requests.put(self.url_1recode, json=request_data, headers=self.headers)

        # レスポンスの例外処理
        res_data = res.json()

        # print(res_data)

        if 'revision' in res_data.keys():
            return True
        else:
            return False


if __name__ == '__main__':
    import json
    token = ''
    domain = ''

    k = KintoneHandler(token, domain, app=2)
    data = k.get_kintone()
    # mergen_list = k.register_kintone({'score': '50', 'state': 'Bad', 'file': 'test'})
    print(json.dumps(data))
