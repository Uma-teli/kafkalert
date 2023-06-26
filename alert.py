from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from kafka import KafkaConsumer
from kafka import TopicPartition
import json








app = Flask(__name__)

app.secret_key = 'abcdefg'

@app.route('/',methods=['GET','POST'])
def defaultHome():
    bootstrap_servers = ['169.38.75.202:9092']
    topic= 'TCS001_ACCOUNT'
    consumer = KafkaConsumer (bootstrap_servers =bootstrap_servers,auto_offset_reset='earliest',enable_auto_commit = False)
            
    tp= TopicPartition(topic,0)
    consumer.assign([tp])

    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)
           

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
                 t+1
                    
                 break
    for r in value1:
                a1=(value1[r].split(','))
                print(a1)
                a2=(a1[1].split(':'))
                a3=(a2[1].strip())
                print(a3)
    b1=a3            
    last_key=list(value)[-1]
    value.pop(last_key)
    value2=[]
    value3=[]
    for r in value1:
              d1=(value1[r].split(','))
              d2=(d1[3].split(':'))
              d3=(d2[1].strip())
               
              value3.append(d3)
    b2=d3
    print(value3)

    for x in value3:

        print(type(x))
        Y=str(10000.00)
        if float(x) >= float(Y):
        
            print("yes")
            balance= True
            a4=a3[-4:]
            a5="X"
            a6=str(a5)+str(a4)
            print(a6)
            return render_template("index.html",bal=balance,acct=a6,bloc="Alert")
        else:
            print("no")
                
    for m in value:
                k=(value[m].split(','))
            #print(k)
                l=(k[1].split(':'))
                u=(l[1].strip())
                value2.append(u)
    print(value2)

    
             
    if a3 in value2:
            print("same")
            return render_template("index.html")
    
          
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

    
                
            return render_template("index.html",t=t,bid=p4,number=account,balance=f2,bloc="Alert")
    
    
    
    
                    



    # return render_template('index.html')

@app.route('/AccountList',methods=['POST'])
def AccountList():
        if request.method=='POST':
          account=request.form['account']
       
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


        #account=str(self.get_body_argument("account"))
        #print(account)
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
            print(k)
            l=(k[1].split(':'))
            u=(l[1].strip())
            print(u)
            #print(json.dumps(u))
            
            if int(u) == int(account):
                print("success")
                print(k)
                g=(k[0].split(','))
                b=(g[0].split(':'))
                b1=(b[1].strip())          
                #b2=json.dumps(b1)
                print(b1)
               
                h=(k[1].split(','))
                h1=(h[0].split(':'))
                acct=(h1[1].strip())
                print(acct)
                
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

        
        return render_template("result.html",accountno=acct,balance=z2,bloc="AccountList")
            

@app.route('/AccountTransaction',methods=['POST'])
def AccountTransaction():
        if request.method=='POST':
          acct=request.form['acct']
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
            if int(u) == int(acct):
                print("success")
                print(k)
                g=(k[0].split(','))
                b=(g[0].split(':'))
                b1=(b[1].strip())          
                #b2=json.dumps(b1)
                print(json.dumps(b1))
               
                h=(k[1].split(','))
                h1=(h[0].split(':'))
                h2=(h1[1].strip())
                print(json.dumps(h2))
                
                f=(k[7].split(','))
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

        
        return render_template("AccountTransaction.html",Accountno=h2,balance=z2,ID=b1,amt=a2,tid=f2,bloc="AccountTransaction")
            

    
   

        

       

        

    
        
        

                    


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')