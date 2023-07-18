import json
import requests


class GrafanaApi:
    def __init__(self, base, key):
        self.base_url = base
        self.headers = {'Authorization': "Bearer" + ' ' + key, 'Accept': "application/json",'content-type': "application/json"}

    def get_all_datasource(self):
        """
        获取所有数据源
        """
        api_url = self.base_url + '/api/datasources'
        response = requests.get(api_url, headers=self.headers, verify=False, timeout=120)
        if response.status_code == 200:
            res = response.json()
            for i in res:
                print(i)
            return res
        else:
            return False


    def get_dashboard_uid(self, name):
        """
        查询指定dashboard的uid
        """
        api_url = self.base_url + '/api/search?query=' + name
        response = requests.get(api_url, headers=self.headers, verify=False, timeout=120)
        if response.status_code == 200:
            res = response.json()

        else:
            return False

    def get_dashboard_data(self, uid):
        """
        查询指定dashboard的data
        """
        api_url = self.base_url + '/api/dashboards/uid/' + uid
        response = requests.get(api_url, headers=self.headers, verify=False, timeout=120)
        if response.status_code == 200:
            res = response.json()['dashboard']
            for i in res:
                print(i)
        else:
            return False

    def get_all_alert(self):
        """
        获取所有告警列表
        """
        api_url = self.base_url + '/api/alerts'
        response = requests.get(api_url, headers=self.headers, verify=False, timeout=120)
        print(response)
        if response.status_code == 200:
            res = response.json()
            print(res)
            for i in res:
                # print(i + ':' + str(res[i]))
                print(i)
        else:
            return False
    def get_all_alert_new(self):
        """
        获取所有告警列表
        """
        api_url = self.base_url + '/api/v1/provisioning/alert-rules'
        response = requests.get(api_url, headers=self.headers, verify=False, timeout=120)
        print(response)
        if response.status_code == 200:
            res = response.json()
            for i in res:
                print(i)
        else:
            return False

    def pause_alert(self):
        """
        暂停指定告警
        """
        data = {
            "pause": 'true'
        }
        api_url = self.base_url + '/api/alerts/16/pause'
        response = requests.delete(api_url, headers=self.headers, json=data)
        if response.status_code == 200:
            res = response.json()
            print(res)
            return res
        else:
            return False
    def delete_all_alert(self):
        """
        暂停指定告警
        """
        # data = {
        #     "paused": 'true'
        # }
        # {"password": "userpassword"}
        api_url = self.base_url + '/api/alert-notifications/16'
        response = requests.delete(api_url, headers=self.headers, verify=False, timeout=120)
        if response.status_code == 200:
            res = response.json()
            print(res)
            return res
        else:
            return False

