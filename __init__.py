from mycroft import MycroftSkill, intent_file_handler

import requests


class Sleeping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.command_headers = {"Content-type": "text/plain"}
        self.url = "http://192.168.2.7:8087/rest"

    @intent_file_handler('sleeping.intent')
    def handle_sleeping(self, message):
        requestUrl = self.url+"/items/oppas"
        req = requests.post(requestUrl, data="ON", headers=self.command_headers)        
        self.speak_dialog('sleeping')


def create_skill():
    return Sleeping()

