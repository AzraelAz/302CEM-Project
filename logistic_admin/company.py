from flask import Flask, render_template, url_for, request, session, redirect
import pymysql
import datetime
import json


conn = pymysql.connect(host='localhost',user='root',password='',db='logisticdb')

myCursor = conn.cursor()

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("ordermake.html")



@app.route("/", methods=["GET", "POST"])
def getvalue():
    od = datetime.datetime.now()
    productN = request.form['name_goods']
    qun = request.form['qun_goods']
    addr = request.form['address']
    cit = request.form['city']
    cou = request.form['country']
    zp = request.form['zip']

    sql = 'SELECT `firstName` FROM `customerlist` WHERE `customerNO` = %s;'
    myCursor.execute(sql, qun)
    data1 = myCursor.fetchone()

    sql = 'SELECT `lastName` FROM `customerlist` WHERE `customerNO` = %s;'
    myCursor.execute(sql, addr)
    data2 = myCursor.fetchone()

    return render_template("order_complete.html", orderdate=od, data1=data1, data2=data2, productName=productN, quantity=qun, address=addr, city=cit, country=cou, zip=zp)

if __name__ == "__main__":
    app.run()