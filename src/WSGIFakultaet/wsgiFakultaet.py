from wsgiref.simple_server import make_server, demo_app
from cgi import FieldStorage
import fibbo


html_template = '''<html>
<head>
  <title>Beispiel Formular-Verarbeitung</title>
</head>
<body>
  <form method="post">
    <h3>Bitte eine Zahl eingeben:</h3>
    <p>
      <input type="text" name="eingabe" value="%s" />
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

    input = form.getlist('eingabe')
    if input:
        eingabe = int(input[0])
        ausgabe = fibbo.fibbo(eingabe)
    else:
        eingabe = ausgabe = ''

    return [html_template % (eingabe, ausgabe)]


#server = make_server('', 8080, demo_app)
server = make_server('', 8080, application)
print 'Server started.'
server.serve_forever()
print 'Server stopped.'