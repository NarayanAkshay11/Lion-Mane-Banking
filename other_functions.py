#Other functions
import pickle
import tkinter as tk
def getloaninfo(a):
    l = []
    lt = []
    f = open('loan.dat','rb')
    data = pickle.load(f)
    print(data)
    for i in data:
        print(i)
        try:
            if(i[0]==str(a)):
                lt = (i[0],i[1],i[2],i[3],i[4],i[5])
                l = l + [lt]
        except:
            pass
    return l
