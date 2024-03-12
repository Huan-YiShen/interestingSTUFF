import random

class Particle():
    def __init__(self, name = None):
        self.name = name

    def __str__(self):
        n = "Anonymous"
        if self != None:
            n = self.name
            
        return n


class unitParticle(Particle):
    stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]

    def takeStep(self):
        return random.choice(stepChoices)


class BiasedParticle(Particle):
    ''' particle is biasied towards positive y'''
    stepChoices = [(0.0, 1.1), (0.0, -0.9), (1.0, 0.0), (-1.0, 0.0)]

    def takeStep(self):     
        return random.choice(stepChoices)
