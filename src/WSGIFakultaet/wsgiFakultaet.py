from wsgiref.simple_server import make_server
from cgi import FieldStorage
from fibbo import fibboRecursive, fibboBinet
import re


html_template = '''<html>
<head>
  <title>Beispiel Formular-Verarbeitung</title>
</head>
<body>
  <form method="post">
    <h3>Bitte eine Zahl eingeben:</h3>
    <p>
      <input type="text" name="eingabe" value="%s" />
    </p>
    <p>
      <input type="radio" name="auswahl" value="Rekursiv" checked="checked" >Rekursiv<br>
      <input type="radio" name="auswahl" value="Binet">Binet<br>
    <p/>
    <p>
      <input type="submit" name="enter" value="Ausrechnen" />
    </p>
    <h3>Ergebnis:</h3>
    <p>%s</p>
  </form>
</body
</html>
'''


def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])

    form = FieldStorage(fp=environ['wsgi.input'], environ=environ)

    input = form.getvalue('eingabe')
    auswahl = form.getvalue('auswahl')
    
    
    if input:
        filter= re.match('[0-9]+', input)
        
        if filter:
            eingabe = int(filter.group())
        else:
            eingabe= 0
            
        
        if auswahl == 'Rekursiv':
            try:
                ausgabe = fibboRecursive(eingabe)
            except:
                ausgabe = 0
                eingabe = 'Zahl zu gross'
        else:
            try:
                ausgabe = fibboBinet(eingabe)
            except:
                ausgabe = 0
                eingabe = 'Zahl zu gross'
         
    else:
        eingabe = ausgabe = ''

    return [html_template % (eingabe, ausgabe)]


#server = make_server('', 8080, demo_app)
server = make_server('', 8080, application)
print 'Server started.'
server.serve_forever()
print 'Server stopped.'