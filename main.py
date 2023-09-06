#coding=utf-8
import flask
from flask import  Flask,request,render_template,session,redirect
from flask_cors import CORS
import json,socket,re,time,datetime,threading,os
import pymysql
from student import student
from gevent import pywsgi

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'jiemaweb'

CORS(app, resources=r'/*')

msghtml = '<!DOCTYPE html><head><meta charset="utf-8"><title>%s</title></head><script>window.onload = function () {alert("%s");window.history.back()}</script></html>'

def dbquery(query,arg=()):
    db.ping(reconnect=True)
    cu = db.cursor()
    try:
        cu.execute(query,arg)
        ret = cu.fetchall()
    except:
        ret = None
    db.commit()
    cu.close()
    return ret

@app.route('/bind',methods=['POST'])
def bind():
    qid = request.form.get("qid")
    sid = request.form.get("sid")
    realname = request.form.get("realname")
    realid = request.form.get("realid")

    if qid == '' or sid == '' or realname == '' or realid == '':
        return msghtml%("失败","请填写所有字段")

    sql = "select count(*) from bindlist where qid = %s"
    ret = dbquery(sql,(qid))
    if ret[0][0] > 0:
        return msghtml%("失败","此QQ已绑定，如需换绑请联系管理员")

    sql = "select * from students where student_id = %s"
    ret = dbquery(sql,(sid))

    if ret.__len__() < 1:
        return msghtml%("失败","信息有误，请检查后再试，如有疑问请联系管理员")

    stu = student()
    stu.fromret(ret)

    if realname != stu.name or realid !=str(stu.id_card_number)[-6:]:
        return msghtml%("失败","信息有误，请检查后再试，如有疑问请联系管理员")
    
    sql = "select count(*) from bindlist where sid = %s"
    ret = dbquery(sql,(sid))
    if ret[0][0] > 0:
        return msghtml%("失败","此学号已被其他QQ绑定，如有疑问请联系管理员")
    
    ipaddr = request.headers.get("X-Forwarded-For")
    sql = "INSERT INTO bindlist (qid,sid,bindtime,ipaddr) VALUES (%s,%s,%s,%s)"
    dbquery(sql,(qid,stu.student_id,datetime.datetime.now(),ipaddr))

    return msghtml%("绑定成功","绑定成功，感谢你的配合")


#web controller
@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    db = pymysql.connect(host='10.233.0.164',user='root',passwd='Wztdaisuki233',database='realname-auth')
    server = pywsgi.WSGIServer(('0.0.0.0', 7891), app)
    server.serve_forever()



