from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db, Course,Class
from jsjy.public import r
from sqlalchemy import distinct

thesis=Blueprint('thesis',__name__)

@thesis.route('/thesis')
def index():
	return render_template('/thesis.html')