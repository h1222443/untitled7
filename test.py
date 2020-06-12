from typing import Dict,List
from collections import defaultdict


_handlers: defaultdict = defaultdict(list)
hand:Dict[str,List] = {}


_handlers['hao'].append(99)
_handlers['hao'].append("87")
print(_handlers)
print(_handlers['hao'])