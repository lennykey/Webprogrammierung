'''
Created on 06.04.2010

@author: Andres Cuartas
'''

class Adressen(object):
    '''
    classdocs
    '''
    def __init__(self, anrede='', titel='', vorname='', nachname='', strasse='', plz='', ort=''):
        '''
        Constructor
        '''
        
        self.__anrede= anrede
        self.__titel= titel
        self.__vorname= vorname 
        self.__nachname= nachname
        self.__strasse= strasse
        self.__plz= plz
        self.__ort= ort
        
    def format(self):
        '''
        Gibt das Adresslabel zurueck
        '''
        if self.__anrede:
            self.__anrede = self.__anrede + ' '
        if self.__titel:
            self.__titel= self.__titel + ' '
        if self.__vorname:
            self.__vorname = self.__vorname + ' '
        if self.__nachname:
            self.__nachname = self.__nachname + ' '
        if self.__strasse:
            self.__strasse= self.__strasse + ' '
        if self.__plz:
            self.__plz= self.__plz + ' '
        if self.__ort:
            self.__ort= self.__ort+ ' '
                
        liste= []
        zeile1= self.__anrede + self.__titel + self.__vorname + self.__nachname + '\n'
        zeile2= self.__strasse + '\n'
        zeile3= '\n'
        zeile4= self.__plz + self.__ort
        
        liste.append(zeile1)
        liste.append(zeile2)
        liste.append(zeile3)
        liste.append(zeile4)
        
        mystring= ''.join(liste)        
        
        return mystring
        
        
        