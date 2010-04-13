class World(object):
    cars= []
    
    def __init__(self, cars):
        self.cars = cars
        
    def addCar(self, car):
        self.cars.append(car)
    
    def step(self, action):
        
        for car in self.cars:
            if action >= 0:
                car.accelerate(action)
            else:
                car.brake(action)
        
            car.drive()
        
    
    def report(self):
        for idx, car in enumerate(self.cars):
            print idx, '/', car.color , car.position , car.speed
            
        
        #print idx, '/', color, ':', position, speed 
        #print '/', color, ':', position, speed