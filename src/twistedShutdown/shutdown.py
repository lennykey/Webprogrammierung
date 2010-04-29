"""
Twisted Web-Anwendung, die ein Shutdownbefehl ueber callLater aufruft.
BS: Ubuntu mit Gnomeoberflaeche
"""
from twisted.web import http
import os

class RequestHandler(http.Request):
    


    def process(self):
        print self.uri
        liste = self.args
        
        self.write('<html>')
        self.write('<head>')
        self.write('<title>Twisted Shutdown</title>')
        self.write('</head>')
        self.write('<body>')
        self.write('<h1>Shutdown</h1>')
        self.write('<form methond="post">')
        self.write('Zeit in Minuten: <input type="text" name="time" value="%s"/>'
                    % liste.get('time', '0')[0])
        #self.write('Ihr Systempasswort: <input type="password" name="password" value="%s"/>' % liste.get('password', ' ')[0])
        
        
        if liste.get('time', '0')[0] != '0':
            #befehl =  "sudo shutdown -P %s "  % (liste.get('time')[0])
            #print befehl
            #args = shlex.split(befehl)

            #reactor.callLater(int(liste.get('time')[0]) * 60, lambda: os.popen('sudo shutdown -P now'))
            
            reactor.callLater(int(liste.get('time')[0]) * 60,
                               lambda: os.popen('dbus-send --print-reply \
                                --dest=org.gnome.SessionManager \
                                 /org/gnome/SessionManager \
                                 org.gnome.SessionManager.RequestShutdown'))
            
            self.write('<br/><br/><span>Das System faehrt in %s Minuten runter </span><br/></br>'
                        % (liste.get('time')[0]) )
            
            #back = subprocess.Popen(args)
            #back = subprocess.Popen("sudo shutdown -P %s % liste.get('time')[0]")
                    #print back.communicate()[0] 
            
        
        self.write('<input type="submit" value="Shutdown"/>')
        
        self.write('</body>')
        self.write('</html>')
        self.finish()


class HttpServer(http.HTTPChannel):

    requestFactory = RequestHandler


class HttpFactory(http.HTTPFactory):

    protocol = HttpServer


if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.listenTCP(8000, HttpFactory())
    reactor.run()