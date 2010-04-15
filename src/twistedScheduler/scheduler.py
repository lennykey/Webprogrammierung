#! /usr/bin/python


"""
Twisted: ein einfacher Job-Scheduler: Liest Datum/Uhrzeit und Kommando aus einer Datei,
 startet Kommando zur angegebenen Zeit. Kann auch mehrere Kommandos mit Datum und Uhrzeit auslesen
"""

from twisted.internet import reactor
import time
import os

def printTime():
    """
    Wird nur zu Testzwecken benoetigt: Hier wird jede Sekunde die Uhrzeit ausgegeben
    """
    print 'Time', time.strftime('%H:%M:%S')
    reactor.callLater(1, printTime)

def startCommands(command):
    """
    Wird durch reactor.callLater() aufgerufen, um die Kommandos zeitgesteurt abzusetzen
    """
    os.popen(command)   #Was ist der Unterschied zu os.system()
    print ('Ausgefuehrt mit %(Kommando)s folgendem Kommando' % {'Kommando':command})
            
    
def scheduler():
    """
    Liest die Kommandos aus der Datei aus und fuehrt sie zeitgesteuert aus. Wenn die Zeit bereits
    verstrichen ist, wird das Kommando ignoriert.
    """
    commandFile = open('commands.txt')
    for line in commandFile:
        execTime, command = line.split(';')
        execTime = time.mktime(time.strptime(execTime, "%d.%m.%Y um %H:%M Uhr"))
        command = command.strip()
        
        aktuelleZeit = time.mktime(time.localtime())
        #print aktuelleZeit
        sekundenBisZumStart = execTime - aktuelleZeit
        #print 'Unterschied: ' + str(unterschied) 
        
        #print command
        
        if sekundenBisZumStart <= 0:
            print 'Leider liegt die Zeit bereits in der Vergangenheit, Kommando wird nicht ausgefuehrt'
        else:
            reactor.callLater(sekundenBisZumStart, startCommands, command )
            print ('Start in %i Sekunden' % sekundenBisZumStart)
            

    #printTime()
        

reactor.callLater(0, scheduler )
  

#printTime()
print 'Running...'
reactor.run()
print '...finished'
