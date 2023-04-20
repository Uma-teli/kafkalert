import os
import json
import requests
import tornado.web
import tornado.autoreload
import sys
import asyncio
#import psycopg2
import pyodbc



#import matplotlib.pyplot as plt

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))
#port=8000
class landingPage(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")
        
class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")

class Login(tornado.web.RequestHandler):
    def post(self):
        #base_url = 'https://api.eu-gb.apiconnect.appdomain.cloud/m1ganeshtcscom1543928228162-dev/sb/payments/custReg?acctId='
        # 100000001001 is the only working answer
        #headers = {'Content-Type': 'application/json'}
        print("inside login")
        username = str(self.get_body_argument("uname"))
        print(username)
        pwd = str(self.get_body_argument("pass"))
        print(pwd)
        #end_url= base_url+str(self.get_body_argument("accnt"))
        #req = requests.get(end_url, headers=headers, auth=('701e3938-c7c7-4568-9e3b-d474bfb39700', ''), verify=False)
        #json_out = req.json()
        print("json")
        if username =="admin" and pwd == "adminpass":
            print("success")
            self.render("static/indexx.html")
        else:
            print("no")
            self.render("static/trial.html")
        #print(json_out)
        #self.render("static/genericresp.html",msg=json_out['CSRGRES']['CSRGRES']['MESSAGES'],cname=json_out['CSRGRES']['CSRGRES']['CUSTOMER_NAME'],cid=json_out['CSRGRES']['CSRGRES']['CUSTOMER_ID'],date=json_out['CSRGRES']['CSRGRES']['SYS_DATE'],time=json_out['CSRGRES']['CSRGRES']['SYS_TIME'],bloc="regreq")



class basicRevHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/reversal.html")

#class predictScore(tornado.web.RequestHandler):
    #def post(self):
        #base_url = 'https://192.86.32.113:19443/api_fraud_detection/fraudDetection?merchantxname='
        #base_url = 'https://gateway.aipc1.cp4i-b2e73aa4eddf9dc566faa4f42ccdd306-0001.us-east.containers.appdomain.cloud/sachinsorg/sandbox/payments/pymntRev?acctId='
        #base_url = 'https://api.eu-gb.apiconnect.appdomain.cloud/m1ganeshtcscom1543928228162-dev/sb/payments/pymntRev?acctId='
        # 100000001001 is the only working answer
        #headers = {'Content-Type': 'application/json'}
        #end_url= base_url+str(self.get_body_argument("accnt"))+"&transId="+str(self.get_body_argument("trans"))+"&revAmt="+str(self.get_body_argument("debit_amt"))
        #end_url= base_url+str(self.get_body_argument("mername"))+"&user1="+str(self.get_body_argument("usr"))+"&amount="+str(self.get_body_argument("amt"))+"&merchantxstate="+str(self.get_body_argument("merstate"))+"&usexchip="+str(self.get_body_argument("chip"))+"&errorsx="+str(self.get_body_argument("err"))+"&mcc="+str(self.get_body_argument("mcc"))+"&merchantxcity="+str(self.get_body_argument("mercity"))+"&card="+str(self.get_body_argument("card"))
        #req = requests.get(end_url, headers=headers, auth=('ibmuser', 'ibmuser'), verify=False)
        #json_out = req.json()
        #print("before")
        #print(json_out)
        #jsonstruct=json_out
        #print(jsonstruct)
        #jsonstruct=json.dumps(jsonstruct)
        #json_load=json.loads(jsonstruct)
        #print(json_load["MODELOUT"]["MODELOUP"]["PROBABILITYX1X"])
        #print("df")

        #val1=json_load['MODELOUT']['MODELOUP']['PROBABILITYX1X']
        #val2=json_load['MODELOUT']['MODELOUP']['PROBABILITYX0X']
        #print(val1)
        #val1=round(val1,16)
        #val2=round(val2,16)
        #print (val1)
        #val1=round((val1*100),2)
        #val2=round((val2*100),2)
        #print(val1)
        #val1=round(val1,2)
        #print(val1)
        #percent1=val1
        #percent2=int(json_load['MODELOUT']['MODELOUP']['PROBABILITYX0X'])*100
        #print(val1,val2)
        #labels= ['Risk for transfer', 'Non-risk for transfer']
        #colors=['#14213d','#e63946']
        #sizes= [val1,val2]
        #plt.pie(sizes,labels=labels, colors=colors, startangle=90, autopct='%1.1f%%')
        #plt.axis('equal')
        #plt.show()

        #self.render("static/result.html",label=labels,color=colors,size=sizes,x1x=json_load['MODELOUT']['MODELOUP']['PROBABILITYX1X'],xox=json_load['MODELOUT']['MODELOUP']['PROBABILITYX0X'],bloc="predictScore", jsonstruct=jsonstruct)
        
class AccountList(tornado.web.RequestHandler):
    def post(self):

        conn=pyodbc.connect(
            Trusted_Connection ='YES',
            Driver='{SQL Server}',
            Server="DESKTOP-QT2Q335\SQLEXPRESS",
            Database="AccountList"

        )

        sql_select_Query = "SELECT * FROM ACCOUNTLIST"
        cursor=conn.cursor()
        cursor.execute(sql_select_Query)
        #for row in cursor:
           # print(row)

        #data=pd.real_sql("SELECT * FROM ACCOUNTLIST",conn)
        records= cursor.fetchall()

        cursor.close()
        conn.close()

        #for row in records:
            #print("s1= ", row[0],)
            #print("s2= ", row[1])
            #print("s3= ", row[2])
            #print("s4= ", row[3], "\n")

        self.render("static/result.html",xox=records[0] ,x0x=records[1],x2x=records[2],x3x=records[4],x4x=records[5],bloc="AccountList")


class AccountTransaction(tornado.web.RequestHandler):
    def post(self):
        account=str(self.get_body_argument('account'))
         
        #connection to the databse 
        conn=pyodbc.connect(
            Trusted_Connection ='YES',
            Driver='{SQL Server}',
            Server="DESKTOP-QT2Q335\SQLEXPRESS",
            Database="AccountList"

        )
        sql_select_Query = "SELECT * FROM AccountTransaction WHERE ACCOUNT_NO=%s"%account
        cursor=conn.cursor()
        cursor.execute(sql_select_Query)

        records= cursor.fetchall()

        cursor.close()
        conn.close()

        self.render("static/AccountTransaction.html",Accountno=records[0][0] ,currentbal=records[0][1] ,credit=records[0][2], transid=records[0][3],transamt=records[0][4],description=records[0][5],bloc="AccountTransaction")

class AccountDetails(tornado.web.RequestHandler):
    def post(self):
        account=str(self.get_body_argument('account'))
        conn=pyodbc.connect(
            Trusted_Connection ='YES',
            Driver='{SQL Server}',
            Server="DESKTOP-QT2Q335\SQLEXPRESS",
            Database="AccountList"

        )
        sql_select_Query = "SELECT * FROM AccountDetails WHERE ACCOUNT_NO=%s"%account
        cursor=conn.cursor()
        cursor.execute(sql_select_Query)
        records= cursor.fetchall()

        cursor.close()
        conn.close()

        self.render("static/AccountDetails.html",accountno=records[0][0], balance=records[0][1] ,ID=records[0][2],bloc="AccountDetails") 



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", landingPage),
        (r"/AccountList", AccountList),
        (r"/AccountDetails",AccountDetails),
        (r"/AccountTransaction",AccountTransaction)

    ])
    print("commit")
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app.listen(port)
    # TODO remove in prod
    #print("inside win")
    #server=HTTPServer(app)
    tornado.autoreload.start()
    print("I'm listening on port specified")
    print(port)
    tornado.ioloop.IOLoop.current().start()
