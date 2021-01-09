from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db, Thesis,Student,Teacher
from jsjy.public import r
from sqlalchemy import distinct

thesis=Blueprint('thesis',__name__)

@thesis.route('/thesis')
def index():
	return render_template('/thesis.html')

#获取课程 (1.5修改bug成功能实现数据的获取)
@thesis.route('/thesislist',methods=['GET'])
def get_thesis():
	perPage=int(request.values.get('perPage'))
	page=int(request.values.get('page'))
	# id=request.values.get('id')
	# t_id=request.values.get('t_id')
	search={}
	search['t_id']=request.values.get('t_id')
	search['sid']=request.values.get('sid')
	search['tid']=request.values.get('tid')
	search['topic']=request.values.get('topic')
	search['info']=request.values.get('info')
	search['status']=request.values.get('status')
	orderBy=request.values.get('orderBy')
	orderDir=request.values.get('orderDir')

	count=db.session.query(Thesis).count()
	# S=db.session.query(Student,Student.name.label('sname'))
	# T=db.session.query(Teacher,Teacher.name.label('tname'))
	db_tc=db.session.query(Thesis)
	offset=((page-1)*perPage)
	rt={}
	ids=[]
	temp=[]
	order=Thesis.t_id.desc()
	if orderBy and orderDir:#排序
		temp1=getattr(Thesis,orderBy)
		order=getattr(temp1,orderDir)()
	db_tc.order_by(order)
	where=[Thesis.t_id>0]
	for k,v in search.items():
		if v:
			temp1=getattr(Thesis,k).like("%"+v+"%")
			where.append(temp1)
	
	tc = db_tc.order_by(order).filter(*where).limit(perPage).offset(offset) 
	for t in tc:
		temp.append({
		't_id':t.t_id,
		'sid':t.sid,
		# 'sname':t.name,
		'tid':t.tid,
		# 'tname':t.name,
		'topic':t.topic,
		'info':t.info,
		'status':t.status
		})
	rt['count']=count
	rt['rows']=temp
	# rt['hasNext']=1
	return r(rt)
	pass

#添加课程
@thesis.route('/thesis',methods=['POST'])
def add_thesis():
	data = request.get_data()
	j_data =  json.loads(data)
	user=db.session.query(Thesis).filter_by(t_id=j_data['t_id']).first()
	if user is not None:
		return r({},0,'',{'t_id':'课题已经存在'})

	j_data.setdefault('info','')
	j_data.setdefault('sid','')
	j_data.setdefault('status','0')
	cl = Thesis(j_data['t_id'],j_data['sid'],j_data['tid'],j_data['topic'],j_data['info'],j_data['status'])
	db.session.add(cl)
	db.session.commit()
	set_thesis_count(j_data['t_id'])
	return r({},0,'添加成功')

#删除课程
@thesis.route('/thesislist/<int:t_id>',methods=['DELETE'])
def delete_thesis(t_id):
	tc = db.session.query(Thesis).filter_by(t_id=t_id).first()
	sql2=db.session.query(Thesis).filter_by(t_id=t_id).delete()
	db.session.commit()
	# set_thesis_count(tc.t_id);
	return r({},0,'删除成功')

#修改
@thesis.route('/thesislist/<int:t_id>',methods=['PUT'])
def edit_thesis(t_id):
	data = request.get_data()
	j_data =  json.loads(data)

	j_data.setdefault('info','')
	j_data.setdefault('sid','')
	j_data.setdefault('status','0')

	tc = db.session.query(Thesis).filter_by(t_id=t_id).first()
	# old_class_id=0
	# flag=False
	# if tc.class_id != j_data['class_id']:
	# 	old_class_id=tc.class_id
	# 	flag=True
	# 	pass
	tc.sid=j_data['sid'],
	tc.tid=j_data['tid'],
	tc.topic=j_data['topic'],
	tc.info=j_data['info'],
	tc.status=j_data['status'],
	db.session.commit()
	# if flag:
	# 	set_class_count(j_data['class_id']);
	# 	if old_class_id >0:
	# 		set_class_count(old_class_id);
	return r({},0,'修改成功')

#修改课程数（暂时不清楚作用）
def set_thesis_count(t_id):
	if int(t_id)>0:
		count=db.session.query(Thesis).filter_by(t_id=t_id).count()
		tc = db.session.query(Thesis).filter_by(t_id=t_id).first()
		# 课程数
		tc.thesis_count=count
		db.session.commit()
	return True

@thesis.route('/thesislist/minlist',methods=['GET'])
def get_minlist():
	data = db.session.query(distinct(Thesis.college).label('college')).all()
	# data=db.session.query(thesis.t_id,thesis.college).order_by(thesis.college.desc()).all()
	re=[]
	for x in data:
		re.append({'label':x[0],'value':x[0]})
		# re.append({'label':x[0]})
	return r({'thesisopt':re})