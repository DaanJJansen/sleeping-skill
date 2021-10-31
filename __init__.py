from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_number

import requests


class Sleeping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.command_headers = {"Content-type": "text/plain"}
        self.url = "http://192.168.2.7:8087/rest"

    @intent_handler('sleeping.intent')
    def handle_sleeping(self, message):
        requestUrl = self.url+"/items/sleeping"
        req = requests.post(requestUrl, data="ON", headers=self.command_headers)        
        self.speak_dialog('sleeping')
        
    @intent_handler('door.intent')
    def handle_door(self, message):
        requestUrl = self.url+"/items/door_lock"
        req = requests.post(requestUrl, data="ON", headers=self.command_headers)        
        self.speak_dialog('door')
        
        
    @intent_handler('speakervolume.intent')
    def handle_door(self, message):
        utterance = message.data.get('utterance')
        volume = int(extract_number(utterance))
        
        if volume.isnumeric() and 0 <= volume <= 30:
            requestUrl = self.url+"/items/OnkyoVolume"
            req = requests.post(requestUrl, data="volume", headers=self.command_headers)        
            self.speak_dialog('speakervolume', data={
                'volume': volume
            })
        else:
            self.speak_dialog('speakervolume.err', data={
                'volume': volume
            })

def create_skill():
    return Sleeping()

