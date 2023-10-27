import tkinter as tk
import account_info
import useraccess



def check():
    global em1,p1ww,logwin
    emaill = em1.get()
    pswd = p1ww.get()
    if(account_info.retrieve(emaill,pswd)==False):
        err = tk.Label(logwin,text="The password or email id is incorrect", foreground="red",font=('Times',15))
        err.pack(pady = 20)
    else:
        print(account_info.retrieve(emaill,pswd))
        useraccess.getval(account_info.retrieve(emaill,pswd))
        logwin.destroy()
        useraccess.account_page()



    
def show():
    global e1,pw1,e2,i,win,sphe,phe
    em = e1.get()
    pwo = pw1.get()
    nam = e2.get()
    phone= phe.get()
    sphone = sphe.get()
    win.destroy()
    account_info.create(em,pwo,nam,phone,sphone)
    useraccess.getval(account_info.retrieve(em,pwo))
    useraccess.account_page()
    

def login():
    global em1,p1ww, logwin,window
    logwin = tk.Tk()
    titl = tk.Label(logwin,text="Kindly Log into your account",foreground = "purple",font=("Times",25))
    titl.pack(pady=20)
    email = tk.Label(logwin,text="Please enter your email id")
    email.pack(pady=10)
    em1 = tk.Entry(logwin)
    em1.pack(pady=20)
    pw1w = tk.Label(logwin,text="Enter the Password")
    pw1w.pack(pady=10)
    p1ww = tk.Entry(logwin,show="*")
    p1ww.pack(pady = 10)
    sub = tk.Button(logwin,text="Submit", command=check)
    sub.pack()
    pkk = tk.Label(logwin,text="")
    pkk.pack(pady=10)
    window.destroy()
    
def register():
    global e1
    global pw2
    global pw1,e2,i,win,sph,sphe,ph,phe,window
    win = tk.Tk()
    win_name = tk.Label(win,text='Register into your account',foreground="purple",font=("Times",25))
    win_name.pack(pady=20)
    name = tk.Label(win,text="Kindly enter your full name below")
    name.pack(pady = 5)
    e2 = tk.Entry(win)
    e2.pack(pady = 10)
    email = tk.Label(win,text="Enter your email id")
    email.pack(pady = 10)
    e1 = tk.Entry(win)
    e1.pack(pady=10)
    pw = tk.Label(win, text = "Enter a secure password")
    pw.pack(pady = 20)
    pw1 = tk.Entry(win)
    pw1.pack(pady = 10)
    ph = tk.Label(win,text="Please enter your primary Phone Number")
    ph.pack(pady=20)
    phe = tk.Entry(win)
    phe.pack(pady=10)
    sph = tk.Label(win,text="Please enter your secondary Phone Number")
    sph.pack(pady=20)
    sphe = tk.Entry(win)
    sphe.pack(pady=10)
    but = tk.Button(win,text="Submit",bg="white",fg="blue", command = show)
    but.pack()
    window.destroy()
    




window = tk.Tk()
img = tk.PhotoImage(file="C:\\Users\\naray\\lionmane.png").subsample(3,3)
tk.Button(window, image=img).pack()
labb = tk.Label(image = img)
title = tk.Label(text='Lion Mane NetBanking', foreground="blue", font=("Times",30))
click = tk.Button(text="Register",fg="black", command = register)
log = tk.Button(text="Login",fg="black", command = login)
title.pack(pady=20)
click.pack(pady = 10)
log.pack()
pk = tk.Label(window,text='')
pk.pack(pady=10)
window.mainloop()
