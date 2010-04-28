'''
Created on 27.04.2010

@author: jupiter
'''

from fiboGenerator import fibogen

def ausgabe():
    for i, fibo in enumerate(fibogen()):
        if i > 6:
            break
        print fibo
    
if __name__ == "__main__": 
    
    ausgabe()
        