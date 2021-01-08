from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db, Course,Class
from jsjy.public import r
from sqlalchemy import distinct

course=Blueprint('course',__name__)

@course.route('/course')
def index():
	return render_template('/course.html')

#获取课程 (1.5修改bug成功能实现数据的获取)
@course.route('/courselist',methods=['GET'])
def get_course():
	perPage=int(request.values.get('perPage'))
	page=int(request.values.get('page'))
	# id=request.values.get('id')
	# c_id=request.values.get('c_id')
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
	cl = Course(j_data['c_id'],j_data['name'],j_data['college'],j_data['credit'],j_data['semester_hour'],j_data['number'],j_data['time'],j_data['local'],j_data['info'])
	db.session.add(cl)
	db.session.commit()
	set_course_count(j_data['c_id'])
	return r({},0,'添加成功')

#删除课程
@course.route('/courselist/<int:c_id>',methods=['DELETE'])
def delete_course(c_id):
	tc = db.session.query(Course).filter_by(c_id=c_id).first()
	sql2=db.session.query(Course).filter_by(c_id=c_id).delete()
	db.session.commit()
	# set_course_count(tc.c_id);
	return r({},0,'删除成功')

#修改
@course.route('/courselist/<int:c_id>',methods=['PUT'])
def edit_course(c_id):
	data = request.get_data()
	j_data =  json.loads(data)
	
	tc = db.session.query(Course).filter_by(c_id=c_id).first()
	# old_class_id=0
	# flag=False
	# if tc.class_id != j_data['class_id']:
	# 	old_class_id=tc.class_id
	# 	flag=True
	# 	pass
	tc.name=j_data['name'],
	tc.credit=j_data['credit'],
	tc.college=j_data['college'],
	tc.semester_hour=j_data['semester_hour'],
	tc.number=j_data['number'],
	tc.time=j_data['time'],
	tc.local=j_data['local'],
	tc.info=j_data['info'],
	db.session.commit()
	# if flag:
	# 	set_class_count(j_data['class_id']);
	# 	if old_class_id >0:
	# 		set_class_count(old_class_id);
	return r({},0,'修改成功')

#修改课程数（暂时不清楚作用）
def set_course_count(c_id):
	if int(c_id)>0:
		count=db.session.query(Course).filter_by(c_id=c_id).count()
		tc = db.session.query(Course).filter_by(c_id=c_id).first()
		# 课程数
		tc.course_count=count
		db.session.commit()
	return True

@course.route('/courselist/minlist',methods=['GET'])
def get_minlist():
	data = db.session.query(distinct(Course.college).label('college')).all()
	# data=db.session.query(Course.c_id,Course.college).order_by(Course.college.desc()).all()
	re=[]
	for x in data:
		re.append({'label':x[0],'value':x[0]})
		# re.append({'label':x[0]})
	return r({'courseopt':re})