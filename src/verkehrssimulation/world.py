"""
world.py - variables and functions for simulating a traffic world.
"""


import car


# variables holding the states of the cars:
colors = []
positions = []
speeds = []


def addCar(color, position=0, speed=0):
    colors.append(color)
    positions.append(position)
    speeds.append(speed)


def step(actions):
    """ Execute one simulation step. The ``actions`` parameter is
        a list of acceleration (>=0) or braking (<0) coefficients
        to apply to each car.
    """
    global positions, speeds # necessary in order to change these variables
    newPositions = []
    newSpeeds = []
    for position, speed, action in zip(positions, speeds, actions):
        newPositions.append(car.drive(position, speed))
        if action >= 0:
            newSpeed = car.accelerate(speed, action)
        else:
            newSpeed = car.brake(speed, -action)
        newSpeeds.append(newSpeed)
    positions = newPositions
    speeds = newSpeeds


def report():
    for idx, car in enumerate(zip(colors, positions, speeds)):
        color, position, speed = car
        print idx, '/', color, ':', position, speed
