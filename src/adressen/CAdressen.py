'''
Created on 06.04.2010

@author: Andres Cuartas
'''

class Adressen(object):
    '''
    classdocs
    '''
    def __init__(self, anrede, titel, vorname, nachname, strasse, plz, ort):
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
        Gibt das Adresslabel aus
        '''
                
        print(self.__anrede + ' ' +  self.__titel + ' ' + self.__vorname + ' ' + self.__nachname)
        print(self.__strasse)
        print('')
        print(self.__plz + ' ' + self.__ort)
        
        
        