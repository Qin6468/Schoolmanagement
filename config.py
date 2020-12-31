
class Base(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:990418@127.0.0.1:3306/dachuang?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_POOL_SIZE = 1024
    SQLALCHEMY_POOL_TIMEOUT = 90
    SQLALCHEMY_POOL_RECYCLE = 3
    SQLALCHEMY_MAX_OVERFLOW = 1024
    
    SALT='IloveYou'#加密盐
    SECRET_KEY='b1bb9c4fe0d5984d26e13d4a091199b2'
class Dev(Base):
    DEBUG=True
class Pro(Base):
    DEBUG=False
