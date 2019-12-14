# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:55:05 2019

@author: andre
"""
import os
import time

def main():
    
    ownPid = os.getpid() #adquire o pid
    pidf= open("pid.txt","w+") #abre o arquivo de texto
    pidf.write(str(ownPid))
    pidf.close()
    xSec = 5
    for i in range(3):
        print("2: I am alive")
        time.sleep(xSec)
    print("2: I am gonna die now, bye")
if __name__ == '__main__':
    main()
        
    
    
    
    
    
    
    
    
