from typing import Optional, Dict, Any
import requests
from lxml.html import fromstring

UPLOAD_ENDPOINT = "/upload"
HOME_ENDPOINT = "/home"
TAG_ADD_ENDPOINT = "/tag/add"


class XBackBoneApi:
    def __init__(self, token: str, base_url: str, session_cookie: Optional[str] = None):
        """
        Initialize the XBackBoneApi class.

        :param token: The token to use for authentication.
        :param base_url: The base URL for the API.
        :param session_cookie: The session cookie, if any.
        """
        self.BASE_URL = base_url
        self.TOKEN = token
        self.SESSION_COOKIE = session_cookie
        self.session = requests.Session()
        self.session.headers.update({"token": self.TOKEN})

        if self.BASE_URL.endswith("/"):
            self.BASE_URL = self.BASE_URL[:-1]

    def make_request(
        self,
        method: str,
        endpoint: str,
        files: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """
        Make a request to the API.

        :param method: The HTTP method to use.
        :param endpoint: The API endpoint to hit.
        :param files: The files to send with the request, if any.
        :param data: The data to send with the request, if any.
        :return: The response from the server.
        """
        full_url = f"{self.BASE_URL}{endpoint}"
        cookies = (
            {"xbackbone_session": self.SESSION_COOKIE} if self.SESSION_COOKIE else None
        )

        # Ensure the token is always included in the data payload
        if data is None:
            data = {}
        data["token"] = self.TOKEN

        response = self.session.request(
            method, full_url, data=data, files=files, cookies=cookies
        )
        response.raise_for_status()
        return response

    def upload_image(self, file_path: str) -> Dict[str, Any]:
        """
        Upload an image to the server.

        :param file_path: The path to the image file.
        :return: The response from the server.
        """
        with open(file_path, "rb") as file:
            response = self.make_request("POST", UPLOAD_ENDPOINT, files={"file": file})
        return response.json()

    def get_home_data(self) -> str:
        """
        Get the home data from the server.

        :return: The home data.
        """
        response = self.make_request("GET", HOME_ENDPOINT)
        return response.text

    def add_tag(self, tag: str, media_id: str) -> Dict[str, Any]:
        """
        Add a tag to a media item.

        :param tag: The tag to add.
        :param media_id: The ID of the media item.
        :return: The response from the server.
        """
        data = {"tag": tag, "mediaId": media_id}
        response = self.make_request("POST", TAG_ADD_ENDPOINT, data=data)
        return response.json()

    def get_latest_id(self) -> str:
        """
        Get the latest ID from the server.

        :return: The latest ID.
        """
        elements = fromstring(self.get_home_data()).xpath(
            "/html/body/div[1]/div[2]/div"
        )
        return elements[0].get("data-id")
