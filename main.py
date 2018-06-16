'''
Priyam Banerjee
University of Texas at Arlington
CSE 6331 Assignment # 2 Running SQL on IBM Bluemix and Clustering the Earthquake data 
Citations : 
 IBM Documentation, github, stackoverflow.com
'''
import os
from flask import Flask, render_template, redirect, request
from collections import defaultdict
import os
import urllib
import datetime
import json
import ibm_db
import logging

if 'VCAP_SERVICES' in os.environ:
    db2info = json.loads(os.environ['VCAP_SERVICES'])['dashDB For Transactions'][0]
    db2cred = db2info["credentials"]
    appenv = json.loads(os.environ['VCAP_APPLICATION'])
else:
    raise ValueError('Expected cloud environment')

port = int(os.getenv("VCAP_APP_PORT"))
app=Flask(__name__)

'''
@app.route('/')
def mainpage():
    return render_template("main.html")
@app.route('/firstpage/',methods=['post','get'])
'''
@app.route('/')
def firstpage():
    db2conn = ibm_db.connect(
        "DATABASE=" + db2cred['db'] + ";HOSTNAME=" + db2cred['hostname'] + ";PORT=" + str(db2cred['port']) + ";UID=" +
        db2cred['username'] + ";PWD=" + db2cred['password'] + ";", "", "")
    dictionary = defaultdict(lambda: None)
    dict = defaultdict(lambda: None)
    numRows = 0
    number = []
    locsource = []
    
    if db2conn:
        # we have a Db2 connection, query the database
        print('Connection Established')
        sql = "select count(*) as NUMBER,locationsource from earthquake group by locationsource" #For mag between 4,5 and a particular date
        #rowcountsql = ""
        # stmt = ibm_db.prepare(db2conn, sql) only for UPDATE INSERT
        try:
            '''
            res = ibm_db.exec_immediate(db2conn, rowcountsql)
            dict = ibm_db.fetch_assoc(res)
            numRows = int(dict['1'])
            '''
            result = ibm_db.exec_immediate(db2conn, sql)
            dictionary = ibm_db.fetch_assoc(result)
            number.append(dictionary["NUMBER"])
            locsource.append(dictionary["LOCATIONSOURCE"])
            while dictionary != False:
                print dictionary["LOCATIONSOURCE"]
                dictionary = ibm_db.fetch_assoc(result)
                number.append(dictionary["NUMBER"])
                locsource.append(dictionary["LOCATIONSOURCE"])
        except:
            print(' Found Val')
    return render_template("main.html",number=number,locsource=locsource)

    #return render_template("main.html",time=time,latitude=latitude,longitude=longitude,depth=depth,mag=mag,magType=magType,nst=nst,gap=gap,dmin=dmin,rms=rms,net=net,id=id,updated=updated,place=place,type=type,hzerror=hzerror,dperror=dperror,magerror=magerror,magnst=magnst,status=status,locsource=locsource,magsource=magsource)


if __name__=='__main__':
    app.run(host='0.0.0.0' , port=port)