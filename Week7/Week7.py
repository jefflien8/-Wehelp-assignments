from flask import Flask,request,render_template,redirect,session,Blueprint
from blueprint import backEnd

frontEnd=Flask(__name__,)
frontEnd.register_blueprint(backEnd)
frontEnd.secret_key="123"

@frontEnd.route("/")
def home():
    return render_template("home.html")

@frontEnd.route("/success/")
def success():
    # 重新導向至首頁
    return render_template("success.html",name=request.args.get("name")),{"Refresh": "3; url='/'"}

@frontEnd.route("/member/")
def member():
    if session["name"]==None:
        return redirect("/")
    else:
        return render_template("member.html",name=session["name"])

@frontEnd.route("/error/")
def error():
    message=request.args.get("message")
    return render_template("error.html", message=message)

frontEnd.run(host="0.0.0.0",port=3000,debug=True)