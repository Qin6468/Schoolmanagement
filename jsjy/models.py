from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    """用户表
    """
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    salt = db.Column(db.String(32), nullable=False)
    level = db.Column(db.Integer)
    name = db.Column(db.String(60), nullable=False)
    status = db.Column(db.Integer)

    def __init__(self, admin, password,salt,level,name,status):
    	self.admin=admin
    	self.password=password
    	self.salt=salt
    	self.level=level
    	self.name=name
    	self.status=status

    def __repr__(self):
        return '<id %r>' % self.id
class Teacher(db.Model):
    """
    	教师
    """
    id = db.Column(db.Integer, primary_key=True)
    a_id = db.Column(db.Integer)
    name = db.Column(db.String(60), nullable=False)
    cid = db.Column(db.String(18), nullable=False)
    in_time = db.Column(db.Integer)
    out_time = db.Column(db.Integer)
    oa_time = db.Column(db.Integer)
    info = db.Column(db.Text, nullable=False)

    def __init__(self, a_id,name,cid,in_time,out_time,oa_time,info):
    	self.a_id=a_id
    	self.name=name
    	self.cid=cid
    	self.in_time=in_time
    	self.out_time=out_time
    	self.oa_time=oa_time
    	self.info=info

    def __repr__(self):
        return '<Teacher id %r>' % self.id

class Class(db.Model):
    """
        教师
    """
    id = db.Column(db.Integer, primary_key=True)
    t_id = db.Column(db.Integer)
    # t_id = db.Column(db.Integer, db.ForeignKey('Teacher.a_id'))
    name = db.Column(db.String(60), nullable=False)
    addtime = db.Column(db.Integer)
    user_count = db.Column(db.Integer)

    def __init__(self, t_id,name,addtime,user_count):
        self.t_id=t_id
        self.name=name
        self.addtime=addtime
        self.user_count=user_count

    def __repr__(self):
        return '<Class id %r>' % self.id
class Student(db.Model):
    """
    学生
    """
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer)
    # class_id = db.Column(db.Integer, db.ForeignKey('Class.id'))
    name = db.Column(db.String(60), nullable=False)
    code = db.Column(db.String(20), nullable=False)
    cid = db.Column(db.String(18), nullable=False)
    in_time = db.Column(db.Integer)
    out_time = db.Column(db.Integer)
    info = db.Column(db.Text, nullable=False)
    l_name = db.Column(db.String(60), nullable=False)
    l_phone = db.Column(db.String(11), nullable=False)
    l2_name = db.Column(db.String(60), nullable=False)
    l2_phone = db.Column(db.String(11), nullable=False)
    add = db.Column(db.String(255), nullable=False)

    def __init__(self, class_id,name,code,cid,in_time,out_time,info,l_name,l_phone,l2_name,l2_phone,add):
    	self.class_id=class_id
    	self.name=name
    	self.code=code
    	self.cid=cid
    	self.in_time=in_time
    	self.out_time=out_time
    	self.info=info
    	self.l_name=l_name
    	self.l_phone=l_phone
    	self.l2_name=l2_name
    	self.l2_phone=l2_phone
    	self.add=add

    def __repr__(self):
        return '<Student id %r>' % self.id

class Score(db.Model):
    """
    学生
    """
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    # uid = db.Column(db.Integer, db.ForeignKey('Student.id'))
    score = db.Column(db.Float(3,1), nullable=False)
    k_time = db.Column(db.Integer)
    kskc = db.Column(db.String(60), nullable=False)
    def __init__(self, uid,score,k_time,kskc):
    	self.uid=uid
    	self.score=score
    	self.kskc=kskc
    	self.k_time=k_time
    def __repr__(self):
        return '<Student id %r>' % self.id

class Course(db.Model):
    """
    课程
    """
    c_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    college = db.Column(db.String(20), nullable=False)
    credit = db.Column(db.Integer)
    semester_hour = db.Column(db.Integer)
    number=db.Column(db.Integer)
    time = db.Column(db.String(60), nullable=False)
    local=db.Column(db.String(60), nullable=False)
    info = db.Column(db.Text, nullable=False)

    def __init__(self,name,college,credit,semester_hour,number,time,local,info):
    	self.name=name
    	self.college=college
    	self.credit=credit
    	self.semester_hour=semester_hour
    	self.number=number
    	self.time=time
    	self.local=local
    	self.info=info

    def __repr__(self):
        return '<Course c_id %r>' % self.c_id

class cc(db.Model):
    """
    班级课程表
    """
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, db.ForeignKey('Course.c_id'))
    class_id = db.Column(db.Integer, db.ForeignKey('Class.id'))

    def __init__(self, c_id, class_id):
        self.c_id = c_id
        self.class_id = class_id
    
    def __repr__(self):
        return '<Course id %r>' % self.id

class sc(db.Model):
    """
    学生成绩表
    """
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('Student.id'))
    cid = db.Column(db.Integer, db.ForeignKey('Course.c_id'))
    gid = db.Column(db.Integer, db.ForeignKey('Score.id'))

    def __init__(self, uid, c_id, gid):
        self.uid = uid
        self.c_id = c_id
        self.gid = gid
    
    def __repr__(self):
        return '<Student id %r>' % self.id

class tc(db.Model):
    """
    老师课程表
    """
    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer, db.ForeignKey('Teacher.a_id'))
    cid = db.Column(db.Integer, db.ForeignKey('Course.c_id'))

    def __init__(self, tid, c_id):
        self.tid = tid
        self.c_id = c_id
    
    def __repr__(self):
        return '<Teacher id %r>' % self.id

