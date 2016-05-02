import json


class ActionResponse(object):
    def __init__(self):
        self.count = 0
        self.messages = []
        self.forced = None
        self.keyboard = None
        self.entities = None

    def to_dict(self):
        res = {}
        res['Count'] = self.count
        res['Messages'] = self.messages
        res['ForcedState'] = self.forced
        res['ForcedKeyboard'] = self.keyboard
        res['Entities'] = self.entities
        return res


class ErrorResponse(ActionResponse):
    def __init__(self, message):
        ActionResponse.__init__(self)
        self.messages = [message]


class LinkedEntity:
    def __init__(self, d):
        self.name = d['name']  # Name of file
        self.desc = d['desc']  # Description of pic
        self.url = d['url'] # URL

    def __str__(self):
        d = dict()
        d['Handle'] = None
        d['Name'] = self.name
        d['ImageUrl'] = self.url
        d['Description'] = self.desc
        return json.dumps(d)

    def to_dict(self):
        res = {}
        res['Handle'] = ''
        res['Name'] = self.name
        res['ImageUrl'] = self.url
        res['Description'] = self.desc
        return res