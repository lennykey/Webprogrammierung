"""
Twisted Web-Anwendung, die ein Shutdownbefehl ueber callLater aufruft.
BS: Ubuntu mit Gnomeoberflaeche
"""
from twisted.web import http
import os
import time
import re

class RequestHandler(http.Request):
    
    html_template_formular= '''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
       "http://www.w3.org/TR/html4/strict.dtd">
    <html>
    <head>
    <title>Einzeilige Eingabefelder definieren</title>
    </head>
    <body>
 
    <h1>Formular f&uuml;r Personendaten</h1>

    <form method="post">
      <p>Vorname:<br><input name="vorname" type="text" value="%s"></p>
      <p>Nachname:<br><input name="nachname" type="text" value="%s" ></p>
      <p>Geburtsdatum:<br><input name="geburtsdatum" type="text" value="%s" \
       ></p>
      <p>Strasse<br><input name="strasse" type="text" value="%s" ></p>
      <p>Nr.:<br><input name="nr" type="text" value="%s" ></p>
      <p>PLZ:<br><input name="plz" type="text" value="%s" ></p>
      <p>Wohnort:<br><input name="wohnort" type="text" value="%s" ></p>
      <input type="submit" name="enter" value="Anzeigen" />
    </form>

    </body>
    </html>
    '''
    
    html_template_anzeige = '''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
       "http://www.w3.org/TR/html4/strict.dtd">
    <html>
    <head>
    <title>Einzeilige Eingabefelder definieren</title>
    </head>
    <body>

    <h1>Ihre Daten</h1>

      <p>Vorname: %s </p>
      <p>Zuname: %s </p>
      <p>Geburtsdatum: %s </p>
      <p>Strasse: %s %s </p>
      <p>PLZ: %s</p>
      <p>Wohnort: %s</p>
      
      <form method="post">
      <input name="vorname" type="hidden" value="%s"></p>
      <input name="nachname" type="hidden" value="%s" ></p>
      <input name="geburtsdatum" type="hidden" value="%s" ></p>
      <input name="strasse" type="hidden" value="%s" ></p>
      <input name="nr" type="hidden" value="%s" ></p>
      <input name="plz" type="hidden" value="%s" ></p>
      <input name="wohnort" type="hidden" value="%s" ></p>
      <input type="submit" name="enter" value="Zurueck" />
      <form>
      
    </body>
    </html>
    '''
    
    
    def process(self):
        print self.uri
        liste = self.args
        
        vorname = ''.join(liste.get('vorname', 'Vorname')[0:])
        nachname = ''.join(liste.get('nachname', 'Nachname')[0:])
        
        enter = ''.join(liste.get('enter', ' ')[0:])
        try:
            datum = time.strptime(''.join(liste.get('geburtsdatum',
                                '1-1-1980')[0:]), '%d-%m-%Y')
            geburtsdatum= str(datum.tm_mday)+'-'+ str(datum.tm_mon)+ '-' \
                                                         + str(datum.tm_year)
        except ValueError:
            geburtsdatum = 'Fehler: 01-01-1980'
            enter = 'error'
        
        if enter is not 'error':
            enter= ''.join(liste.get('enter', ' ')[0:])
        
        strasse = ''.join(liste.get('strasse', 'Strasse')[0:])
        
        nr = ''.join(liste.get('nr', '0')[0:])
        try:
            nr = re.match('[0-9]+', nr).group()
        except AttributeError:
            nr= 'Nur Zahlen Bitte'      
            enter = 'error'          
        
        
        plz= ''.join(liste.get('plz', '12345')[0:5])
        try:
            plz = re.match('[0-9]{5}', plz).group()
        except AttributeError:
            plz= 'Nur Zahlen Bitte (min. 5 Zahlen)'      
            enter = 'error'          
            
        wohnort= ''.join(liste.get('wohnort', 'Geburtsort')[0:])
        
        
        
        
        print vorname
        print nachname
        print enter
        
        if enter == 'Anzeigen':
            self.write(self.html_template_anzeige % (vorname, nachname,
                                                      geburtsdatum, strasse,
                                                      nr, plz, wohnort,
                                                      vorname, nachname,
                                                      geburtsdatum, strasse, 
                                                      nr, plz, wohnort))
            
        elif enter == 'Zurueck':
            self.write(self.html_template_formular % (vorname, nachname,
                                                      geburtsdatum, strasse,
                                                      nr, plz, wohnort))
        else:
            self.write(self.html_template_formular % (vorname, nachname,
                                                      geburtsdatum, strasse,
                                                      nr, plz, wohnort))
            
                                        
        
        self.finish()
                

class HttpServer(http.HTTPChannel):

    requestFactory = RequestHandler


class HttpFactory(http.HTTPFactory):

    protocol = HttpServer


if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.listenTCP(8000, HttpFactory())
    reactor.run()