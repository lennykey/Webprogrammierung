class Car(object):
    def __init__(self, color, position, speed):
        self.color = color
        self.position = position
        self.speed = speed
    
    def accelerate(self, coeff=5, factor=10):
        """ Increase the speed by a value derived from the coefficient
            argument given (a value between 10 and -10).
        """
        if self.speed < 10.0:
            divisor = 10.0
        else:
            divisor = self.speed
        newSpeed = self.speed + factor * coeff / divisor
        if newSpeed < 0.0:
            newSpeed = 0.0
        
        self.speed = newSpeed
    
    def brake(self, action):
        self.accelerate(action, 40)
        
    def drive(self):
        """ Calculate new position (in meters) depending on speed (in km/h).
        """
        self.position = self.position + self.speed/3.6