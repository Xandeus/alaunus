#!/usr/bin/env python3
class LEDAnimation:
    def __init__(self, name, cycle_function):
        self.name = name
        self.cycle_function = cycle_function 
        self.isActive = True

    def run(self, values):
        self.cycle_function(values)

    def deactivate(self):
        self.isActive = False

    def activate(self):
        self.isActive = True

    def isActive(self):
        return self.isActive
