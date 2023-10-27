import tkinter as tk
import menu_func
import account_info
import other_functions
import pickle

from datetime import datetime




def paylah():
    global rec1,rec2
    global idd
    global naam
    global newc, rec1,rec2
    
    amt = rec1.get()
    pswd = rec2.get()
    newc.destroy()
    newc = tk.Tk()
    cash = tk.Label(newc,text="Lion Mane NetBanking", foreground="blue", font=("Times",35))
    cash.pack(pady=10)
    img2 = tk.PhotoImage(file="C:\\Users\\naray\\OneDrive\\Desktop\\abc.png").subsample(2,2)    
    a = account_info.chanstat(idd,pswd,amt,naam[1])
    print(a)
    if(a=="chanhappy"):
        tk.Label(newc,text="Transaction Successful",foreground="green",font=("Times",20,"bold")).pack(pady=10)
    elif(str(a[-1])=='1'):
        l = tk.Label(newc,text="Insufficient Funds",foreground="red",font=("Times",20,"bold"))
        l.pack(pady=10)
    elif(str(a[-1])=='2'):
        l = tk.Label(newc,text="Incorrect Password",foreground="red",font=("Times",20,"bold"))
        l.pack(pady=10)
    

def search():
    global rec
    global naam
    global twin, newc,rec1, rec2
    
    emph = rec.get()
    newc = tk.Tk()
    naam = account_info.arnykndm(emph)
    twin.destroy()
    if(naam!=False):
        cash = tk.Label(newc,text="Lion Mane NetBanking", foreground="blue", font=("Times",35))
        cash.pack(pady=10)
        cash1 = tk.Label(newc,text="Enter Transaction Details", foreground="purple", font=("Times",25))
        cash1.pack(pady=10)
        ll1 = tk.Label(newc,text="Amount")
        ll1.pack(pady=5)
        rec1 = tk.Entry(newc)
        rec1.pack(pady=10)
        ll2 = tk.Label(newc,text="Password")
        ll2.pack(pady=5)
        rec2 = tk.Entry(newc,show="*")
        rec2.pack(pady=10)
        recsub = tk.Button(newc,text="Proceed",command = paylah)
        recsub.pack(pady=10)
    else:
        cash = tk.Label(newc,text="Lion Mane NetBanking", foreground="blue", font=("Times",35))
        cash.pack(pady=10)
        ll1 = tk.Label(newc,text="User Not Found",foreground="red",font=("Times",20))
        ll1.pack(pady=5)


    
def srfrs():
    global idd
    global rec
    global cash
    global twin
    twin = tk.Tk()
    cash = tk.Label(twin,text="Lion Mane NetBanking", foreground="blue", font=("Times",35))
    cash.pack(pady=10)
    cash1 = tk.Label(twin,text="Let's find the person", foreground="purple", font=("Times",25))
    cash1.pack(pady=10)
    ll1 = tk.Label(twin,text="Enter the Email address/Phone Number of receiver")
    ll1.pack(pady=5)
    rec = tk.Entry(twin)
    rec.pack(pady=10)
    recsub = tk.Button(twin,text="Search User",command = search)
    recsub.pack(pady=10)



def trant():
    global idd
    global loanwin
    print("Viewing Transactions")
    atmm=[]
    namedic = {}
    f = open('transactionlog.dat','rb')
    logg = pickle.load(f)
    atmwin = tk.Tk()
    Titless = tk.Label(atmwin,text="Lion Mane NetBanking", foreground="blue", font=("Times",35))
    Titless.pack(pady=10)
    ll = []
    atmbel = tk.Label(atmwin,text="Your Transaction Hstory",foreground="purple",font=('Times',20))
    for i in logg:
        print(i)
        if(str(i[0])==str(idd)):
            ll = ll + [i]
            print('a')
            
        elif(str(i[1])==str(idd)):
            ll =ll + [i]
            print('b')
    
    for i in ll:
        print(i)
        namedic[i[0]]= account_info.retrieve2(i[0])
        namedic[i[1]]= account_info.retrieve2(i[1])
    
    atmtitle1 = tk.Label(atmwin,text="Sender",font=("Times",15,"bold"))
    atmtitle1.place(x = 50, y = 70)
    atmtitle2 = tk.Label(atmwin,text="Receiver",font=("Times",15,"bold"))
    atmtitle2.place(x = 250, y = 70)
    atmtitle3 = tk.Label(atmwin,text="Amount",font=("Times",15,"bold"))
    atmtitle3.place(x = 450, y = 70)
    atmtitle4 = tk.Label(atmwin,text="Date",font=("Times",15,"bold"))
    atmtitle4.place(x = 650, y = 70)
    n = 0
    m = 0
    for i in ll:
        for j in range(4):
        
            if(j==0 or j==1):
                tr11 = tk.Label(atmwin,text=str(namedic[i[j]]),font=("Times",10,"bold"))
                tr11.place(x= (n + 50),y=(m+100))
                n = n + 200
            else:
                tr11 = tk.Label(atmwin,text=str(i[j]),font=("Times",10,"bold"))
                tr11.place(x= (n + 50),y=(m+100))
                n = n + 200
        m = m + 20
        n = 0
    
        
def loans():
    global newin
    global idd
    global loanwin
    
    details = other_functions.getloaninfo(idd)
    print("Details")
    print(details)
    loanwin = tk.Tk()
    Titled = tk.Label(loanwin,text='Lion Mane NetBanking', foreground="blue", font=("Times",35))
    Titled.pack(pady=10)
    loanbel = tk.Label(loanwin,text="On Going Loans",font=('Times',20))
    loanbel.pack(pady=10)
    for i in details:
        print(i)
        lab = tk.Label(loanwin,text="Loan " + str(details.index(i)+1)+":", foreground="brown",font=("Times",15,'bold'))
        lab.pack(pady=15)
        det = tk.Label(loanwin,text="Loan Category: " + str(i[1]),font=('Times',10))
        det.pack(pady=1)
        det2 = tk.Label(loanwin,text = "Interest: " +str(i[2]),font=('Times',10))
        det2.pack(pady=1)
        det3 = tk.Label(loanwin,text= "Loan Term: " +str(i[3]),font=('Times',10))
        det3.pack(pady=1)
        det4 = tk.Label(loanwin,text="Principal: " +str(i[4]),font=('Times',10))
        det4.pack(pady=1)
        det5 = tk.Label(loanwin,text= "Monthly Payment: " +str(i[5]),font=('Times',10))
        det5.pack(pady=1)
        
    
def getval(t):
    global idd
    global nam
    global phon
    idd = t[0]
    nam = t[1]
    phon = t[2]
    print(t)
    print(idd,nam,phon)

def ggetbal():
    global idd
    global a
    global men
    global newin
    a = str(menu_func.getbal(idd))
    newin = tk.Tk()
    
    Title = tk.Label(newin,text='Lion Mane NetBanking', foreground="blue", font=("Times",35))
    Title.pack(pady=10)
    balabel = tk.Label(newin,text="Account Balance",font=('Times',20))
    balabel.pack(pady=10)
    bala = tk.Label(newin,text=a,font=('Times',20))
    bala.pack(pady=5)
    newin.mainloop()
    
    

def logout():
    global men
    men.destroy()


    
def account_page():
    global men
    
    men = tk.Tk()
    men.geometry('650x550')
    img = tk.PhotoImage(file="C:\\Users\\naray\\lionmane.png").subsample(6,6)
    tk.Button(men,image=img,command=logout).place(x=15,y=15)

    Title = tk.Label(men,text='Lion Mane NetBanking', foreground="blue", font=("Times",35))
    Title.place(x=115,y=30)

    bt = tk.Button(men,text="Account Balance",font=('Times',15),command = ggetbal)
    bt.place(x = 255,y = 100)
    bt2 = tk.Button(men,text='Ongoing Loans',font=('Times',15),command=loans)
    bt2.place(x = 265,y = 200)
    bt3 = tk.Button(men,text='Start Transaction',font=('Times',15),command=srfrs)
    bt3.place(x = 245,y = 300)
    bt4 = tk.Button(men,text='View Transactions',font=('Times',15),command=trant)
    bt4.place(x = 245,y = 400)
    l = tk.Label(men,text='')
    l.place(x = 265,y = 450)
      
    men.mainloop()
