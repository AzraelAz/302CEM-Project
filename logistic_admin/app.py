from flask import Flask, render_template, url_for, redirect, request, session, flash
import pymysql
import datetime
import json

conn = pymysql.connect(host='localhost',user='root',password='',db='logistic_db')

myCursor = conn.cursor()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':

        userid = request.form['userid']
        pwd = request.form['pwd']
        
        myCursor.execute("SELECT `adminID` FROM `loginlist` WHERE `adminID` = %s" % userid)
        id1 = myCursor.fetchone()
        ID1 = ' '.join(id1)

        myCursor.execute("SELECT `adminPWD` FROM `loginlist` WHERE `adminID` = %s" % userid)
        pw1 = myCursor.fetchone()
        PW1 = ' '.join(pw1)

        if ID1 == userid and PW1 == pwd:
            return redirect(url_for('orders'))
        else:
            error = 'Invalid UserId / Password'
            return render_template('login.html', error=error)
    



@app.route('/log', methods=["GET","POST"])
def log():
    if request.method =="POST":

        find_order_number = request.form.get("find_order_number")

        myCursor.execute("SELECT `orderNo` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        t1 = myCursor.fetchone()
        tr1 = str(t1)
        y = len(tr1) - 2
        try1 = tr1[1:y]

        myCursor.execute("SELECT `S_FirstName` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr2 = myCursor.fetchone()
        try2 = ' '.join(tr2)

        myCursor.execute("SELECT `S_LastName` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr3 = myCursor.fetchone()
        try3 = ' '.join(tr3)

        myCursor.execute("SELECT `S_Address` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr4 = myCursor.fetchone()
        try4 = ' '.join(tr4)

        myCursor.execute("SELECT `S_City` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr5 = myCursor.fetchone()
        try5 = ' '.join(tr5)

        myCursor.execute("SELECT `S_Country` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr6 = myCursor.fetchone()
        try6 = ' '.join(tr6)

        myCursor.execute("SELECT `R_FirstName` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr7 = myCursor.fetchone()
        try7 = ' '.join(tr7)

        myCursor.execute("SELECT `R_LastName` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr8 = myCursor.fetchone()
        try8 = ' '.join(tr8)

        myCursor.execute("SELECT `R_Address` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr9 = myCursor.fetchone()
        try9 = ' '.join(tr9)

        myCursor.execute("SELECT `R_City` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr10 = myCursor.fetchone()
        try10 = ' '.join(tr10)

        myCursor.execute("SELECT `R_Country` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr11 = myCursor.fetchone()
        try11 = ' '.join(tr11)

        myCursor.execute("SELECT `ProductName` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr12 = myCursor.fetchone()
        try12 = ' '.join(tr12)

        myCursor.execute("SELECT `OrderQun` FROM `orderlist` WHERE `orderNo` = %s" % find_order_number)
        tr13 = myCursor.fetchone()
        try13 = ' '.join(tr13)

        return render_template("ordermake.html",orderNo=try1,S_FirstName=try2,S_LastName=try3,S_Address=try4,S_City=try5,S_Country=try6,R_FirstName=try7,R_LastName=try8,R_Address=try9,R_City=try10,R_Country=try11,ProductName=try12,OrderQun=try13)

    return render_template("ordermake.html")



@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        a = request.form['P_orderNo']
        b = request.form['N_S_firstName']
        c = request.form['N_S_lastName']
        d = request.form['N_S_address']
        e = request.form['N_S_city']
        f = request.form['N_S_country']
        g = request.form['N_R_firstName']
        h = request.form['N_R_lastName']
        i = request.form['N_R_address']
        j = request.form['N_R_city']
        k = request.form['N_R_country']
        l = request.form['N_productname']
        m = request.form['N_orderqun']

        sql = ("UPDATE orderlist SET S_FirstName=%s,S_LastName=%s,S_Address=%s,S_City=%s,S_Country=%s,R_FirstName=%s,R_LastName=%s,R_Address=%s,R_City=%s,R_Country=%s,ProductName=%s,OrderQun=%s WHERE orderNo = %s")
        myCursor.execute(sql, (b,c,d,e,f,g,h,i,j,k,l,m,a))
        myCursor.execute('commit')

    return redirect(url_for('log'))



@app.route("/orders", methods=["GET","POST"])
def orders():
    if request.method =="POST":

        order_number = request.form.get("order_number")

        myCursor.execute("SELECT `orderNo` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        da1 = myCursor.fetchone()
        dat1 = str(da1)
        x = len(dat1) - 2
        data1 = dat1[1:x]

        myCursor.execute("SELECT `S_FirstName` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt2 = myCursor.fetchone()
        data2 = ' '.join(dt2)

        myCursor.execute("SELECT `S_LastName` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt3 = myCursor.fetchone()
        data3 = ' '.join(dt3)

        myCursor.execute("SELECT `S_Address` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt4 = myCursor.fetchone()
        data4 = ' '.join(dt4)

        myCursor.execute("SELECT `S_City` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt5 = myCursor.fetchone()
        data5 = ' '.join(dt5)

        myCursor.execute("SELECT `S_Country` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt6 = myCursor.fetchone()
        data6 = ' '.join(dt6)

        myCursor.execute("SELECT `R_FirstName` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt7 = myCursor.fetchone()
        data7 = ' '.join(dt7)

        myCursor.execute("SELECT `R_LastName` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt8 = myCursor.fetchone()
        data8 = ' '.join(dt8)

        myCursor.execute("SELECT `R_Address` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt9 = myCursor.fetchone()
        data9 = ' '.join(dt9)

        myCursor.execute("SELECT `R_City` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt10 = myCursor.fetchone()
        data10 = ' '.join(dt10)

        myCursor.execute("SELECT `R_Country` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt11 = myCursor.fetchone()
        data11 = ' '.join(dt11)

        myCursor.execute("SELECT `ProductName` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt12 = myCursor.fetchone()
        data12 = ' '.join(dt12)

        myCursor.execute("SELECT `OrderQun` FROM `orderlist` WHERE `orderNo` = %s" % order_number)
        dt13 = myCursor.fetchone()
        data13 = ' '.join(dt13)
    
        return render_template("orders.html",data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9,data10=data10,data11=data11,data12=data12,data13=data13)

    return render_template("orders.html")
		

if __name__ == "__main__":
    app.run(debug=True)