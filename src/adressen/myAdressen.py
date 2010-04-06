'''
Created on 06.04.2010

@author: Andres Cuartas
'''

#from adressen.CAdressen import Adressen 
from CAdressen import Adressen

if __name__ == '__main__':
    def main():
        myAdresse= Adressen('Herr', 'Doctor', 'Michael', 'Mayer', 'Brunnenstr. 5', '86150', 'Augsburg' )
        myAdresse.format()
        

    main()