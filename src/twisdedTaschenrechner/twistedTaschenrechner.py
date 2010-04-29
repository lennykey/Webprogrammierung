"""
Twisted Taschenrechner 
"""
from twisted.web import http
import os
import time
import re

class RequestHandler(http.Request):
    
    
    html_taschenrechner = '''
    <html>
    <head><title>Twisted Taschenrechner</title></head>
    <body>
    <h1>Ihr Twisted Taschenrechner</h1>
    <form style="border-style: solid; border-color: grey; width:850px;
     padding:5px" method="post">
    <input type="text" name="zahl1" value="%s"/>
    <select name="operator" size="1">
       %s
    </select>
    <input type="text" name="zahl2" value="%s"/>
    = 
    <span style="color:red; font-weight: bold">%s</span>
    <br/>
    <br/>
    <input type="submit" name="enter" value="Ausrechnen"/>
    </form>
    </body>
    </html>
    '''
    
    
    def process(self):
        
        liste = self.args
        
        zahl1 = ''
        try:
            zahl1 = re.match('[0-9.]+', ''.join(liste.get('zahl1',
                                                          '0')[0:])).group()
        except AttributeError:
            zahl1= 'Bitte Zahl eingeben'
        
        operator = ''.join(liste.get('operator', '+')[0:])

        zahl2 = ''
        try:
            zahl2 = re.match('[0-9.]+', ''.join(liste.get('zahl2',
                                                          '0')[0:])).group()
        except AttributeError:
            zahl2 = 'Bitte Zahl eingeben'
        
        
        toEvaluate= []
        toEvaluate.append(zahl1)
        toEvaluate.append(operator)
        toEvaluate.append(zahl2)
        
        
        
        toEvaluate = ''.join(toEvaluate)
        
        try:
            ergebnis = float(eval(toEvaluate))
            print ergebnis
        except ZeroDivisionError:
            ergebnis = 'Division durch 0 ist nicht definiert'
        except SyntaxError:
            ergebnis = 'Fehler' 
        
        if operator == '+':
            options= '''
            <option selected>+</option>
            <option>-</option>
            <option>*</option>
            <option>/</option>
            '''
        elif operator == '-':
            options= '''
            <option >+</option>
            <option selected>-</option>
            <option>*</option>
            <option>/</option>
            '''
        elif operator == '*':
            options= '''
            <option >+</option>
            <option>-</option>
            <option selected>*</option>
            <option>/</option>
            '''
        elif operator == '/':
            options= '''
            <option>+</option>
            <option>-</option>
            <option>*</option>
            <option selected>/</option>
            '''
            
        
        self.write(self.html_taschenrechner % (zahl1, options, zahl2, ergebnis) )
        
        self.finish()
                

class HttpServer(http.HTTPChannel):

    requestFactory = RequestHandler


class HttpFactory(http.HTTPFactory):

    protocol = HttpServer


if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.listenTCP(8000, HttpFactory())
    reactor.run()
    