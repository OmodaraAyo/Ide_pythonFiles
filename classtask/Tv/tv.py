from unittest import expectedFailure


class Tv:
    def __init__(self):
        self.turn_on = False
        self.channel = 1
        self.volume_level = 0

    def turn_On(self):
        self.turn_on= True
        return self.turn_on

    def turn_0ff(self):
        self.turn_on = False
        return self.turn_on

    def get_channel(self):
            return self.channel

    def set_channel(self, channel):
        if self.turn_on and 1 < channel <= 100:
            self.channel = channel
        if self.turn_on and channel > 100:
            return f"Channel cannot go above 100"
        if self.turn_on and channel < 0:
            return f"Channel cannot go below 0"

    def get_volume(self):
            return self.volume_level

    def set_volume(self, volume):
        if self.turn_on and 0 <= volume <= 100:
            self.volume_level = volume
        if self.turn_on and volume > 100:
            return f"Volume cannot go above 100"
        if self.turn_on and volume < 0:
            return f"Volume cannot go below 0"

    def channel_up(self):
        if self.turn_on:
            self.channel += 1

    def channel_down(self):
        if self.turn_on:
            self.channel -= 1

    def volume_up(self):
        if self.turn_on:
            self.volume_level += 1

    def volume_down(self):
        if self.turn_on:
            self.volume_level -= 1
