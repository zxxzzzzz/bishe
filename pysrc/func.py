import json
from pysrc.vehicle import Vehicle
class Func:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Func, cls).__new__(cls, *args, **kwargs)
            cls._instance.iterationX = {##迭代器字典，用来防止迭代器冲突
                'vehicle':None,
            }
        return cls._instance
    #param为?后面的参数，是个字典{a:xxx,b:xxx}
    def vehicle(self,queryMap):
        tag = 'vehicle'
        re = {}
        re['data'] = Vehicle(queryMap['id']).getPosition(queryMap['time'],int(queryMap['offset']),int(queryMap['limit']))
        return json.dumps(re)