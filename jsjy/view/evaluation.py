from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db,Evaluation
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
	search['id']=request.values.get('id')
	search['sid']=request.values.get('sid')
	search['tid']=request.values.get('tid')
	search['c_id']=request.values.get('c_id')
	search['score1']=request.values.get('score1')
	search['score2']=request.values.get('score2')
	search['score3']=request.values.get('score3')
	search['score4']=request.values.get('score4')
	search['score5']=request.values.get('score5')
	search['commit']=request.values.get('commit')
	orderBy=request.values.get('orderBy')
	orderDir=request.values.get('orderDir')

	count=db.session.query(Evaluation).count()
	db_tc=db.session.query(Evaluation)
	offset=((page-1)*perPage)
	rt={}
	ids=[]
	temp=[]
	order=Evaluation.id.desc()
	if orderBy and orderDir:#排序
		temp1=getattr(Evaluation,orderBy)
		order=getattr(temp1,orderDir)()
	db_tc.order_by(order)
	where=[Evaluation.id>0]
	for k,v in search.items():
		if v:
			temp1=getattr(Evaluation,k).like("%"+v+"%")
			where.append(temp1)
	
	tc = db_tc.order_by(order).filter(*where).limit(perPage).offset(offset) 
	for t in tc:
		temp.append({
		'id':t.id,
		'sid':t.sid,
		'tid':t.tid,
		'c_id':t.c_id,
		'score1':t.score1,
		'score2':t.score2,
		'score3':t.score3,
		'score4':t.score4,
		'score5':t.score5,
		'commit':t.commit
		})
	rt['count']=count
	rt['rows']=temp
	# rt['hasNext']=1
	return r(rt)
	pass

# 添加
@evaluation.route('/evaluation',methods=['POST'])
def add_evaluation():
	data = request.get_data()
	j_data =  json.loads(data)
	user=db.session.query(Evaluation).filter_by(id=j_data['id']).first()
	# if user is not None:
	# 	return r({},0,'',{'id':'已经存在'})

	j_data.setdefault('commit','')
	cl = Evaluation(j_data['sid'],j_data['tid'],j_data['c_id'],j_data['score1'],j_data['score2'],j_data['score3'],j_data['score4'],j_data['score5'],j_data['commit'])
	db.session.add(cl)
	db.session.commit()
	# set_evaluation_count(j_data['id'])
	return r({},0,'添加成功')

#删除
@evaluation.route('/evaluationlist/<int:id>',methods=['DELETE'])
def delete_evaluation(id):
	tc = db.session.query(Evaluation).filter_by(id=id).first()
	sql2=db.session.query(Evaluation).filter_by(id=id).delete()
	db.session.commit()
	# set_evaluation_count(tc.c_id);
	return r({},0,'删除成功')

#修改
@evaluation.route('/evaluationlist/<int:id>',methods=['PUT'])
def edit_evaluation(id):
	data = request.get_data()
	j_data =  json.loads(data)
	
	tc = db.session.query(Evaluation).filter_by(id=id).first()
	# old_class_id=0
	# flag=False
	# if tc.class_id != j_data['class_id']:
	# 	old_class_id=tc.class_id
	# 	flag=True
	# 	pass
	tc.sid=j_data['sid'],
	tc.tid=j_data['tid'],
	tc.c_id=j_data['c_id'],
	tc.score1=j_data['score1'],
	tc.score2=j_data['score2'],
	tc.score3=j_data['score3'],
	tc.score4=j_data['score4'],
	tc.score5=j_data['score5'],
	tc.commit=j_data['commit'],
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
	data = db.session.query(distinct(Evaluation.c_id).label('c_id')).all()
	# data=db.session.query(evaluation.c_id,evaluation.college).order_by(evaluation.college.desc()).all()
	re=[]
	for x in data:
		re.append({'label':x[0],'value':x[0]})
		# re.append({'label':x[0]})
	return r({'evaluationopt':re})