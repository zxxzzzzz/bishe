from sqlserver import Db
import csv
'''
这个模块用来做数据整理，把数据库里的数据进行筛选，然后保存为csv格式
'''
class DataFilter:
    def __init__(self):
        pass
    def saveAllVehicleID(self,time):#time表示2017-03-02之类
        timeArr = time.split('-')
        year = timeArr[0]
        month = timeArr[1]
        day = timeArr[2]
        a = set() ##生成set保存id
        with open('AllVehicleID.csv') as f:
            reader = csv.reader(f)
            temp = list(reader)
            ii = 0
            for i in temp:
                if ii != 0:
                    a.add(i[0])
                ii += 1
                
        tablename = 'gps_' + year + month + day
        temp = Db().execSql('select DISTINCT VehicleID from ' + tablename)
        for i in temp:##添加id,如果重复就不添加，这是set的特性
            a.add(str(i[0]))
        data = list(a)
        data2 = [['vehicleID']]##添加字段头
        for i in data:
            data2.append([i]) ##添加set里的数据
        with open('AllVehicleID.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for row in data2:
                    writer.writerow(row)
    def savePath(self, vehicleID, time):
        timeArr = time.split('-')
        year = timeArr[0]
        month = timeArr[1]
        day = timeArr[2]
        tablename = 'gps_' + year + month + day
        data = Db().execSql('select recvtime,lng,lat from ' + tablename + ' where VehicleID='+vehicleID)
        data.insert(0,['recvtime','lng','lat'])
        with open('path-'+time+'-'+vehicleID+'.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
    def saveSpeed(self, vehicleID, time):
        timeArr = time.split('-')
        year = timeArr[0]
        month = timeArr[1]
        day = timeArr[2]
        tablename = 'gps_' + year + month + day
        data = Db().execSql('select recvtime,veo from ' + tablename + ' where VehicleID='+vehicleID)
        data.insert(0,['recvtime','veo'])
        with open('speed-'+time+'-'+vehicleID+'.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
DataFilter().savePath('6784381','2017-03-02')