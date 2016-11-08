#show  MD5  
import os  
import hashlib  
import sys  
import re  
  
path=r".\file"
  
def GetMd5(filename):  
    m=hashlib.md5()  
    n=1024*8  
    inp=open(filename,'rb')  
    while True:  
        buf=inp.read(n)  
        if buf:  
            m.update(buf)  
        else:  
            break;  
    return (m.hexdigest())  
  
def ChangeFilename():  
    for file in os.listdir(path):  
        if os.path.isfile(os.path.join(path,file))==True:  
            new_name=GetMd5( os.path.join(path,file))  
              
            print new_name  
            if os.path.exists(os.path.join(path,new_name))==False:                  
                os.rename(os.path.join(path,file),os.path.join(path,new_name))  
            else:  
                print 'exist the file of '+file  
  
if __name__=="__main__":  
    ChangeFilename()  
    #print os.path.exists(r'd:\1.txt')  
