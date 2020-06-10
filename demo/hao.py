from peewee import *
import datetime
from abc import ABC,abstractmethod


class ModelBase(Model):

    def to_dict(self):
        return self.__data__

class mo(ABC):

    @abstractmethod
    def clean(self, symbol: str):
        """
        delete all records for a symbol
        """
        pass

class moo(mo):
    def clean(self,symbol:str):
        pass

def funmoo():
    return moo()