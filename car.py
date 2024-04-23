from init import *
from random import *

class Car:
    def __init__(self, vertex):
        self.vertex = vertex
        self.s = 0.5
        self.v = 0
        self.acc = a_friction
        self.cross_allowed = False
        self.handler = None

    def set_acc(self, mode: int):
        if mode == 0:
            self.acc = a_friction
        elif mode == 1:
            self.acc = a_gas
        else:
            self.acc = a_brake

    def update(self):
        self.v += dt * self.acc
        self.v = max(0, self.v)
        self.v = min(v_max, self.v)
        self.s += self.v * dt
        if self.s >= 1:

            if self.handler is not None:
                if self.vertex[0] == self.handler.vertex:
                    self.handler.car_crossed()
                    self.cross_allowed = False
                    self.handler = None
            self.vertex = choice(vertices[self.vertex])
            self.s -= 1

