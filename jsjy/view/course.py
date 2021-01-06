from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db, Course,Class
from jsjy.public import r

course=Blueprint('course',__name__)

@course.route('/course')
def index():
	return render_template('/course.html')
@course.route('/course',methods=['POST'])

#获取课程 (1.5修改bug成功能实现数据的获取)
@course.route('/courselist',methods=['GET'])
def get_course():
	perPage=int(request.values.get('perPage'))
	page=int(request.values.get('page'))
	c_id=request.values.get('c_id')
	search={}
	search['name']=request.values.get('name')
	search['college']=request.values.get('college')
	search['credit']=request.values.get('credit')
	search['semester_hour']=request.values.get('semester_hour')
	search['number']=request.values.get('number')
	search['time']=request.values.get('time')
	search['local']=request.values.get('local')
	search['info']=request.values.get('info')
	orderBy=request.values.get('orderBy')
	orderDir=request.values.get('orderDir')

	count=db.session.query(Course).count()
	db_tc=db.session.query(Course)
	offset=((page-1)*perPage)
	rt={}
	ids=[]
	temp=[]
	order=Course.c_id.desc()
	if orderBy and orderDir:#排序
		temp1=getattr(Course,orderBy)
		order=getattr(temp1,orderDir)()
	db_tc.order_by(order)
	where=[Course.c_id>0]
	for k,v in search.items():
		if v:
			temp1=getattr(Course,k).like("%"+v+"%")
			where.append(temp1)
	
	tc = db_tc.order_by(order).filter(*where).limit(perPage).offset(offset) 
	for t in tc:
		temp.append({
		'id':t.id,
		'c_id':t.c_id,
		'name':t.name,
		'credit':t.credit,
		'college':t.college,
		'semester_hour':t.semester_hour,
		'number':t.number,
		'time':t.time,
		'local':t.local,
		'info':t.info
		})
	rt['count']=count
	rt['rows']=temp
	# rt['hasNext']=1
	return r(rt)
	pass
#添加课程
@course.route('/course',methods=['POST'])
def add_course():
	data = request.get_data()
	j_data =  json.loads(data)
	user=db.session.query(Course).filter_by(c_id=j_data['c_id']).first()
	if user is not None:
		return r({},0,'',{'c_id':'课程已经存在'})

	j_data.setdefault('l2_name','')
	j_data.setdefault('l2_phone','')
	j_data.setdefault('add','')
	j_data.setdefault('code','')
	j_data.setdefault('info','')
	cl = course(j_data['class_id'],j_data['name'],j_data['code'],j_data['cid'],j_data['in_time'],0,j_data['info'],j_data['l_name'],j_data['l_phone'],j_data['l2_name'],j_data['l2_phone'],j_data['add'])
	db.session.add(cl)
	db.session.commit()
	set_class_count(j_data['class_id']);
	return r({},0,'添加成功')

def set_class_count(class_id):
	if class_id>0:
		count=db.session.query(course).filter_by(c_id=c_id).count()
		tc = db.session.query(Class).filter_by(id=c_id).first()
		tc.user_count=count
		db.session.commit()
	return True