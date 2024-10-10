class Bike:

    def __init__(self):
        self.isOn = False
        self.gear = 0
        self.acceleration = 0

    def turn_on(self):
        self.isOn = True
        return self.isOn

    def turn_off(self):
        self.isOn = False
        self.gear = 0
        self.acceleration = 0
        return self.isOn

    def error_message(self):
        return "Bike is not On"

    def accelerate(self, gear, speed):
        self.gear = gear
        self.acceleration = speed
        if self.isOn:
            if self.gear == 1 or 0 <= speed <= 20:
               self.acceleration = gear + speed
            if self.gear == 2 or 21 < speed <= 30:
                self.acceleration = gear + speed
            if self.gear == 3 or 31 < speed <= 40:
                self.acceleration = gear + speed
            if self.gear == 4 or speed >= 41:
                self.acceleration = gear + speed
        else:
           return self.error_message()

    def decelerate(self, gear, speed):
        self.gear = gear
        self.acceleration = speed
        if self.isOn:
            if self.gear == 1 or 0 <= speed <= 20:
                self.acceleration = speed - gear
            if self.gear == 2 or 21 < speed <= 30:
                self.acceleration = speed - gear
            if self.gear == 3 or 31 < speed <= 40:
                self.acceleration = speed - gear
            if self.gear == 4 or speed >= 41:
                self.acceleration = speed - gear
        else:
            return self.error_message()

    def get_speed(self):
        return self.acceleration