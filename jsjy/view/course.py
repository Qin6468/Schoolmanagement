from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db, Course,Class
from jsjy.public import r

course=Blueprint('course',__name__)

@course.route('/course')
def index():
	return render_template('/course.html')
@course.route('/course',methods=['POST'])

#获取课程
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
	where=[Course.c_id>0]
	for k,v in search.items():
		if v:
			temp1=getattr(Course,k).like("%"+v+"%")
			where.append(temp1)

	# if in_time :
	# 	temptime=in_time.split(',')
	# 	where.append(course.in_time>=temptime[0])
	# 	where.append(course.in_time<=temptime[1])
	# tc = db_tc.order_by(order).filter(*where).limit(perPage).offset(offset)#.all()
	# print(tc)
	# for t in tc:
	# 	temp.append({
	# 	'c_id':t.c_id,
	# 	'name':t.name,
	# 	'college':t.college,
	# 	'credit':t.credit,
	# 	'semester_hour':t.semester_hour,
	# 	'number':t.number,
    #     'time':t.time,
    #     'local':t.local,
	# 	'info':t.info
	# 	})

	rt['count']=count
	rt['rows']=temp
	# rt['hasNext']=1
	return r(rt)
	pass

def set_class_count(class_id):
	if class_id>0:
		count=db.session.query(course).filter_by(c_id=c_id).count()
		tc = db.session.query(Class).filter_by(id=c_id).first()
		tc.user_count=count
		db.session.commit()
	return True