'''
Created on 06.04.2010

@author: Andres Cuartas
'''

#from adressen.CAdressen import Adressen 
from CAdressen import Adressen

if __name__ == '__main__':
    def main():
        myAdresse= Adressen(anrede='Herr', titel='Prof.', vorname='Michael', nachname='Mayer', strasse='Brunnenstr. 5', plz='86150', ort='Augsburg' )
        label= myAdresse.format()
        print label
        

    main()