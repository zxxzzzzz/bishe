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
        try:
            if(self.iterationX[tag] == None): ##内部迭代器，用来做大量数据传输，分成一段一段的
                self.iterationX[tag] = Vehicle(queryMap['id']).getPosition(queryMap['time'])
            temp = next(self.iterationX[tag])
        except StopIteration: ##迭代结束后会抛出异常，捕获，然后去除迭代器
            self.iterationX[tag] = None
            return '{"end":1}'
        re = {}
        re['end'] = 0
        re['data'] = temp
        return json.dumps(re)