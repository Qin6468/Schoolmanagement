
class Base(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/educational?charset=utf8' #用于连接数据的数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True   #如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_RECORD_QUERIES = True        #可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用。
    SQLALCHEMY_POOL_SIZE = 1024             #数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）
    SQLALCHEMY_POOL_TIMEOUT = 90            #指定数据库连接池的超时时间
    SQLALCHEMY_POOL_RECYCLE = 3             #自动回收连接的秒数。这对 MySQL 是必须的，默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。 需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。
    SQLALCHEMY_MAX_OVERFLOW = 1024          #控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。
    
    SALT='IloveYou'#加密盐
    SECRET_KEY='b1bb9c4fe0d5984d26e13d4a091199b2'
class Dev(Base):
    DEBUG=True
class Pro(Base):
    DEBUG=False
