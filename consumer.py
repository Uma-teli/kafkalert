
import os
import json
import requests
import tornado.web
import tornado.autoreload
import sys
import asyncio
#import psycopg2
from kafka import KafkaConsumer
#from kafka import  KafkaProducer
#import ksql

from kafka import TopicPartition,OffsetAndMetadata
from json import loads
import re









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
        # Define server with port
        bootstrap_servers = ['169.38.75.202:9092']

        # Define topic name where the message will publish

        topic = 'TCS001_TRANSACTION'

        # Publish text in defined topic
        consumer = KafkaConsumer (group_id='test-consumer-group',bootstrap_servers =bootstrap_servers,auto_offset_reset='latest',enable_auto_commit = False)
        #consumer=KafkaConsumer(group_id='test-consumer-group',bootstrap_servers =bootstrap_servers, enable_auto_commit = False,auto_offset_reset = 'latest',value_deserializer=lambda x:  json.loads(x.decode('utf-8')))
        ##consumer.subscription()
        #sub=consumer.subscription()
        #print(sub)
        #consumer.get()
        print("starting the server")
        acct=int(self.get_body_argument("account"))
       
        tp= TopicPartition(topic,0)
        consumer.assign([tp])

        consumer.seek_to_end(tp)
        lastOffset = consumer.position(tp)

        consumer.seek_to_beginning(tp)     


        account=str(self.get_body_argument("account"))
        print(account)
        value={}
        j=0
        
        for msg in consumer:
                
                #print("Consumer records:\n")
                #print(msg)
                #json_message = json.loads(msg.value)
                #print(json_message)

                #print(msg.value.decode('UTF-8'))
                #value.append((msg.value))
                i=msg.value.decode('UTF-8').replace("'",' ')
                value[j]=json.dumps(i)
                j+=1

                #value.append(json.dumps(i))
                
                

                #print (msg.offset)
                #print(msg.value.Account_Number.decode('UTF-8'))
                #if msg.value[1] == account:
                    #print(msg.value)
                if msg.offset == lastOffset - 1:
                      break
        for m in value:
            k=(value[m].split(','))
            #print(k)
            l=(k[1].split(':'))
            u=(l[1].strip())
            print(u)
            #print(json.dumps(u))
            
            if u == account:
                print("success")
                print(k)
                g=(k[0].split(','))
                b=(g[0].split(':'))
                b1=(b[1].strip())          
                #b2=json.dumps(b1)
                print(b1)
               
                h=(k[1].split(','))
                h1=(h[0].split(':'))
                h2=(h1[1].strip())
                print(json.dumps(h2))
                
                f=(k[2].split(','))
                f1=(f[0].split(':'))
                f2=(f1[1].strip())
                print(json.dumps(f2))
                
                a=(k[3].split(','))
                a1=(a[0].split(':'))
                a2=(a1[1].strip())
                print(json.dumps(a2))

                z=(k[9].split(','))
                z1=(z[0].split(':'))
                z2=(z1[1].strip())
                print(json.dumps(z2))
            
            else:
               print("not success")

        
        self.render("static/result.html",accountno=h2,balance=z2,bloc="AccountList")
            #print(u)
        
       

    
class AccountTransaction(tornado.web.RequestHandler):
    def post(self):
        bootstrap_servers = ['169.38.75.202:9092']

        # Define topic name where the message will publish

        topic = 'TCS001_TRANSACTION'

        # Publish text in defined topic
        consumer = KafkaConsumer (group_id='test-consumer-group',bootstrap_servers =bootstrap_servers,auto_offset_reset='latest',enable_auto_commit = False)
        #consumer=KafkaConsumer(group_id='test-consumer-group',bootstrap_servers =bootstrap_servers, enable_auto_commit = False,auto_offset_reset = 'latest',value_deserializer=lambda x:  json.loads(x.decode('utf-8')))
        ##consumer.subscription()
        #sub=consumer.subscription()
        #print(sub)
        #consumer.get()
        print("starting the server")
        #acct=int(self.get_body_argument("account"))
       
        tp= TopicPartition(topic,0)
        consumer.assign([tp])

        consumer.seek_to_end(tp)
        lastOffset = consumer.position(tp)

        consumer.seek_to_beginning(tp)     


        acct=str(self.get_body_argument("acct"))
        print(acct)
        value={}
        j=0
        
        for msg in consumer:
            i=msg.value.decode('UTF-8').replace("'",' ')
            value[j]=json.dumps(i)
            j+=1
            if msg.offset == lastOffset - 1:
                      break
        for m in value:
            k=(value[m].split(','))
            #print(k)
            l=(k[1].split(':'))
            u=(l[1].strip())
            print(u)
            #print(json.dumps(u))
            if u == acct:
                print("success")
                print(k)
                g=(k[0].split(','))
                b=(g[0].split(':'))
                b1=(b[1].strip())          
                #b2=json.dumps(b1)
                print(b1)
               
                h=(k[1].split(','))
                h1=(h[0].split(':'))
                h2=(h1[1].strip())
                print(json.dumps(h2))
                
                f=(k[5].split(','))
                f1=(f[0].split(':'))
                f2=(f1[1].strip())
                print(json.dumps(f2))
                
                a=(k[8].split(','))
                a1=(a[0].split(':'))
                a2=(a1[1].strip())
                print(json.dumps(a2))
               

                z=(k[9].split(','))
                z1=(z[0].split(':'))
                z2=(z1[1].strip())
                print(json.dumps(z2))
            
            else:
               print("not success")

        
        self.render("static/AccountTransaction.html",Accountno=h2,balance=z2,ID=b1,amt=a2,tid=f2,bloc="AccountTransaction")
            
       

    


        

       

   

        
       
        
       
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
