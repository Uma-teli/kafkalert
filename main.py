import os
import json
import requests
import tornado.web
import tornado.autoreload
import sys
import asyncio
#import psycopg2
#from kafka import KafkaConsumer
from kafka import  KafkaProducer
from time import sleep
from json import dumps








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


       
        
        
class AccountList(tornado.web.RequestHandler):
    def post(self):
        #headers = {'Content-Type': 'application/json'}
        #base_url='http://169.38.75.202:8085/zdih/rest/api/v1/accounts?limit=5'
        #req = requests.get(base_url, headers=headers,  verify=False)
        #json_out = req.json()
        #print("json")
        #print(json_out)
        
        #self.render("static/result.html",len = len(json_out), json_out = json_out,headers=headers,bloc="AccountList") 
        #self.render("static/result.html",xox=json_out['accounts'][0],x0x=json_out['accounts'][1],x2x=json_out['accounts'][2],x3x=json_out['accounts'][3],x4x=json_out['accounts'][4],headers=headers,bloc="AccountList")
       

        # Define server with port
        bootstrap_servers = ['169.38.75.202:9092']

        # Define topic name where the message will publishpython main.py

        topicName = 'TCS001_ACCOUNT'

        # Initialize producer variable
        producer = KafkaProducer(bootstrap_servers = bootstrap_servers,value_serializer=lambda x: dumps(x).encode('utf-8'))
        #producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
        # Publish text in defined topic
        #producer.send(topicName, b'h')
        #for e in range(2):
        data = {'Bank_ID ': 900, 'Account_Number':678934561000,'Transaction_Count':0,'Available_Balance':2000.00}
        producer.send(topicName, value=data)
        sleep(5)

        # Print message

        print("Message Sent")

        
             


        
       

        



class AccountTransaction(tornado.web.RequestHandler):
    def post(self):
        headers = {'Content-Type': 'application/json'}
        end_url= str(self.get_body_argument("account"))
        base_url=f'http://169.38.75.202:8085/zdih/rest/api/v1/accounts/{end_url}/transactions?pagingLimit=5'
        req = requests.get(base_url, headers=headers, verify=False)
        json_out = req.json()
        print("json")
        print(json_out)
        self.render("static/AccountTransaction.html",Accountno=json_out['accountStatementRecords'][0]['accountNumber'],balance=json_out['accountStatementRecords'][0]['availableBalance'],ID=json_out['accountStatementRecords'][0]['bankId'],amt=json_out['accountStatementRecords'][0]['transAmount'],tid=json_out['accountStatementRecords'][0]['tranId'],headers=headers,bloc="AccountTransaction")


        
        
       
class AccountDetails(tornado.web.RequestHandler):
    def post(self):
        base_url='http://169.38.75.202:8085/zdih/rest/api/v1/accounts/'
        #account=str(self.get_body_argument("account"))
        headers = {'Content-Type': 'application/json'}
        acct=str(self.get_body_argument("account"))
        end_url= base_url+acct
        req = requests.get(end_url, headers=headers, verify=False)
        json_out = req.json()
        print("json")
        print(json_out)
        
        self.render("static/AccountDetails.html",accountno= json_out[acct]['accountNumber'], balance=json_out[acct]['availableBalance'],ID=json_out[acct]['bankId'],
                    headers=headers,bloc="AccountDetails") 


       

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
