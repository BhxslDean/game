import pymysql
'''mysql用户类'''
class mysqlpython(object):
    def __init__(self,database,host='localhost',user='root',password='123456',charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.database = database
    
    def myopen(self):
        self.db = pymysql.connect(host=self.host,user=self.user,password=self.password,charset=self.charset,database=self.database)
        self.cur = self.db.cursor()

    def myclose(self):
        self.cur.close()
        self.db.close()

    def do(self,order,lst=None):
        if lst == None:
            lst = []
        self.myopen()
        self.cur.execute(order,lst)
        self.db.commit()
        self.myclose()

    def getall(self,order,lst=None):
        if lst == None:
            lst = []
        self.myopen()
        self.cur.execute(order,lst)
        result = self.cur.fetchall()
        self.myclose()
        return result

        
