from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db,Class
from jsjy.public import r
from sqlalchemy import distinct

evaluation=Blueprint('evaluation',__name__)

@evaluation.route('/evaluation')
def index():
	return render_template('/evaluation.html')

#获取课程 (1.5修改bug成功能实现数据的获取)
@evaluation.route('/evaluationlist',methods=['GET'])
def get_evaluation():
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

	count=db.session.query(evaluation).count()
	db_tc=db.session.query(evaluation)
	offset=((page-1)*perPage)
	rt={}
	ids=[]
	temp=[]
	order=evaluation.c_id.desc()
	if orderBy and orderDir:#排序
		temp1=getattr(evaluation,orderBy)
		order=getattr(temp1,orderDir)()
	db_tc.order_by(order)
	where=[evaluation.c_id>0]
	for k,v in search.items():
		if v:
			temp1=getattr(evaluation,k).like("%"+v+"%")
			where.append(temp1)
	
	tc = db_tc.order_by(order).filter(*where).limit(perPage).offset(offset) 
	for t in tc:
		temp.append({
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
@evaluation.route('/evaluation',methods=['POST'])
def add_evaluation():
	data = request.get_data()
	j_data =  json.loads(data)
	user=db.session.query(evaluation).filter_by(c_id=j_data['c_id']).first()
	if user is not None:
		return r({},0,'',{'c_id':'课程已经存在'})

	j_data.setdefault('info','')
	cl = evaluation(j_data['c_id'],j_data['name'],j_data['college'],j_data['credit'],j_data['semester_hour'],j_data['number'],j_data['time'],j_data['local'],j_data['info'])
	db.session.add(cl)
	db.session.commit()
	set_evaluation_count(j_data['c_id'])
	return r({},0,'添加成功')

#删除课程
@evaluation.route('/evaluationlist/<int:c_id>',methods=['DELETE'])
def delete_evaluation(c_id):
	tc = db.session.query(evaluation).filter_by(c_id=c_id).first()
	sql2=db.session.query(evaluation).filter_by(c_id=c_id).delete()
	db.session.commit()
	# set_evaluation_count(tc.c_id);
	return r({},0,'删除成功')

#修改
@evaluation.route('/evaluationlist/<int:c_id>',methods=['PUT'])
def edit_evaluation(c_id):
	data = request.get_data()
	j_data =  json.loads(data)
	
	tc = db.session.query(evaluation).filter_by(c_id=c_id).first()
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
def set_evaluation_count(c_id):
	if int(c_id)>0:
		count=db.session.query(evaluation).filter_by(c_id=c_id).count()
		tc = db.session.query(evaluation).filter_by(c_id=c_id).first()
		# 课程数
		tc.evaluation_count=count
		db.session.commit()
	return True

@evaluation.route('/evaluationlist/minlist',methods=['GET'])
def get_minlist():
	data = db.session.query(distinct(evaluation.college).label('college')).all()
	# data=db.session.query(evaluation.c_id,evaluation.college).order_by(evaluation.college.desc()).all()
	re=[]
	for x in data:
		re.append({'label':x[0],'value':x[0]})
		# re.append({'label':x[0]})
	return r({'evaluationopt':re})