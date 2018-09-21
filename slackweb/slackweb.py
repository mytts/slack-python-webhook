# -*- coding: utf-8 -*-
import requests

class Slack():

    def __init__(self, url="", proxies=None):
        self.url = url
        self.proxies = proxies

    def notify(self, **kwargs):
        """
        Send message to slack API
        """
        return self.send(kwargs)

    def send(self, payload):
        """
        Send payload to slack API
        """
        response = requests.post(self.url, json=payload, proxies=self.proxies, headers={
                                 'Content-Type': 'application/json'})
        return response.text
