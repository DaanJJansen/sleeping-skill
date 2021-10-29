from mycroft import MycroftSkill, intent_file_handler

import requests


class Sleeping(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sleeping.intent')
    def handle_sleeping(self, message):
        self.speak_dialog('sleeping')


def create_skill():
    return Sleeping()

