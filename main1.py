
'''
Priyam Banerjee
CSE 6331 Assignment # 2
Citations : 
github, stackoverflow.com, IBM Documentation
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
    dictionary1 = defaultdict(lambda: None)
    dict1 = defaultdict(lambda: None)
    dictionary2 = defaultdict(lambda: None)
    dict2 = defaultdict(lambda: None)
    dictionary3 = defaultdict(lambda: None)
    dict3 = defaultdict(lambda: None)
    numRows1 = 0
    numRows2 = 0
    numRows3 = 0
    numRows4 = 0
    numRows5 = 0
    numRows6 = 0
    numRows7 = 0
    numRows8 = 0
    numRows9 = 0
    numRows10 = 0
    time1 = []
    latitude1 = []
    longitude1 = []
    depth1 = []
    mag1 = []
    magtype1 = []
    time2 = []
    latitude2 = []
    longitude2 = []
    depth2 = []
    mag2 = []
    magtype2 = []
    time3 = []
    latitude3 = []
    longitude3 = []
    depth3 = []
    mag3 = []
    magtype3 = []
    '''
    nst = []
    gap = []
    dmin = []
    rms = []
    id = []
    place = []
    dperror = []
    magerror = []
    magnst = []
    locsource = []
    '''
    
    if db2conn:
        # we have a Db2 connection, query the database
        print('Connection Established')
        sql1 = "SELECT * FROM EARTHQUAKE WHERE  MAG BETWEEN 3 AND 5" #For mag between 4,5 and a particular date
        rowcountsql1 = "SELECT COUNT(*) FROM EARTHQUAKE WHERE MAG BETWEEN 3 AND 5"
        # stmt = ibm_db.prepare(db2conn, sql) only for UPDATE INSERT
        try:
            res1 = ibm_db.exec_immediate(db2conn, rowcountsql1)
            dict1 = ibm_db.fetch_assoc(res1)
            numRows1 = int(dict1['1'])
            result1 = ibm_db.exec_immediate(db2conn, sql1)
            dictionary1 = ibm_db.fetch_assoc(result1)
            time1.append(dictionary1["TIME"])
            latitude1.append(dictionary1["LATITUDE"])
            longitude1.append(dictionary1["LONGITUDE"])          
            while dictionary1 != False:
                #print dictionary["TIME"],dictionary["LATITUDE"],dictionary["LONGITUDE"]
                dictionary1 = ibm_db.fetch_assoc(result1)
                time1.append(dictionary1["TIME"])
                latitude1.append(dictionary1["LATITUDE"])
                longitude1.append(dictionary1["LONGITUDE"])
                
               
        except:
            print(' Found Val')
    return render_template("firstpage.html",numRows1=numRows1,time1=time1,latitude1=latitude1,longitude1=longitude1)
 
    #return render_template("main.html",time=time,latitude=latitude,longitude=longitude,depth=depth,mag=mag,magType=magType,nst=nst,gap=gap,dmin=dmin,rms=rms,net=net,id=id,updated=updated,place=place,type=type,hzerror=hzerror,dperror=dperror,magerror=magerror,magnst=magnst,status=status,locsource=locsource,magsource=magsource)


if __name__=='__main__':
    app.run(host='0.0.0.0' , port=port)