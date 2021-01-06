from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db, Course,Class
from jsjy.public import r
from sqlalchemy import distinct

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

	j_data.setdefault('info','')
	cl = Course(j_data['c_id'],j_data['name'],j_data['credit'],j_data['college'],j_data['semester_hour'],j_data['number'],j_data['time'],j_data['info'],j_data['local'])
	db.session.add(cl)
	db.session.commit()
	set_course_count(j_data['c_id'])
	return r({},0,'添加成功')

def set_course_count(c_id):
	if c_id>0:
		count=db.session.query(Course).filter_by(c_id=c_id).count()
		# tc = db.session.query(Class).filter_by(id=c_id).first()
		# 课程数
		tc.course_count=count
		db.session.commit()
	return True

@course.route('/courselist/minlist',methods=['GET'])
def get_minlist():
	# data =db.session.query(distinct(Course.college)).all()
	data=db.session.query(Course.c_id,Course.college).order_by(Course.college.desc()).all()
	re=[]
	for x in data:
		re.append({'label':x[1],'value':x[0]})
	return r({'courseopt':re})