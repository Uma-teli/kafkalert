import os
import json
import requests
import tornado.web
import tornado.autoreload
import sys
import asyncio
#import psycopg2
import hazelcast
import logging







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

        #self.render("static/result.html",label=labels,color=colors,size=sizes,x1x=json_load['MODELOU
        # T']['MODELOUP']['PROBABILITYX1X'],xox=json_load['MODELOUT']['MODELOUP']['PROBABILITYX0X'],bloc="predictScore", jsonstruct=jsonstruct)
        
class AccountList(tornado.web.RequestHandler):
    def post(self):

        #conn=pyodbc.connect(
            #Trusted_Connection ='YES',
            #Driver='{SQL Server}',
            #Server="DESKTOP-QT2Q335\SQLEXPRESS",
            #Database="AccountList"

        #)

        #sql_select_Query = "SELECT * FROM ACCOUNTLIST"
        #cursor=conn.cursor()
        #cursor.execute(sql_select_Query)
        
        
        #json_out= cursor.fetchall()

        #cursor.close()

        #conn.close()

        
        #headers = {'Content-Type': 'application/json'}
        #base_url='http://192.86.32.113:16099/zdih/rest/api/v1/accounts?limit=30'
        #req = requests.get(base_url, headers=headers, auth=('ibmuser', 'tcs2041'), verify=False)
        #json_out = req.json()
        #print("json")
        #print(json_out)
        
        #self.render("static/result.html",len = len(json_out), json_out = json_out,bloc="AccountList") 
        #self.render("static/result.html",xox=records[0],x0x=records[1],x2x=records[2],x3x=records[4],x4x=records[5],bloc="AccountList")
        headers = {'Content-Type': 'application/json'}
        logging.basicConfig(level=logging.INFO)
        client = hazelcast.HazelcastClient(
                cluster_name="zdih-tcs",
                cluster_members=[
                            "192.86.32.113:6701",
                ])
        #client= hazelcast.HazelcastClient()
        #account=str(self.get_body_argument('account'))
        account=int(self.get_argument("account"))
        print(account)
        #result=client.sql.execute(f"SELECT * FROM TCS001_ACCOUNT WHERE Account_Number= {account} ").result()
        result1=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {account} ").result()
        

        for row in result1:
                print(row.get_object("Account_Number"))
                print(row.get_object("Available_Balance"))
                Account_no=row["Account_Number"]
                balance=row["Available_Balance"]
                self.render("static/result.html",accountno=Account_no,balance=balance,headers=headers,bloc="AccountList")
       
        #else:       
            #outVal = 'Account number does not exists'
            #self.render("static/AccountNotExists.html",outVal = outVal ,bloc="AccountList")
        #self.render("static/result.html",accountno=row[0],accountno1=row[1],accountno2=r
       
        #json_out=json.dumps(result)

        #print(json_out)s
          
        #sself.render("static/result.html",accountno=Account_no,balance=balance,outval=outval,headers=headers,bloc="AccountList")
        #self.render("static/result.html",accountno=row[0],accountno1=row[1],accountno2=row[2],accountno3=row[3],accountno4=row[4],accountno5=row[5],headers=headers,bloc="AccountList") 
        
        

        #my_map = client.get_map("TCS001_ACCOUNT").blocking()
        #json_out = my_map.get('Account_number')
        #print(json_out)

        #print(my_map.get("Account_number"))

        #for Account_number in my_map.entry_set().result():

            #print(Account_number)


        
       
        client.shutdown()
        #self.render("static/result.html",len = len(json_out), json_out = json_out,bloc="AccountList") 
        
        #self.render("static/result.html", accountno = json_out,headers=headers,bloc="AccountList") 
       

        #sql_select_Query = "SELECT * FROM ACCOUNTLIST"
        #cursor=client.cursor()
        #cursor.execute(sql_select_Query)
        
        
        #json_out= cursor.fetchall()

        #cursor.close()
        
        #headers = {'Content-Type': 'application/json'}
        #req = requests.get(AccountList, headers=headers, verify=False)
        #json_out = req.json()
        #print("json")
        #print(json_out)
        #self.render("static/result.html",len = len(json_out), json_out = json_out,bloc="AccountList") 
        



class AccountTransaction(tornado.web.RequestHandler):
    def post(self):
        logging.basicConfig(level=logging.INFO)
        client = hazelcast.HazelcastClient(
            cluster_name="zdih-tcs",
            cluster_members=[

                "192.86.32.113:6701",
                ])
        
        act=int(self.get_argument("act"))
        print(act)
        damt=int(self.get_argument("damt"))
        print(damt)

        #result=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {act} ").result()
        
        #if result:
            ##print(row.get_object("Account_Number"))
                #print(row.get_object("Available_Balance"))
                #Account_no=row["Account_Number"]
                #balance=row["Available_Balance"]
                #self.render("static/AccountTransaction.html",Accountno=Account_no,balance=balance,bloc="AccountTransaction")
       

       
       

       
        result1=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {act}").result()
        for row in result1:
            print(row.get_object("Available_Balance"))
            print(row.get_object("Account_Number"))
            Account_no=row["Account_Number"]
            balance=row["Available_Balance"]


        balance1=balance+damt
        client.sql.execute(f"UPDATE TCS001_TRANSACTION SET Available_Balance= {balance1} WHERE Account_Number={act}").result()
        result3=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {act}").result()
        for row in result3:
            print(row.get_object("Available_Balance"))
            b=row["Available_Balance"]
            

        self.render("static/AccountTransaction.html",Accountno=Account_no,balance=b,bloc="AccountTransaction")
       
        #balance2=balance-camt
        #client.sql.execute(f"UPDATE TCS001_TRANSACTION SET Available_Balance= {balance2} WHERE Account_Number={act}").result()
        #result4=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {act}").result()
        #for row in result4:
            #print(row.get_object("Available_Balance"))
            #b=row["Available_Balance"]
            



        #self.render("static/AccountTransaction.html",Accountno=Account_no,balance=balance,bloc="AccountTransaction")
            #b=row["Available_Balance"]



            
        #self.render("static/AccountTransaction.html",)
        #result=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {act} AND CREDITORDEBIT:'c").result() 
        
        #for row in result:
            #print(row.get_object("Account_Number"))
            #print(row.get_object("Available_Balance"))
            #Account_no=row["Account_Number"]
            #balance=row["Available_Balance"]
            #self.render("static/AccountTransaction.html",Accountno=Account_no,balance=balance,bloc="AccountTransaction")
       
       
        

        #base_url='http://192.86.32.113:16099/zdih/rest/api/v1/accounts?/transactions?pagingLimit=5&pagingoffset=1'
        #account=str(self.get_body_argument('account'))
        #headers = {'Content-Type': 'application/json'}
        #end_url= base_url+str(self.get_body_argument("account"))
        #req = requests.get(end_url, headers=headers, auth=('ibmuser', 'tcs2041'), verify=False)
        #json_out = req.json()
        #print("json")
        #print(json_out)
        #self.render("static/AccountTransaction.html",Accountno=json_out[0][0] ,currentbal=json_out[0][1] ,credit=json_out[0][2], transid=json_out[0][3],transamt=json_out[0][4],description=json_out[0][5],bloc="AccountTransaction")


        #connection to the databse 
        #conn=pyodbc.connect(
           # Trusted_Connection ='YES',
           # Driver='{SQL Server}',
           # Server="DESKTOP-QT2Q335\SQLEXPRESS",
           # Database="AccountList"

        #)
        #sql_select_Query = "SELECT * FROM AccountTransaction WHERE ACCOUNT_NO=%s"%account
        #cursor=conn.cursor()
        #cursor.execute(sql_select_Query)

       # records= cursor.fetchall()

        #cursor.close()
        #conn.close()

        #self.render("static/AccountTransaction.html",Accountno=records[0][0] ,currentbal=records[0][1] ,credit=records[0][2], transid=records[0][3],transamt=records[0][4],description=records[0][5],bloc="AccountTransaction")

class AccountDetails(tornado.web.RequestHandler):
    def post(self):
        logging.basicConfig(level=logging.INFO)
        client = hazelcast.HazelcastClient(
            cluster_name="zdih-tcs",
            cluster_members=[

                "192.86.32.113:6701",
                ])
        
        acct=int(self.get_argument("acct"))
        print(acct)
        camt=int(self.get_argument("camt"))
        print(camt)
       
        result1=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {acct}").result()
        for row in result1:
            print(row.get_object("Available_Balance"))
            print(row.get_object("Account_Number"))
            Account_no=row["Account_Number"]
            balance=row["Available_Balance"]



        balance2=balance-camt
        client.sql.execute(f"UPDATE TCS001_TRANSACTION SET Available_Balance= {balance2} WHERE Account_Number={acct}").result()
        result4=client.sql.execute(f"SELECT * FROM TCS001_TRANSACTION WHERE Account_Number= {acct}").result()
        for row in result4:
            print(row.get_object("Available_Balance"))
            b=row["Available_Balance"]

        self.render("static/AccountDetails.html",accountno=Account_no,balance=b,bloc="AccountDetails")
       
            

        #base_url='http//192.867.32.113:16099/zdih/rest/api/v1/accounts='
        #account=str(self.get_body_argument('account'))
        #headers = {'Content-Type': 'application/json'}
        #end_url= base_url+str(self.get_body_argument("account"))
        #req = requests.get(end_url, headers=headers, auth=('ibmuser', 'tcs2041'), verify=False)
        #json_out = req.json()
       # print("json")
        #print(json_out)
        #self.render("static/AccountDetails.html",accountno= json_out[0][0], balance=json_out[0][1] ,ID= json_out[0][2],bloc="AccountDetails") 


        ###cursor=conn.cursor()
        ##records= cursor.fetchall()

        #cursor.close()
        #conn.close()

        #self.render("static/AccountDetails.html",accountno=records[0][0], balance=records[0][1] ,ID=records[0][2],bloc="AccountDetails") 



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
