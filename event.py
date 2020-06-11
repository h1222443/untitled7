from typing import Any


class Event:
    def __init__(self,type:str,data:Any):
        self.type = type
        self.data = data


class EventEngine:
    def register(self,event_type,handler):
        pass