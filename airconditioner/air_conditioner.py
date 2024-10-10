class Ac:

    def __init__(self):
        self.is_on = False
        self.temperature = 16

    def power_status(self):
        return self.is_on

    def get_temperature(self):
        return self.temperature

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        self.temperature = 16

    def increase_temperature(self):
        if self.is_on:
            self.temperature_increment()
        else:
            return self.error_message()

    def decrease_temperature(self):
        if self.is_on:
             self.temperature_decrement()
        else:
            return self.error_message()

    def temperature_increment(self):
        if 16 <= self.temperature <= 30:
            self.temperature += 1
        else:
            pass

    def temperature_decrement(self):
        if 16 <= self.temperature <= 30:
            self.temperature -= 1
        else:
            self.temperature = self.temperature

    @staticmethod
    def error_message():
        return "Ac is not On"
