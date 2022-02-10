import pymysql
from flask import Flask,url_for,request,render_template,redirect,session
app=Flask(__name__,)
app.secret_key="123"
db=pymysql.connect(
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='123456', 
    db='website', 
    charset='utf8'
    )
cursor=db.cursor()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["POST"])
def signup():
    newname=request.form["name"]
    newusername=request.form["username"]
    newpassword=request.form["password"]
    if (newname=="")|(newusername=="")|(newpassword==""):
        return redirect(url_for("error",message="請填寫完整！"))
    sql='''SELECT `username` FROM `member` WHERE `username`=%s'''
    cursor.execute(sql,(newusername))
    result=cursor.fetchone()
    if(result !=None):
        return redirect(url_for("error",message="帳號已經被註冊"))
    sql='''INSERT INTO `member`(name,username,password) VALUE(%s,%s,%s)'''
    try:
        cursor.execute(sql,(newname,newusername,newpassword))
        db.commit()
    except:
        db.rollback()
        print('error')
    db.close
    return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]
    sql='''SELECT `name` FROM `member` WHERE `username`=%s AND `password`=%s'''
    cursor.execute(sql,(username,password))
    result=cursor.fetchone()
    if(username=="")|(password==""):
        return redirect(url_for("error",message="請輸入帳號、密碼"))
    elif(result!=None):
        session["name"]=result[0]
        session.permanent=True
        return redirect("/member/")
    else:
        return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))

@app.route("/member/")
def member():
    if session["name"]==None:
        return redirect("/")
    else:
        return render_template("member.html",name=session["name"])

@app.route("/error/")
def error():
    return render_template("error.html", message=request.args.get("message"))

@app.route("/signout", methods=["GET"])
def signout():
    session["name"]=None
    return redirect("/")

app.run(port=3000, debug=True)