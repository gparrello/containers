import appdaemon.plugins.hass.hassapi as hass
from random import randrange, choice

class DiscoLights(hass.Hass):

    def initialize(self):
        self.switch = self.args['switch']
        self.lights = self.args['lights']
        self.color = self.random_color()
        self.listen_state(self.start, self.switch, new = 'on')
        self.listen_state(self.set_color, self.switch, attribute = 'rgb_color')

    def start(self, entity, attribute, old, new, kwargs):
        # [self.log(self.get_state(l, attribute='all')) for l in self.lights]
        [self.turn_off(l) for l in self.lights]
        if new == 'on':
            for light in self.lights:
                self.run_in(
                    self.loop_light,
                    delay=1,
                    random_start=0,
                    random_end=0,
                    light = light
                )

    @staticmethod
    def random_color():
        # playing with reds
        blue = choice((0,randrange(255)))
        green = randrange(255) if blue == 0 else 0
        red = 255
        return (red, green, blue)

    def set_color(self, entity, attribute, old, new, kwargs):
        self.log(new)
        self.color = new

    def loop_light(self, kwargs):
        light = kwargs['light']
        self.toggle(light, rgb_color=self.color, brightness=255)
        if self.is_enabled():
            self.run_in(
                self.loop_light,
                delay=1,
                random_start=-3,
                random_end=3,
                light=light
            )
        else:
            [(self.turn_off(l) if self.get_state(l) == 'on') for l in self.lights]

    def is_enabled(self):
        if self.get_state(self.switch) == 'on':
            return True
        else:
            return False
