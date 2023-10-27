#Getting menu information from different csv files
import pickle
import uuid
def getbal(a):
    f = open('balance.dat','rb')
    data = pickle.load(f)
    for i in data:
        if(str(i[0])==str(a)):
            return i[1]
    else:
        print('False')
        return False


def updatebal(sender,amt,receiver):
    f = open('balance.dat','rb')
    baldat = pickle.load(f)
    newdat = []
    l = []
    for i in baldat:
        
        if(str(i[0])==str(sender)):
            l = [str(i[0]),int(i[1])-int(amt)]
            
            newdat = newdat + [l]
            l = []
        elif(str(i[0])== str(receiver)):
            if(i[1]==None):
                l = [str(i[0]),int(amt)]
            else:
                l = [str(i[0]),int(i[1])+int(amt)]
            newdat = newdat + [l]
            print(l)
            l = []
        else:
            newdat = newdat + [i]
    f.close()
    ff = open('balance.dat','wb')
    pickle.dump(newdat,ff)
    print("Superman")
    print(newdat)
    ff.close()
