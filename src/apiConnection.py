import http.client
import json
import src.constant as constant


class ApiConnection:
    def __init__(self):
        self.__headers = {'X-Auth-Token': '5329e4dea68b4adcb38f2ebbaa0868a3'}
        self.__baseUrl = 'api.football-data.org'

    def get_all_standings(self):
        connection = self.__create_connection()
        connection.request('GET', constant.STANDINGS, None, self.__headers)
        return json.loads(connection.getresponse().read().decode())

    def get_all_matches(self):
        connection = self.__create_connection()
        connection.request('GET', constant.MATCHES, None, self.__headers)
        return json.loads(connection.getresponse().read().decode())

    def __create_connection(self):
        return http.client.HTTPConnection(self.__baseUrl)
