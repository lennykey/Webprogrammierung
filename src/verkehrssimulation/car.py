"""
car.py - functions for moving cars.
"""


def drive(position, speed):
    """ Calculate new position (in meters) depending on speed (in km/h).
    """
    return position + speed/3.6


def accelerate(speed=0.0, coeff=5, factor=10):
    """ Increase the speed by a value derived from the coefficient
        argument given (a value between 10 and -10).
    """
    if speed < 10.0:
        divisor = 10.0
    else:
        divisor = speed
    newSpeed = speed + factor * coeff / divisor
    if newSpeed < 0.0:
        newSpeed = 0.0
    return newSpeed


def brake(speed, coeff):
    """ Reduce the speed by a value derived from the braking coefficient
        argument given (a value between 0 and 10).
    """
    return accelerate(speed, -coeff, 40)