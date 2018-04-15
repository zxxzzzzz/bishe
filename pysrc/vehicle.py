from pysrc.sqlserver import Db
class Vehicle: #数据库里车辆对象的数据整合
    def __init__(self, id):#id为车辆id
        self.id = id
    def get(self, time):#用来获取数据
        pass
    def setId(self, id):
        self.id = id
    # time = 2017-12-01 这种格式
    def getPosition(self, time = '',offset = 1, limit =10):#返回[{lng:xx,lat:xx,posinfo:xxx,cstate:xxx,time:xxxx}]
        selectKeys = 'VehicleID,lng,lat,posinfo,cstate,recvtime'
        timeArr = time.split('-')
        year = timeArr[0]
        month = timeArr[1]
        day = timeArr[2]
        tablename = 'gps_' + year + month + day
        data = Db().table(tablename).setLimit(offset,limit).setWhere([['VehicleID','=',self.id]]).select(selectKeys)  
        positionmap = []
        if data == {}:
            return []
        for elem in data:
            positionmap.append({})
            positionmap[-1]['VehicleID'] = elem[1]
            positionmap[-1]['lng'] = elem[2]
            positionmap[-1]['lat'] = elem[3]
            positionmap[-1]['posinfo'] = elem[4]
            positionmap[-1]['cstate'] = elem[5]
            positionmap[-1]['recvtime'] = str(elem[6])
        return positionmap
    

