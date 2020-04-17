from flask import *
import pymysql
import datetime
import json

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('orderlist.html')

if __name__ == "__main__":
    app.run()