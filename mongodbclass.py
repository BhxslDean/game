'''
自定义的mongodb操作类
'''
import pymongo
import bson.binary

class MyMongo(object):
    def __init__(self,database,host='localhost',port=27017):
        self.database = database
        self.host = host
        self.port = port

    def open(self,collection=None):
        if collection is None:
            print('未选择打开集合，已退出执行程序')
            return
        self.conn = pymongo.MongoClient(self.host,self.port)
        self.db = self.conn[self.database]
        self.col = self.db[collection]

    def close(self):
        self.conn.close()

    def collection_judge(self):
        dblist = self.conn.database_names()
        if self.database in dblist:
            print('正在操作已有数据库')
        else:
            print('正在操作新建数据库')

    def myinsert(self,msg,collection=None):
        self.open(collection)
        self.collection_judge()
        self.col.insert(msg)
        print('插入成功')
        self.close()

    def myupdate(self,query,msg,upins=False,upmul=False,collection=None):
        self.open(collection)
        self.collection_judge()
        self.col.update(query,msg,upsert=upins,multi=upmul)
        print('修改成功')
        self.close()
    
    def mydelete(self,query,delmul=False,collection=None):
        self.open(collection)
        self.collection_judge()
        if delmul is False:
            ret = self.col.delete_one(query)
            print('删除笔数:{}'.format(ret.delete_count()))
        elif delmul is True:
            ret = self.col.delete_many(query)
            print('删除笔数:{}'.format(ret.delete_count()))
        else:
            print('指令错误')
        self.close()
    
    def myfind(self,query,collection,fun=0,query2={'_id':0}):
        self.open(collection)
        self.collection_judge()
        if fun:
            docs = self.col.find(query,query2).fun
        else:
            docs = self.col.find(query,query2)
        for doc in docs:
            print(doc)
        self.close()

    def myaggregate(self,cmd,collection,fun=0):
        self.open(collection)
        self.collection_judge()
        if fun:
            docs = self.col.aggregate(query).fun
        else:
            docs = self.col.aggregate(query)
        for doc in docs:
            print(doc)
        self.close()





