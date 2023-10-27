#Predominantly used to store the account details
import uuid
import pickle
import menu_func
from datetime import datetime

def updatetran(sender,cash,receiver):
    f = open('transactionlog.dat','rb')
    logdat = pickle.load(f)
    newtrandat = [str(sender),str(receiver),cash,datetime.now()]
    logdat.append(newtrandat)
    print("Logdat")
    print(logdat)
    f.close()
    ff = open('transactionlog.dat','wb')
    pickle.dump(logdat,ff)
    ff.close()
    return "RamHappy"
    print("Transactions Updated")
    




    
def create(a,b,c,d,e):
    f = open('accounts.dat','rb')
    des = pickle.load(f)
    acc_id = uuid.uuid4()
    des = des + [[acc_id,c,a,b,d,e]]
    print(des)
    ff = open('accounts.dat','wb')
    pickle.dump(des,ff)
    ff.close()
    f.close()

def retrieve(a,b):
    f = open('accounts.dat','rb')
    data = pickle.load(f)
    for i in data:
        if(i[2]==a and i[3]==b):
            return (i[0],i[1],i[4])
    else:
        return False
    f.close()
    
def retrieve2(a):
    f = open('accounts.dat','rb')
    data = pickle.load(f)
    for i in data:
        if(str(i[0])==a):
            return i[1]
    else:
        return None
def chanstat(a,b,cash,recid):
    f = open('accounts.dat','rb')
    chandat = pickle.load(f)
    ans = ''
    print(chandat)
    for i in chandat:
        if(str(i[0])==str(a)):
            print('a')
            if(i[3]==b):
                print('b')
                print(menu_func.getbal(a))
                if(int(cash)<= int(menu_func.getbal(a))):
                    menu_func.updatebal(a,cash,recid)
                    ans = "chanhappy"
                    updatetran(a,cash,recid)
                else:
                    ans = "chansad1"
            else:
                ans = "chansad2"
    print(ans)
    print("!!!Ans")
    return ans

def arnykndm(a):
    f = open('accounts.dat','rb')
    finddat = pickle.load(f)
    for i in finddat:
        
        if(i[2]==a or i[4]==a):
            return (i[1],str(i[0]))
    else:
        return False
