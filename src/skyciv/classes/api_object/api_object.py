
import json
from typing import Literal
from classes.auth.auth_object import AuthObject
from classes.functions.api_functions import ApiFunctions
from classes.options.options_object import OptionsObject
from utils.helpers import clone, keyvals

from lib.request import request


class ApiObject:
    def __init__(self):
        """Create an instance of the SkyCiv API Object.
        """
        self.auth = AuthObject()
        self.options = OptionsObject()
        self.functions = ApiFunctions()

    def request(self, http_or_https: Literal["https", "http"] = 'https', version: int = 3):
        """Send the ApiObject to the SkyCiv API.

        Args:
            http_or_https (str, optional): Whether to use http or https. {"http" | "https"}. Defaults to 'https'.
            version (int, optional): API version. {2 | 3}. Defaults to 3.
        """
        return request(self.to_json(), {http_or_https, version})

    def get(self) -> dict:
        """Converts the ApiObject into a Python dictionary that will parse to JSON in the SkyCiv format.

        Returns:
            dict: The API object as a Python dictionary.
        """
        api_object = {
            "auth": clone(self.auth.get()),
            "options": clone(self.options.get()),
            "functions": clone(self.functions.get()),
        }
        return api_object

    def to_json(self) -> str:
        model = self.get()
        return json.dumps(model)
