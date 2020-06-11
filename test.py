from dataclasses import dataclass


@dataclass
class a:

    eqq:str
    qqe:str

    def __post_init__(self):
        """"""
        self.vt_symbol = f"{self.eqq}.{self.qqe}"


tick = a(eqq = 'hao',qqe = 'wei')





print(tick.__getattribute__('vt_symbol'))