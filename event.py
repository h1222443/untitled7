from typing import Any,Dict,List
from queue import Queue,Empty
from threading import Thread
from collections import defaultdict
from time import sleep
from object import *
from datetime import datetime


EVENT_TICK = "eTick."
EVENT_TRADE = "eTrade."
EVENT_ORDER = "eOrder."
EVENT_POSITION = "ePosition."
EVENT_ACCOUNT = "eAccount."
EVENT_CONTRACT = "eContract."
EVENT_LOG = "eLog"

class Event:
    def __init__(self,type:str,data:Any):
        self.type = type
        self.data = data


class EventEngine:
    def __init__(self):
        self.thread_product = Thread(target=self.run_product)
        self.thread_consumer = Thread(target=self.run_consumer)
        self.queue_ = Queue()
        self.interval = 1
        self.handlers:defaultdict = defaultdict(list)
        self.active = False
        self.start()


    def run_product(self):
        a = 0
        while self.active:

            a += 10
            sleep(self.interval)
            DATA = data(
                class_= 'hao',
                name='weihua',
                sex=True,
                age=18,
                salary = a + self.interval,
                time=datetime.now()
            )
            event = Event(EVENT_TICK,DATA)
            self.queue_.put(event)

    def run_consumer(self):
        while self.active:
            try:
                event = self.queue_.get(block=True,timeout=2)
                self._process(event)
            except Empty:
                pass

    def _process(self,event:Event):

        if event.type in self.handlers:
            [handler(event) for handler in self.handlers[event.type]]



    def start(self):
        self.active = True
        self.thread_product.start()
        self.thread_consumer.start()


    def register(self,event_type:str,handler):
        handler_list = self.handlers[event_type]
        if handler not in handler_list:
            handler_list.append(handler)



