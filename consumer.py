
import os
import json
import requests
import tornado.web
import tornado.autoreload
import sys
import asyncio
#import psycopg2
from kafka import KafkaConsumer
from kafka import TopicPartition
import tornado.httpclient
import tornado.websocket
import tornado.ioloop













#import matplotlib.pyplot as plt

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))
#port=8000
class Page(tornado.web.RequestHandler):
    def get(self):
            self.render("static/index.html")  
        
            
        
      
        
class Alert(tornado.web.RequestHandler):
    def post(self):
        bootstrap_servers = ['169.38.75.202:9092']
        topic= 'TCS001_ACCOUNT'
        consumer = KafkaConsumer( bootstrap_servers =bootstrap_servers,auto_offset_reset='earliest',enable_auto_commit = False)
            
        tp= TopicPartition(topic,0)
        consumer.assign([tp])

        consumer.seek_to_end(tp)
        lastOffset = consumer.position(tp)
            #for row in consumer:
                #(row.value)

        consumer.seek_to_beginning(tp)    
        value1={}
        t=0

        value={}
        j=0
            
        for msg in consumer:
            i=msg.value.decode('UTF-8').replace("'",' ')
            value[j]=json.dumps(i)
            j+=1
              
            if msg.offset == lastOffset - 1:
                 print(msg.value.decode('UTF-8'))
                 p1=msg.value.decode('UTF-8').replace("'",' ')
                 value1[t]=json.dumps(p1)
                 
              
                 break
        #print(value1)
        for r in value1:
                a1=(value1[r].split(','))
                print(a1)
                a2=(a1[1].split(':'))
                a3=(a2[1].strip())
                print(a3)
        #value2=list(value[:-1])
        #print(value2)
        last_key=list(value)[-1]
        value.pop(last_key)
        value2=[]
       # p=0
        print(value)
        for m in value:
                 k=(value[m].split(','))
            #print(k)
                 l=(k[1].split(':'))
                 u=(l[1].strip())
                 value2.append(u)
                # p+=1
        print(value2)
                # print(u)
                # if u == a3:
                    #print("same")
                    #self.render("static/AccountNotExists.html")

                 #else:
                    # print("not same")
                    #print(a1)
                     
                    #p2=(a1[0].split(','))
                   # p3=(p2[0].split(':'))
                   # p4=(p3[1].strip())          
                     #b2=json.dumps(b1)
                    #print(p4)
               
                    # h=(a1[1].split(','))
                    #h1=(h[0].split(':'))
                    #account=(h1[1].strip())
                    #print(account)
                
                   # f=(a1[2].split(','))
                   # f1=(f[0].split(':'))
                   # f2=(f1[1].strip())
                   # print(f2)

                   # e=(a1[3].split(','))
                   # e1=(e[0].split(':'))
                   # e2=(e1[1].strip())
                   # print(e2)
       # trigger= False
        print(a3)
        if a3 in value2:
            print("same")
            
            self.render("static/index.html")  
        else:
            print(" not same")
            t = True
            # Set this variable based on your condition
            p2=(a1[0].split(','))
            p3=(p2[0].split(':'))
            p4=(p3[1].strip())

            h=(a1[1].split(','))
            h1=(h[0].split(':'))
            account=(h1[1].strip())
            #print(account)

            f=(a1[3].split(','))
            f1=(f[0].split(':'))
            f2=(f1[1].strip())
                   # print(f2)
            self.render("static/newaccount.html",t=t,bid=p4,number=account,balance=f2,bloc="Alert")
                    

        #self.render("static/newaccount.html",account=account,bid=p4,balance=e2,bloc="Alert")

#class WebSocketHandler(tornado.websocket.WebSocketHandler):
    #def open(self):
        #self.application.websocket_clients.append(self)sss

    #def on_close(self):ss

       # self.application.websocket_clients.remove(self)s

#class TriggerAlertHandler(tornado.web.RequestHandler):
    #def get(self):
        #for client in self.application.websocket_clients:
            #client.write_message("DisplayAlert")
        #self.write("Alert trigger requested")       



#client = tornado.httpclient.HTTPClient()
#response = client.fetch("http://localhost:8888/trigger_alert")
#client.close()
#print(response.body.decode())         
                    

             

    



        


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
       
        print("json")
        if username =="admin" and pwd == "adminpass":
            print("success")
            self.render("static/indexx.html")
        else:
            print("no")
            self.render("static/trial.html")
       

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
        consumer = KafkaConsumer (bootstrap_servers =bootstrap_servers,auto_offset_reset='earliest',enable_auto_commit = False)
        
        print("starting the server")
        
       
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
            
            if u == account:
                print("success")
                print(k)
                g=(k[0].split(','))
                b=(g[0].split(':'))
                global b1
                b1=(b[1].strip())          
                #b2=json.dumps(b1)
                print(b1)
               
                h=(k[1].split(','))
                h1=(h[0].split(':'))
                global acct
                acct=(h1[1].strip())
                print(json.dumps(acct))
                
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

        
        self.render("static/result.html",accountno=acct,balance=z2,bloc="AccountList")
            #print(u)
        
       

    
class AccountTransaction(tornado.web.RequestHandler):
    def post(self):
        bootstrap_servers = ['169.38.75.202:9092']

        # Define topic name where the message will publish

        topic = 'TCS001_TRANSACTION'

        # Publish text in defined topic
        consumer = KafkaConsumer (group_id='test-consumer-group',bootstrap_servers =bootstrap_servers,auto_offset_reset='latest',enable_auto_commit = False)
       
        print("starting the server")
       
       
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
                acnt=(h1[1].strip())
                print(acnt)
                
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

        
        self.render("static/AccountTransaction.html",Accountno=acnt,balance=z2,ID=b1,amt=a2,tid=f2,bloc="AccountTransaction")
            

    
   

        

       

   

        
       
        
       



       

if __name__ == "__main__":

    #def make_app():
        # return tornado.web.Application([
        #(r"/", landingPage),
        #(r"/ws", WebSocketHandler),
        #(r"/trigger_alert", TriggerAlertHandler),
    #], websocket_clients=[])

    app = tornado.web.Application([
         
        (r"/", Page),
        (r"/AccountList", AccountList),
        (r"/AccountTransaction",AccountTransaction),
        (r"/Alert",Alert)
    
        

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
