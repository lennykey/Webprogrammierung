from CWorld import World
from Ccar import Car



if __name__ == '__main__':
    BlueBeetle = Car('blau', 0, 0)
    Ferrari = Car('rot', 0, 0)
    carList= [BlueBeetle, Ferrari]
    
    SilberPfeil = Car('silber', 0, 0) 
    SilberPfeil.accelerate()
    #SilberPfeil.drive()
    
    myWorld = World(carList)
    myWorld.addCar(SilberPfeil)
    
    myWorld.step(1)
    myWorld.step(1)
    myWorld.step(1)
    myWorld.step(1)
    myWorld.step(1)
    myWorld.step(1)


    
    myWorld.report()





