from flask import Flask,url_for,request,render_template,redirect,session
app=Flask(__name__,)
app.secret_key='123'

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form['a']
    password=request.form['p']
    session["state"]=account
    session.permanent=True
    if(account=="")|(password==""):
        return redirect(url_for("error",message="請輸入帳號、密碼"))
    else:
        if (account=='test') & (password=='test'):
            return redirect("/member/")
        if(account!="test")|(password!="test"):
            return redirect(url_for("error",message="帳號、或密碼輸入錯誤"))

@app.route("/member/")
def member():
    if session['state']==None:
        return redirect("/")
    else:
        return render_template('member.html')

@app.route("/error/")
def error():
    message=request.args.get("message","")
    return (message)

@app.route("/signout", methods=["GET"])
def signout():
    session["state"]=None
    return redirect("/")

app.run(port=3000, debug=True)
