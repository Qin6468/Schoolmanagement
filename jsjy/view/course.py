from flask import Blueprint,render_template,Flask,request,redirect,session,json,current_app as app
import hashlib,time
from jsjy.models import db, Admin,Teacher
from jsjy.public import r

# import csv
course=Blueprint('course',__name__)