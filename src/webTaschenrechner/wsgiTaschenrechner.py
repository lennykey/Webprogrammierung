'''
Created on 26.04.2010

@author: Andres 
'''

from wsgiref.simple_server import make_server
from cgi import FieldStorage
#from fibbo import fibboRecursive, fibboBinet

html_formular = '''
<html>
<head>
    <title>Online Rechner</title>
</head>
<body>
<h1>Ihr Onlinerechner</h1>
<form method="post">
<input type="text" name="zahl1" value="%s"/>

%s

<input type="text" name="zahl2" value="%s"/>
=
<input type="text" name="ergebnis" value="%s"/>
<div><input type="submit" name="rechnung" value="Berechnen" /></div>
</form>
</body>
</html>
'''


   
    
def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])

    form = FieldStorage(fp=environ['wsgi.input'], environ=environ)
   
    zahl1 = form.getvalue('zahl1', '0')
    #if zahl1 == 'None':
    #    zahl1 = '0'
    #else:
    #    zahl1 = str(form.getvalue('zahl1'))
        #print 'Zahl1 : ' +  type(zahl1)
        
    operator = form.getvalue('operator', '+') 
    zahl2 = str(form.getvalue('zahl2', '0'))
    
    #if zahl2 == 'None':
    #    zahl2 = "0"
    #else:
    #    zahl2 = str(form.getvalue('zahl2'))
    
    expression = zahl1+operator+zahl2
    #print expression
    #expression = '5+1'
    
    if operator == '/' and (zahl2 == '0' or zahl2 == '0.0'):
        ergebnis = 'Operation nicht gueltig'
    else:
        ergebnis = float(eval(expression))
        print ergebnis
        
    
    
    if operator == '+': 
        selectBox= '''
        <select name="operator" size="1">
          <option selected>+</option>
          <option>-</option>
          <option>*</option>
          <option>/</option>
          </select>
        '''
    elif operator == '-':
        selectBox= '''
        <select name="operator" size="1">
          <option>+</option>
          <option selected>-</option>
          <option>*</option>
          <option>/</option>
          </select>
        '''
    elif operator == '*':
        selectBox= '''
        <select name="operator" size="1">
          <option>+</option>
          <option>-</option>
          <option selected>*</option>
          <option>/</option>
          </select>
        '''
    elif operator == '/':
        selectBox= '''
        <select name="operator" size="1">
          <option>+</option>
          <option>-</option>
          <option>*</option>
          <option selected>/</option>
          </select>
        ''' 
    
    return html_formular % (zahl1, selectBox, zahl2, ergebnis)


#server = make_server('', 8080, demo_app)
server = make_server('', 8080, application)
print 'Server started.'
server.serve_forever()
print 'Server stopped.'