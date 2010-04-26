from wsgiref.simple_server import make_server
from cgi import FieldStorage
#from fibbo import fibboRecursive, fibboBinet
import re
import csv

csv_view_template= '''
<html>
<head>
<title>CSV Datei</title>
</head>
<body>
Die Persoenlichen Daten wurden als CSV-Datei gespeichert

<a href="">Neuen Eintrag schreiben</a>
</body>
</html>
'''


html_form_template = '''<html>
<head>
  <title>Personendaten</title>
</head>
<body>
  <form method="post" >
    <h3>Geben Sie bitte Ihre persoenliche Daten ein:</h3>
    <p>
      <div><span>Name: </span> <input type="text" name="name" value="%s" /></div>
      <div><span>Vorname: </span><input type="text" name="vorname" value="%s" /></div>
      <div><span>Geburtsort: </span><input type="text" name="gebOrt" value="%s" /></div>
      <div><span>Groesse: </span><input type="text" name="groesse" value="%s" /></div>
      <div><span>Geburtsdatum: <input type="text" name="gebDatum" value="%s" /></div>
      <div><span>Augenfarbe: </span>
      <select name="augenfarbe" size="1">
      <option>schwarz</option>
      <option>braun</option>
      <option>gruen</option>
      <option>blau</option>
      </select>
      </div>
    <p>
      <input type="submit" name="enter" value="anzeigen" />
    </p>
  </form>
</body
</html>
'''

html_view_template = '''
<html>
<head>
<title>Ihre Angaben</title>
</head>
<body>

<div><span>Vorname: </span><span>%s</span></div>
<div><span>Nachname: </span><span>%s</span></div>
<div><span>Geburtsort: </span><span>%s</span></div>
<div><span>Groesse: </span><span>%s</span></div>
<div><span>Geburtsdatum: </span><span>%s</span></div>
<div><span>Augenfarbe: </span><span>%s</span></div>


<form method="post" >
    <p>
      <input type="hidden" name="name" value="%s" />
      <input type="hidden" name="vorname"  value="%s" />
      <input type="hidden" name="gebOrt"  value="%s" />
      <input type="hidden" name="groesse" value="%s" />
      <input type="hidden" name="gebDatum" value="%s" />
      <input type="hidden" name="augenfarbe"  value="%s" />
    <p/>
    <p>
      <input type="submit" name="enter" value="csv" />
    </p>
  </form>


</body
</html>
''' 



def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])

    form = FieldStorage(fp=environ['wsgi.input'], environ=environ)

    name = form.getvalue('name')
    vorname = form.getvalue('vorname')
    
    try:
        gebDatum = re.match('[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]',
                             str(form.getvalue('gebDatum'))).group()
    except AttributeError:
        gebDatum = 'TT-MM-JJJJ'
        
    
    
    gebOrt = form.getvalue('gebOrt')
    groesse = form.getvalue('groesse')
    augenfarbe = form.getvalue('augenfarbe')
    button = form.getvalue('enter')
    
   
    
    liste= []
    liste.append(name)
    liste.append(vorname)
    liste.append(gebDatum)
    liste.append(gebOrt)
    liste.append(groesse)
    liste.append(augenfarbe)

    print liste
    
    if button == 'anzeigen':
        
        for info in liste:
            print info
            print type(info)
            if (info == 'None' or info == None or info == 'TT-MM-JJJJ'):
                html = [html_form_template % (name, vorname, gebOrt, 
                                              groesse, gebDatum)]
                break
        
            else:
                html= [html_view_template % (name, vorname, gebOrt, groesse,
                                              gebDatum, augenfarbe, name,
                                               vorname, gebOrt, groesse,
                                                gebDatum, augenfarbe)]
                
    elif button == 'csv':
        csvDaten = csv.writer(open('personen.csv', 'a'), delimiter=' ',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvDaten.writerow(liste)
       
        html = csv_view_template
    
    else:
        html = html_form_template % (name, vorname, gebOrt, groesse, gebDatum)
     
    return html


#server = make_server('', 8080, demo_app)
server = make_server('', 8080, application)
print 'Server started.'
server.serve_forever()
print 'Server stopped.'