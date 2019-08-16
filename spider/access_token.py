import json
import requests
from utils import config


class AccessToken:

    def __init__(self):
        self.config = config.Config()

    def _get_token(self):

        domain = self.config.get_cfg_value("ROUTE", "domain")
        open_route = self.config.get_cfg_value("ROUTE", "open_api_url")
        token = self.config.get_cfg_value("ROUTE", "token")

        grant_type = self.config.get_cfg_value("COMMAND", "grant_type")
        client_id = self.config.get_cfg_value("COMMAND", "client_id")
        client_secret = self.config.get_cfg_value("COMMAND", "client_secret")

        url = '{}/{}/{}?grant_type={}&client_id={}&client_secret={}'.format(domain, open_route, token, grant_type, client_id, client_secret)

        headers = {
            "Host": self.config.get_cfg_value("HEADERS", "Host"),
            "App-Slug": self.config.get_cfg_value("HEADERS", "App-Slug"),
            "Connection": self.config.get_cfg_value("HEADERS", "Connection"),
            "Accept": self.config.get_cfg_value("HEADERS", "Accept"),
            "sid": self.config.get_cfg_value("HEADERS", "sid"),
            "User-Agent": self.config.get_cfg_value("HEADERS", "User-Agent"),
            "Referer": "https://neon.aihuishou.com/fenqile/",
            "Accept-Language": self.config.get_cfg_value("HEADERS", "Accept-Language"),
            "Accept-Encoding": self.config.get_cfg_value("HEADERS", "Accept-Encoding"),
        }

        result = requests.get(url, headers=headers)
        result = json.loads(result.text)

        expires_in = result['expires_in']
        access_token = result['access_token']

        return {"expires":expires_in, "token": access_token}

