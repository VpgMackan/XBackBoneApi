import requests
from lxml.html import fromstring

class XBackBoneApi:
    def __init__(self, token, base_url, xpath_expression="/html/body/div[1]/div[2]/div"):
        self.BASE_URL = base_url
        self.TOKEN = token
        self.XPATH_EXPRESSION = xpath_expression
        self.session = requests.Session()
        self.session.headers.update({'token': self.TOKEN})

    def make_request(self, method, url, files=None, cookies=None, data=None):
        full_url = self.BASE_URL + url
        response = self.session.request(method, full_url, data=data, files=files, cookies=cookies)
        response.raise_for_status()
        return response

    def upload_image(self, file_path):
        with open(file_path, "rb") as file:
            response = self.make_request("POST", "/upload", files={"file": file})
        return response.json()

    def get_home_data(self, session_cookie):
        response = self.make_request("GET", "/home", cookies={"xbackbone_session": session_cookie})
        return response.text

    def add_tag(self, tag, media_id, session_cookie):
        data = {"tag": tag, "mediaId": media_id}
        cookies = {"xbackbone_session": session_cookie}
        response = self.make_request("POST", "/tag/add", data=data, cookies=cookies)
        return response.json()

    def get_latest_id(self, session_cookie):
        elements = fromstring(self.get_home_data(session_cookie)).xpath(self.XPATH_EXPRESSION)
        return elements[0].get("data-id")