import pyodbc
class Db:
    def __init__(self):
        self.tableName = ''
        self.where = ''
        self.limit = 10
        self.offset = 1
        self.distincy = ''#不重复值查询
        self.sql = ''
        conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=DESKTOP-IKDGO3K\SQLEXPRESS;DATABASE=gserver_201703;UID=sa;PWD=zxx')
        self.cursor = conn.cursor()
    def table(self, name):
        self.tableName = name
        return self
    def setWhere(self, arr): #[['key','op','value'],[]]
        for elem in arr:
            if(self.where != ''):
                self.where = self.where + ' AND ' + elem[0] + elem[1] + elem[2]
            else: ##init where
                self.where = elem[0] + elem[1] + elem[2]
        return self
    def select(self,keysStr = '*'): #'keysStr' = 'name time' like this
        #select   top   y   *   from   表   where   主键   not   in(select   top   (x-1)*y   主键   from   表)  
        if(keysStr != '*'):
            keysStr = 'id,' + keysStr
        self.str = 'select ' + self.distincy + ' top ' + str(self.limit) + ' ' + keysStr +' from ' + self.tableName + \
            ' where id not in ('+'select ' + self.distincy + ' top ' + str((self.offset - 1)*self.limit) + ' id from ' + \
            self.tableName + ')'
            ### select top 500 id,VehicleID,lng,lat,posinfo,cstate,recvtime from gps_20170302 
            ### where id not in (select top 23000 id from gps_20170302) AND VehicleID=8509726
        if (self.where == ''):
            print(self.str)
            self.cursor.execute(self.str)
        else:
            self.str = 'select ' + self.distincy + ' top ' + str(self.limit) + ' ' + keysStr +' from ' + self.tableName + \
            ' where id not in ('+'select ' + self.distincy + ' top ' + str((self.offset - 1)*self.limit) + ' id from ' + \
            self.tableName + ' where ' + self.where + ')'
            print(self.str + ' AND ' + self.where)
            self.cursor.execute(self.str + ' AND ' + self.where)
        return self.cursor.fetchall()
    def setLimit(self, offset, limit):
        self.offset = offset
        self.limit = limit
        return self
    def execSql(self,sqlstr):
        self.cursor.execute(sqlstr)
        return self.cursor.fetchall()
    def setDistincy(self):##不要使用这个函数，有bug
        self.distincy = 'DISTINCT'
        return self



# b = 0
# for i in Vehicle('8509726').getPosition('2017-03-02'):
#     b += 1
#     print(i[0])
#print(next(Vehicle('8509726').getPosition('2017-03-02'))[0])
