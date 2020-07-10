"""

Desc:               工厂方法(简化创建对象,为客户端隐藏创建细节,侧重于创建结果;
                            优点:符合开闭原则,单一职责.
                            缺点:每进行一次扩展都会引入一个工厂类
                            应用:简单的产品关系,明确创建的产品类型,不关注创建细节)
CreatedOn:          2020/6/17 10:33
Author:             wut
"""

from abc import abstractmethod


class DB:
    def __init__(self, host, port, conn_str=None):
        self.host = host
        self.port = port
        self.conn_str = conn_str

    @abstractmethod
    def get_conn(self):
        raise Exception("not connection")


class MySQL(DB):
    def __init__(self, host, port):
        super(MySQL, self).__init__(host, port)

    def get_conn(self):
        return 'Mysql Conn'


class Mongo(DB):
    def __init__(self, host, port):
        super(Mongo, self).__init__(host, port)

    def get_conn(self):
        return 'Mongo Conn'


if __name__ == "__main__":
    mongo_conn = Mongo('127.0.0.1', '9042').get_conn()
    print(mongo_conn)
