from unicodedata import name
import pymysql
from flask import url_for,request,redirect,session,Blueprint,jsonify
from flask_cors import CORS
import json
from pymysql import NULL
backEnd = Blueprint('blueprint', __name__)
CORS(backEnd)

db=pymysql.connect(
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='123456', 
    db='website', 
    charset='utf8'
    )
cursor=db.cursor()

# @backEnd.before_first_request
# def before_first_request():
#     # configure the connection pool in the global object
#     g.cnx_pool = mysql.connector.pooling.MySQLConnectionPool(
#         pool_name="name",pool_size=10,autocommit=True,
#         user='root',
#         password='123456',
#         host='locolhost',
#         database=db)
        
@backEnd.route("/signup", methods=["POST"])
def signup():
    newname=request.form["name"]
    newusername=request.form["username"]
    newpassword=request.form["password"]
    if (newname=="")|(newusername=="")|(newpassword==""):
        return redirect("/error?message=請填寫完整")
    sql='''SELECT `username` FROM `member` WHERE `username`=%s'''
    cursor.execute(sql,(newusername))
    result=cursor.fetchone()
    if(result !=None):
        return redirect("/error?message=帳號已經被註冊")
    sql='''INSERT INTO `member`(name,username,password) VALUE(%s,%s,%s)'''
    try:
        cursor.execute(sql,(newname,newusername,newpassword))
        db.commit()
    except:
        db.rollback()
        print('error')
    db.close
    return redirect(url_for("success",name=newname))

@backEnd.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    sql='''SELECT `name` FROM `member` WHERE `username`=%s AND `password`=%s'''
    cursor.execute(sql,(username,password))
    result=cursor.fetchone()
    if(username=="")|(password==""):
        return redirect("/error?message=請輸入帳號、密碼")
    elif(result!=None):
        session["username"]=username
        session["name"]=result[0]
        session.permanent=True
        return redirect("/member/")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@backEnd.route("/signout", methods=["GET"])
def signout():
    session["username"]=None
    return redirect("/")

@backEnd.route("/api/members", methods=["GET"])
def api():
    username=request.args.get("username")
    sql='''SELECT `id`,`name`,`username` FROM `member` WHERE `username`=%s'''
    cursor.execute(sql,(username))
    result=cursor.fetchone()
    if(result!=None):
        memberData={
            "data":{
            "id":result[0],
            "name":result[1],
            "username":result[2]
            }
        }
        return jsonify(memberData)
    else:
        Data={
            "data":None
            }
        return jsonify(Data)

@backEnd.route("/api/member", methods=["POST"])
def changeName():
    if session["username"]==None:
        return jsonify({"error":True})
    else:
        name=request.get_json()
        newname=name["name"]
        sql='''UPDATE `member` SET `name`=%s WHERE `username`=%s'''
        try:
            cursor.execute(sql,(newname,session["username"]))
            db.commit()
        except:
            db.rollback()
            print('error')
        db.close
        return jsonify({"ok":True})

    
